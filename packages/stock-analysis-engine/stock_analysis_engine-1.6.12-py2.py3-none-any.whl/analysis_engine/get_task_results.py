"""
Get Task Results

Debug by setting the environment variable:

::

        export DEBUG_TASK=1

"""

import analysis_engine.consts as ae_consts
import spylunking.log.setup_logging as log_utils

log = log_utils.build_colorized_logger(name=__name__)


def get_task_results(
        work_dict=None,
        result=None,
        **kwargs):
    """get_task_results

    If celery is disabled by the
    environment key ``export CELERY_DISABLED=1``
    or requested in the ``work_dict['celery_disabled'] = True`` then
    return the task result dictionary, otherwise
    return ``None``.

    This method is useful for allowing tests
    to override the returned payloads during task chaining
    using ``@mock.patch``.

    :param work_dict: task work dictionary
    :param result: task result dictionary
    :param kwargs: keyword arguments
    """

    send_results_back = None
    cel_disabled = False
    if work_dict:
        if ae_consts.is_celery_disabled(
                work_dict=work_dict):
            send_results_back = result
            cel_disabled = True
    # end of sending back results if told to do so

    if ae_consts.ev('DEBUG_TASK', '0') == '1':
        status = ae_consts.NOT_SET
        err = None
        record = None
        label = None
        if result:
            status = result.get(
                'status',
                ae_consts.NOT_SET)
            err = result.get(
                'err',
                None)
            record = result.get(
                'rec',
                None)
        if work_dict:
            label = work_dict.get(
                'label',
                None)
        log_id = 'get_task_results'
        if label:
            log_id = '{} - get_task_results'.format(
                label)

        result_details = record
        if record:
            result_details = ae_consts.ppj(record)

        status_details = status
        if status:
            status_details = ae_consts.get_status(status=status)

        work_details = work_dict
        if work_dict:
            work_details = ae_consts.ppj(work_dict)

        if status == ae_consts.SUCCESS:
            log.info(
                '{} celery_disabled={} '
                'status={} err={} work_dict={} result={}'.format(
                    log_id,
                    cel_disabled,
                    status_details,
                    err,
                    work_details,
                    result_details))
        else:
            if cel_disabled:
                log.error(
                    '{} celery_disabled={} '
                    'status={} err={} work_dict={} result={}'.format(
                        log_id,
                        cel_disabled,
                        status_details,
                        err,
                        work_details,
                        result_details))
            else:
                log.info(
                    '{} celery_disabled={} '
                    'status={} err={} work_dict={} result={}'.format(
                        log_id,
                        cel_disabled,
                        status_details,
                        err,
                        work_details,
                        result_details))
    # end of if debugging the task results

    return send_results_back
# end of get_task_results
