# for pytest,
# test file should either start or end with "test" i,e test_*.py or *_test.py
# test function should start with test

# fucntion 1
def func(x):
    return x+1

# fucntion 2
def check_val():
    x = (1,2,3)
    return x

# testing the fucnction 1
def test_func():
    assert func(3) == 4

# testing the function 2
def test_checkval():
    assert check_val() == (1,2,3)

# testing the function 1, but it won't run because function need to be started with test
def check_func():
    assert func(2) == 3

# testing the function 1, but it won't run because function need to be started with test_
def check_test():
    assert func(2)==3