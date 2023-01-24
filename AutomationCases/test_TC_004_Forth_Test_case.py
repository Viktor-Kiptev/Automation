import pytest
from test_TC_001_First_Test_case import actual_result

@pytest.mark.Smoke
def test_tc_001_Exit_testing():
    print('This is my Smoke Exit test case code...')
    print('Test case is finished...')
    assert actual_result == False

@pytest.mark.Sanity
def test_tc_002_Avatar_View_login():
    print('This is my Sanity test case code...')
    print('Test case is succesful view...')
    assert actual_result == True

def test_tc_003_Transaction_withholding():
    print('This is my test case code...')
    print('Test case is finished ...')
    assert actual_result == False

def test_tc_004_Transaction_withrraw():
    print('This is my test case code...')
    print('Test case is finished ...')
    assert actual_result == False