import requests, json, jsonpath, openpyxl

from Data_Driving_testing import Library



def test_add_multipl_students():
    api_url = 'https://reqres.in/api/users'
    my_file = open('C:/Users/Vikto/PycharmProjects/PytestLearning/Data_Driving_testing/new_student_data.json', 'r')
    my_json = json.loads(my_file.read())

    obj = Library.Common("C:/Users/Vikto/PycharmProjects/PytestLearning/Data_Driving_testing/test_data.xlsx", 'Лист1')
    column = obj.fetch_column_count()
    key_list = obj.fetch_key_names()
    rov = obj.fetch_rov_count()

    for i in range(2, rov + 1):
        updated_json_request = obj.update_json_with_data(i, my_json, key_list)
        response = requests.post(api_url, updated_json_request)
        print(response.text)
        print(response.status_code)
        assert response.status_code == 201