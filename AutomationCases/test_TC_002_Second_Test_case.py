import pytest
from test_TC_001_First_Test_case import actual_result

def test_tc_001_Creating_User_testing():
    print('This is my test case code...')
    print('Test case is finished...')
    assert actual_result == False

@pytest.mark.Smoke
def test_tc_002_View_User_testing():
    print('This is my Smoke test case code...')
    print('Test case is finished...')
    assert actual_result == False

@pytest.mark.Sanity
def test_tc_003_Remove_User_testing():
    print('This is my Sanity test case code...')
    print('Test case is finished...')
    assert actual_result == True


