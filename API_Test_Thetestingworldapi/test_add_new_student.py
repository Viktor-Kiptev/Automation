import requests, json, jsonpath


def test_Add_student_address():
    api_url = 'https://reqres.in/api/addresses'
    student_data = open('C:/Users/Vikto/PycharmProjects/PytestLearning/API_Test_Thetestingworldapi/request_create_new_addres.json', 'r')
    json_request = json.loads(student_data.read())
    response = requests.post(api_url, json_request)
    print(response.text)
    assert response.status_code == 201

def test_Get_student_details_by_id():
    api_url = f'https://reqres.in/api/studentsDetails/10'
    response = requests.get(api_url)
    json_response = response.json() # or json.loads(response.text)
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(response.text)
    assert id[0] == 10

def test_PUT_update_my_address_by_id():
    api_url = 'https://reqres.in/api/addresses/10'
    student_data = open('C:/Users/Vikto/PycharmProjects/PytestLearning/API_Test_Thetestingworldapi/request_update_addres.json', 'r')
    json_request = json.loads(student_data.read())
    response = requests.put(api_url, json_request)
    print(response.text)
    assert response.status_code == 200

def test_DELETE_address():
    api_url = 'https://reqres.in/api/studentsDetails/1'
    response = requests.delete(api_url)
    print(response.text)
    assert response.status_code == 204

