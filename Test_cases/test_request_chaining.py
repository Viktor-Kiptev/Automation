import requests, json, jsonpath, pytest

def test_add_new_student():
    global user_id
    api_url = 'https://thetestingworldapi.com/api/studentsDetails'
    json_file = open('C:/Users/Vikto/PycharmProjects/PytestLearning/Test_cases/add_new_student_data.json', 'r')
    json_request = json.loads(json_file.read())
    response = requests.post(api_url, json_request)
    user_id = jsonpath.jsonpath(response.json(), 'id')
    print(user_id[0])

def test_get_details():
    api_url = f'https://thetestingworldapi.com/api/studentsDetails/{user_id}'
    response = requests.get(api_url)
    print(response.text)

