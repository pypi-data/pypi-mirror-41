"""
**Get New Pricing Data Task**

This will fetch data (pricing, financials, earnings, dividends, options,
and more) from these sources:

#.  IEX

#.  Tradier

#.  Yahoo - disabled as of 2019/01/03

**Detailed example for getting new pricing data**

.. code-block:: python

    import datetime
    import build_get_new_pricing_request
    from analysis_engine.api_requests
    from analysis_engine.work_tasks.get_new_pricing_data
        import get_new_pricing_data

    # store data
    cur_date = datetime.datetime.now().strftime('%Y-%m-%d')
    work = build_get_new_pricing_request(
        label='get-pricing-{}'.format(cur_date))
    work['ticker'] = 'TSLA'
    work['s3_bucket'] = 'pricing'
    work['s3_key'] = '{}-{}'.format(
        work['ticker'],
        cur_date)
    work['redis_key'] = '{}-{}'.format(
        work['ticker'],
        cur_date)
    work['celery_disabled'] = True
    res = get_new_pricing_data(
        work)
    print('full result dictionary:')
    print(res)
    if res['data']:
        print(
            'named datasets returned as '
            'json-serialized pandas DataFrames:')
        for k in res['data']:
            print(' - {}'.format(k))

.. warning:: When fetching pricing data from sources like IEX,
             Please ensure the returned values are
             not serialized pandas Dataframes to prevent
             issues with celery task results. Instead
             it is preferred to returned a ``df.to_json()``
             before sending the results into the
             results backend.

.. tip:: This task uses the `analysis_engine.work_tasks.
    custom_task.CustomTask class <https://github.com/A
    lgoTraders/stock-analysis-engine/blob/master/anal
    ysis_engine/work_tasks/custom_task.py>`__ for
    task event handling.

**Sample work_dict request for this method**

`analysis_engine.api_requests.build_get_new_pricing_request <https://
github.com/AlgoTraders/stock-analysis-engine/blob/master/
analysis_engine/api_requests.py#L49>`__

**Supported Environment Variables**

::

    export DEBUG_RESULTS=1

"""

import datetime
import copy
import celery
import analysis_engine.consts as ae_consts
import analysis_engine.utils as ae_utils
import analysis_engine.iex.consts as iex_consts
import analysis_engine.td.consts as td_consts
import analysis_engine.build_result as build_result
import analysis_engine.get_task_results as get_task_results
import analysis_engine.work_tasks.custom_task as custom_task
import analysis_engine.options_dates as opt_dates
import analysis_engine.work_tasks.publish_pricing_update as publisher
import analysis_engine.yahoo.get_data as yahoo_data
import analysis_engine.iex.get_data as iex_data
import analysis_engine.td.get_data as td_data
import analysis_engine.send_to_slack as slack_utils
import spylunking.log.setup_logging as log_utils

log = log_utils.build_colorized_logger(name=__name__)


@celery.task(
    bind=True,
    base=custom_task.CustomTask,
    queue='get_new_pricing_data')
