import pytest
# Test case code must be writen in method
# Method name must be started from 'test'
# Print statement output display on console -s
# Verbose mode - display test case name with status -v
# Run just selected test cases -k 'Name of test case' may be part of name
# Run just selected test cases by Tag -m 'Some tag' or use 'not Tag' to skip also work with 'or', 'and'

a = 100
actual_result = True

@pytest.fixture(scope='module')
def fixture_code():
    print('__________Some preconditions that execute BEFORE ALL run test module___________')
    yield
    print("___Some code that executed AFTER the finish run ALL tests___")


@pytest.fixture()
def fixture_code():
    print('__________Some preconditions that execute before run test___________')
    yield
    print("___Some code that executed after run test___")

# @pytest.mark.skip("Skipping as this functionalyty doesn't finihed")
def test_tc_001_Login_Logout_testing(fixture_code):
    print('This is my test case code...')
    print('Test case is finished...')
    assert actual_result == True, "Not match"

# @pytest.mark.skipif(a > 90, reason='User die')
def test_tc_002_Login_Logout_invalid_login(fixture_code):
    print('This is my test case code...')
    print('Test case is unsuccessful with incorrect login...')
    assert actual_result == False

def test_tc_003_Login_Logout_invalid_password():
    print('This is my test case code...')
    print('Test case is finished unsuccessful with wrong password...')
    assert actual_result == True

def test_tc_004_Login_Logout_invalid_login_and_password():
    print('This is my test case code...')
    print('Test case is finished unsuccessful with wrong password...')
    assert actual_result == False