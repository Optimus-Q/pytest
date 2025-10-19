from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def list_tasks(owner = None):

    if owner and not isinstance(owner, str):
        raise TypeError('Owner must be in string type')
    
    return []

def get_id(task_id = 0):

    if not isinstance(task_id, int):
        raise TypeError("Task Id should be int type")
    
    return task_id