def get_new_pricing_data(
        self,
        work_dict):
    """get_new_pricing_data

    Get Ticker information on:

    - prices - turn off with ``work_dict.get_pricing = False``
    - news - turn off with ``work_dict.get_news = False``
    - options - turn off with ``work_dict.get_options = False``

    :param work_dict: dictionary for key/values
    """

    label = 'get_new_pricing_data'

    log.info(
        'task - {} - start '
        'work_dict={}'.format(
            label,
            work_dict))

    ticker = ae_consts.TICKER
    ticker_id = ae_consts.TICKER_ID
    rec = {
        'pricing': None,
        'options': None,
        'calls': None,
        'puts': None,
        'news': None,
        'daily': None,
        'minute': None,
        'quote': None,
        'stats': None,
        'peers': None,
        'iex_news': None,
        'financials': None,
        'earnings': None,
        'dividends': None,
        'company': None,
        'exp_date': None,
        'publish_pricing_update': None,
        'date': ae_utils.utc_now_str(),
        'updated': None,
        'version': ae_consts.DATASET_COLLECTION_VERSION
    }
    res = {
        'status': ae_consts.NOT_RUN,
        'err': None,
        'rec': rec
    }

    try:
        ticker = work_dict.get(
            'ticker',
            ticker)
        ticker_id = work_dict.get(
            'ticker_id',
            ae_consts.TICKER_ID)
        s3_bucket = work_dict.get(
            's3_bucket',
            ae_consts.S3_BUCKET)
        s3_key = work_dict.get(
            's3_key',
            ae_consts.S3_KEY)
        redis_key = work_dict.get(
            'redis_key',
            ae_consts.REDIS_KEY)
        exp_date = work_dict.get(
            'exp_date',
            None)
        cur_date = datetime.datetime.utcnow()
        cur_strike = work_dict.get(
            'strike',
            None)
        contract_type = str(work_dict.get(
            'contract',
            'C')).upper()
        label = work_dict.get(
            'label',
            label)
        iex_datasets = work_dict.get(
            'iex_datasets',
            iex_consts.DEFAULT_FETCH_DATASETS)
        td_datasets = work_dict.get(
            'td_datasets',
            td_consts.DEFAULT_FETCH_DATASETS_TD)
        fetch_mode = work_dict.get(
            'fetch_mode',
            ae_consts.FETCH_MODE_ALL)
        td_token = work_dict.get(
            'td_token',
            td_consts.TD_TOKEN)

        # control flags to deal with feed issues:
        get_iex_data = True
        get_td_data = True

        if (
                fetch_mode == ae_consts.FETCH_MODE_ALL
                or str(fetch_mode).lower() == 'all'):
            get_iex_data = True
            get_td_data = True
        elif (
                fetch_mode == ae_consts.FETCH_MODE_YHO
                or str(fetch_mode).lower() == 'yahoo'):
            get_iex_data = False
            get_td_data = False
        elif (
                fetch_mode == ae_consts.FETCH_MODE_IEX
                or str(fetch_mode).lower() == 'iex'):
            get_iex_data = True
            get_td_data = False
        elif (
                fetch_mode == ae_consts.FETCH_MODE_TD
                or str(fetch_mode).lower() == 'td'):
            get_iex_data = False
            get_td_data = True
        else:
            log.debug(
                '{} - unsupported fetch_mode={} value'.format(
                    label,
                    fetch_mode))

        if get_td_data:
            missing_td_token = [
                'MISSING_TD_TOKEN',
                'SETYOURTDTOKEN',
                'SETYOURTRADIERTOKENHERE'
            ]
            if td_token in missing_td_token:
                log.warn(
                    '{} - please set a valid Tradier Account token ('
                    'https://developer.tradier.com/user/sign_up'
                    ') to fetch pricing data from Tradier. It must be '
                    'set as an environment variable like: '
                    'export TD_TOKEN=<token>'
                    ''.format(
                        label))
                get_td_data = False
        # sanity check - disable Tradier fetch if the token is not set

        """
        as of Thursday, Jan. 3, 2019:
        https://developer.yahoo.com/yql/
        Important EOL Notice: As of Thursday, Jan. 3, 2019
        the YQL service at query.yahooapis.com will be retired
        """
        get_yahoo_data = False

        if not exp_date:
            exp_date = opt_dates.option_expiration(
                date=exp_date)
        else:
            exp_date = datetime.datetime.strptime(
                exp_date,
                '%Y-%m-%d')

        rec['updated'] = cur_date.strftime('%Y-%m-%d %H:%M:%S')
        log.info(
            '{} getting pricing for ticker={} '
            'cur_date={} exp_date={} '
            'yahoo={} iex={}'.format(
                label,
                ticker,
                cur_date,
                exp_date,
                get_yahoo_data,
                get_iex_data))

        yahoo_rec = {
            'ticker': ticker,
            'pricing': None,
            'options': None,
            'calls': None,
            'puts': None,
            'news': None,
            'exp_date': None,
            'publish_pricing_update': None,
            'date': None,
            'updated': None
        }

        # disabled on 2019-01-03
        if get_yahoo_data:
            log.info(
                '{} yahoo ticker={}'.format(
                    label,
                    ticker))
            yahoo_res = yahoo_data.get_data_from_yahoo(
                work_dict=work_dict)
            if yahoo_res['status'] == ae_consts.SUCCESS:
                yahoo_rec = yahoo_res['rec']
                log.info(
                    '{} yahoo ticker={} '
                    'status={} err={}'.format(
                        label,
                        ticker,
                        ae_consts.get_status(status=yahoo_res['status']),
                        yahoo_res['err']))
                rec['pricing'] = yahoo_rec.get('pricing', '{}')
                rec['news'] = yahoo_rec.get('news', '{}')
                rec['options'] = yahoo_rec.get('options', '{}')
                rec['calls'] = rec['options'].get(
                    'calls', ae_consts.EMPTY_DF_STR)
                rec['puts'] = rec['options'].get(
                    'puts', ae_consts.EMPTY_DF_STR)
            else:
                log.error(
                    '{} failed YAHOO ticker={} '
                    'status={} err={}'.format(
                        label,
                        ticker,
                        ae_consts.get_status(status=yahoo_res['status']),
                        yahoo_res['err']))
        # end of get from yahoo

        if get_iex_data:
            num_iex_ds = len(iex_datasets)
            log.debug(
                '{} iex datasets={}'.format(
                    label,
                    num_iex_ds))
            for idx, ft_type in enumerate(iex_datasets):
                dataset_field = iex_consts.get_ft_str(
                    ft_type=ft_type)

                log.info(
                    '{} iex={}/{} field={} ticker={}'.format(
                        label,
                        idx,
                        num_iex_ds,
                        dataset_field,
                        ticker))
                iex_label = '{}-{}'.format(
                    label,
                    dataset_field)
                iex_req = copy.deepcopy(work_dict)
                iex_req['label'] = iex_label
                iex_req['ft_type'] = ft_type
                iex_req['field'] = dataset_field
                iex_req['ticker'] = ticker
                iex_res = iex_data.get_data_from_iex(
                    work_dict=iex_req)

                if iex_res['status'] == ae_consts.SUCCESS:
                    iex_rec = iex_res['rec']
                    log.info(
                        '{} iex ticker={} field={} '
                        'status={} err={}'.format(
                            label,
                            ticker,
                            dataset_field,
                            ae_consts.get_status(status=iex_res['status']),
                            iex_res['err']))
                    if dataset_field == 'news':
                        rec['iex_news'] = iex_rec['data']
                    else:
                        rec[dataset_field] = iex_rec['data']
                else:
                    log.debug(
                        '{} failed IEX ticker={} field={} '
                        'status={} err={}'.format(
                            label,
                            ticker,
                            dataset_field,
                            ae_consts.get_status(status=iex_res['status']),
                            iex_res['err']))
                # end of if/else succcess
            # end idx, ft_type in enumerate(iex_datasets):
        # end of if get_iex_data

        if get_td_data:
            num_td_ds = len(td_datasets)
            log.debug(
                '{} td datasets={}'.format(
                    label,
                    num_td_ds))
            for idx, ft_type in enumerate(td_datasets):
                dataset_field = td_consts.get_ft_str_td(
                    ft_type=ft_type)

                log.info(
                    '{} td={}/{} field={} ticker={}'.format(
                        label,
                        idx,
                        num_td_ds,
                        dataset_field,
                        ticker))
                td_label = '{}-{}'.format(
                    label,
                    dataset_field)
                td_req = copy.deepcopy(work_dict)
                td_req['label'] = td_label
                td_req['ft_type'] = ft_type
                td_req['field'] = dataset_field
                td_req['ticker'] = ticker
                td_res = td_data.get_data_from_td(
                    work_dict=td_req)

                if td_res['status'] == ae_consts.SUCCESS:
                    td_rec = td_res['rec']
                    log.info(
                        '{} td ticker={} field={} '
                        'status={} err={}'.format(
                            label,
                            ticker,
                            dataset_field,
                            ae_consts.get_status(status=td_res['status']),
                            td_res['err']))
                    if dataset_field == 'tdcalls':
                        rec['tdcalls'] = td_rec['data']
                    if dataset_field == 'tdputs':
                        rec['tdputs'] = td_rec['data']
                    else:
                        rec[dataset_field] = td_rec['data']
                else:
                    log.critical(
                        '{} failed TD ticker={} field={} '
                        'status={} err={}'.format(
                            label,
                            ticker,
                            dataset_field,
                            ae_consts.get_status(status=td_res['status']),
                            td_res['err']))
                # end of if/else succcess
            # end idx, ft_type in enumerate(td_datasets):
        # end of if get_td_data

        update_req = {
            'data': rec
        }
        update_req['ticker'] = ticker
        update_req['ticker_id'] = ticker_id
        update_req['strike'] = cur_strike
        update_req['contract'] = contract_type
        update_req['s3_enabled'] = work_dict.get(
            's3_enabled',
            ae_consts.ENABLED_S3_UPLOAD)
        update_req['redis_enabled'] = work_dict.get(
            'redis_enabled',
            ae_consts.ENABLED_REDIS_PUBLISH)
        update_req['s3_bucket'] = s3_bucket
        update_req['s3_key'] = s3_key
        update_req['s3_access_key'] = work_dict.get(
            's3_access_key',
            ae_consts.S3_ACCESS_KEY)
        update_req['s3_secret_key'] = work_dict.get(
            's3_secret_key',
            ae_consts.S3_SECRET_KEY)
        update_req['s3_region_name'] = work_dict.get(
            's3_region_name',
            ae_consts.S3_REGION_NAME)
        update_req['s3_address'] = work_dict.get(
            's3_address',
            ae_consts.S3_ADDRESS)
        update_req['s3_secure'] = work_dict.get(
            's3_secure',
            ae_consts.S3_SECURE)
        update_req['redis_key'] = redis_key
        update_req['redis_address'] = work_dict.get(
            'redis_address',
            ae_consts.REDIS_ADDRESS)
        update_req['redis_password'] = work_dict.get(
            'redis_password',
            ae_consts.REDIS_PASSWORD)
        update_req['redis_db'] = int(work_dict.get(
            'redis_db',
            ae_consts.REDIS_DB))
        update_req['redis_expire'] = work_dict.get(
            'redis_expire',
            ae_consts.REDIS_EXPIRE)
        update_req['updated'] = rec['updated']
        update_req['label'] = label
        update_req['celery_disabled'] = True
        update_status = ae_consts.NOT_SET

        try:
            update_res = publisher.run_publish_pricing_update(
                work_dict=update_req)
            update_status = update_res.get(
                'status',
                ae_consts.NOT_SET)
            if ae_consts.ev('DEBUG_RESULTS', '0') == '1':
                log.info(
                    '{} update_res status={} data={}'.format(
                        label,
                        ae_consts.get_status(status=update_status),
                        ae_consts.ppj(update_res)))
            else:
                log.info(
                    '{} run_publish_pricing_update status={}'.format(
                        label,
                        ae_consts.get_status(status=update_status)))
            # end of if/else

            rec['publish_pricing_update'] = update_res
            res = build_result.build_result(
                status=ae_consts.SUCCESS,
                err=None,
                rec=rec)
        except Exception as f:
            err = (
                '{} publisher.run_publish_pricing_update failed '
                'with ex={}'.format(
                    label,
                    f))
            log.error(err)
            res = build_result.build_result(
                status=ae_consts.ERR,
                err=err,
                rec=rec)
        # end of trying to publish results to connected services

    except Exception as e:
        res = build_result.build_result(
            status=ae_consts.ERR,
            err=(
                'failed - get_new_pricing_data '
                'dict={} with ex={}').format(
                    work_dict,
                    e),
            rec=rec)
        log.error(
            '{} - {}'.format(
                label,
                res['err']))
    # end of try/ex

    if ae_consts.ev('DATASET_COLLECTION_SLACK_ALERTS', '0') == '1':
        env_name = 'DEV'
        if ae_consts.ev('PROD_SLACK_ALERTS', '1') == '1':
            env_name = 'PROD'
        done_msg = (
            'Dataset collected ticker=*{}* on env=*{}* '
            'redis_key={} s3_key={} iex={} yahoo={}'.format(
                ticker,
                env_name,
                redis_key,
                s3_key,
                get_iex_data,
                get_yahoo_data))
        log.debug(
            '{} sending slack msg={}'.format(
                label,
                done_msg))
        if res['status'] == ae_consts.SUCCESS:
            slack_utils.post_success(
                msg=done_msg,
                block=False,
                jupyter=True)
        else:
            slack_utils.post_failure(
                msg=done_msg,
                block=False,
                jupyter=True)
        # end of if/else success
    # end of publishing to slack

    log.info(
        'task - get_new_pricing_data done - '
        '{} - status={}'.format(
            label,
            ae_consts.get_status(res['status'])))

    return get_task_results.get_task_results(
        work_dict=work_dict,
        result=res)
