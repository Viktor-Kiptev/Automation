import requests, json, jsonpath, pytest


def test_add_new_student():
    app_url = 'https://reqres.in/api/users'
    # app_url = 'https://thetestingworldapi.com/api/Students'
    json_file = open('C:/Users/Vikto/PycharmProjects/PytestLearning/Test_cases/student_data.json', 'r')
    request_json = json.loads(json_file.read())
    response = requests.post(app_url, request_json)
    print(response.text)
    print(response.status_code)
    # id = jsonpath.jsonpath(response.json(), 'id')
    # print(id[0])
    assert response.status_code == 201

    # app_url = 'https://reqres.in/api/users/2'
    # json_file = open('C:/Users/Vikto/PycharmProjects/PytestLearning/Test_cases/new_user_data.json', 'r')
    # request_json = json.loads(json_file.read())
    # response = requests.post(app_url, request_json)
    # print(response.text)
    # print(response.status_code)
    # # id = jsonpath.jsonpath(response.json(), 'id')
    # # print(id[0])
    # assert response.status_code == 201
