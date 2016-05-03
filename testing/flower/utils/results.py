from celery.result import AsyncResult
from celery.exceptions import TimeoutError

DEFAULT_TIMEOUT = 5


def get_results_by_taskid(task_id):
    """
    Utility to fetch results from celery result backend

    :params task_id: Task ID

    :returns: Result object
    """
    result = None
    try:
        result = AsyncResult(
            task_id, follow_parents=False,
            propagate=False)
    except TimeoutError, e:
        pass
    return result