# end of get_new_pricing_data


def run_get_new_pricing_data(
        work_dict):
    """run_get_new_pricing_data

    Celery wrapper for running without celery

    :param work_dict: task data
    """

    label = work_dict.get(
        'label',
        '')

    log.info(
        'run_get_new_pricing_data - {} - start'.format(
            label))

    response = build_result.build_result(
        status=ae_consts.NOT_RUN,
        err=None,
        rec={})
    task_res = {}

    # allow running without celery
    if ae_consts.is_celery_disabled(
            work_dict=work_dict):
        work_dict['celery_disabled'] = True
        task_res = get_new_pricing_data(
            work_dict)
        if task_res:
            response = task_res.get(
                'result',
                task_res)
            if ae_consts.ev('DEBUG_RESULTS', '0') == '1':
                response_details = response
                try:
                    response_details = ae_consts.ppj(response)
                except Exception:
                    response_details = response

                log.info(
                    '{} task result={}'.format(
                        label,
                        response_details))
        else:
            log.error(
                '{} celery was disabled but the task={} '
                'did not return anything'.format(
                    label,
                    response))
        # end of if response
    else:
        task_res = get_new_pricing_data.delay(
            work_dict=work_dict)
        rec = {
            'task_id': task_res
        }
        response = build_result.build_result(
            status=ae_consts.SUCCESS,
            err=None,
            rec=rec)
    # if celery enabled

    if response:
        if ae_consts.ev('DEBUG_RESULTS', '0') == '1':
            log.info(
                'run_get_new_pricing_data - {} - done '
                'status={} err={} rec={}'.format(
                    label,
                    ae_consts.get_status(response['status']),
                    response['err'],
                    response['rec']))
        else:
            log.info(
                'run_get_new_pricing_data - {} - done '
                'status={} err={}'.format(
                    label,
                    ae_consts.get_status(response['status']),
                    response['err']))
    else:
        log.info(
            'run_get_new_pricing_data - {} - done '
            'no response'.format(
                label))
    # end of if/else response

    return response
# end of run_get_new_pricing_data
