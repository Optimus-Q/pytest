import pytest
from src.tasks import Task

@pytest.mark.skip()     # this will skip the test and it will give as "s" while running
def test_getdefault():
    
    # testing for the default data types
    data_update = Task()
    data_dict = data_update._asdict()
    expected = Task(None, None, False, None)
    assert data_dict == expected._asdict()


def test_getdefaults():
    
    # testing for the default data types
    data_update = Task()
    data_dict = data_update._asdict()
    expected = Task(None, None, False, None)
    assert data_dict == expected._asdict()

def test_memberclass():

    # testing the individual member class
    new_task = Task('Buy', 'Roy')
    assert new_task.summary == 'Buy'
    assert new_task.owner == 'Roy'
    assert (new_task.done, new_task.id) == (False, None)