import pytest

@pytest.fixture(scope='session')
def my_cool_fixture():
    '''This is my pytest fixture (set of code to
    execute bofore/after my scope.'''
    print("*************This is the SETUP fixture to run before your scope of your fixture.")

    yield my_cool_fixture

    print("***********This is the TEARDOWN steps after each of  your scope*******")