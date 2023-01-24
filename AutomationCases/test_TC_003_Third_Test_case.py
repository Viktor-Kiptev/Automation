import pytest
from test_TC_001_First_Test_case import actual_result
@pytest.mark.Smoke
def test_tc_001_Go_to_main_page_testing():
    print('This is my Smoke main page test case code...')
    print('Test case is finished...')
    assert actual_result == False

@pytest.mark.Sanity
def test_tc_002_Go_to_main_page_testing():
    print('This is my Sanity test case code...')
    print('Test case is finished...')
    assert actual_result == True
