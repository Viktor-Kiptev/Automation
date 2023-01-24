import requests, json, jsonpath, openpyxl

def test_add_multipl_students():
    api_url = 'https://reqres.in/api/users'
    my_file = open('C:/Users/Vikto/PycharmProjects/PytestLearning/Data_Driving_testing/new_student_data.json', 'r')
    my_json = json.loads(my_file.read())
    my_xl_file = openpyxl.load_workbook("C:/Users/Vikto/PycharmProjects/PytestLearning/Data_Driving_testing/test_data.xlsx")
    sh = my_xl_file['Лист1']
    num_rov = sh.max_row
    for i in range(2, num_rov + 1):
        cell_name = sh.cell(i, 1)
        cell_job = sh.cell(i, 2)
        my_json['name'] = cell_name.value
        my_json['job'] = cell_job.value
        response = requests.post(api_url, my_json)
        print(response.text)
        print(response.status_code)
        assert response.status_code == 201