import pytest
from tasks import *

ver = 4

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

def test_replace():

    # testing replace
    new_task_before = Task("Finish book", "Roy", False)
    new_task_after = new_task_before._replace(id=10, done=True)
    expected_task = Task("Finish book", "Roy", True, 10)
    assert new_task_after == expected_task

@pytest.mark.smoke
def test_list_raises():

    # list_task should raise exception if input data type is other than none or str
    with pytest.raises(TypeError):
        list_tasks(owner = 123)

@pytest.mark.get
@pytest.mark.smoke
def test_gettaskid_raises():

    # get task id should raise type error when incorrect data type is used
    with pytest.raises(TypeError):
        get_id(task_id = '12')

@pytest.mark.skipif(ver < 3, reason="Version is less than 3")
def test_skipipmethod():
    assert 1==1


@pytest.mark.xfail
def test_expectfail():

    # get task id should raise type error when incorrect data type is used
    # if input is right -> it should XFAIL
    # if input is wrong -> it should XPASS
    with pytest.raises(TypeError):
        get_id(task_id = 1)


tasks_to_try = ('0','1','hello', 'you')
@pytest.mark.parametrize('taskid', tasks_to_try)
def test_multipara(taskid):

    with pytest.raises(TypeError):
        get_id(task_id = taskid)