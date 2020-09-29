import pytest

# @pytest.fixture(scope='module')
# def setup():
#     print("*************This is the SETUP fixture to run first.")
#     yield setup
#     print("***********This is the TEARDOWN steps after each file")

def num_square(num):
    print(" Sample step function is running")
    return num * num

def num_sum(numbers: list):
    print(" num_sum function is running")
    return sum(numbers)


@pytest.mark.regression
def test_scenario1(my_cool_fixture):
    print(" Running scenario 1.")
    num = 8
    nums = [1,5,4]
    assert num_square(num) == 64
    assert num_sum(nums) == 10

@pytest.mark.regression
def test_scenario2(my_cool_fixture):
    try:
        print(" Running scenario 2.")
        num = 10
        assert num_square(num) == 100
    except AssertionError as err:
        print("Test scenario test_scenario2 Failed.")
        pytest.fail("Scenario 2 FAILED!!")

@pytest.mark.regression
#@pytest.mark.skip
def test_scenario3(my_cool_fixture):
    try:
        print(" Running scenario 3.")
        num = 5
        assert num_square(num) >= 24
    except AssertionError as err:
        print("Test scenario test_scenario3 Failed.")
        pytest.fail("Scenario 3 FAILED!!")


