import requests, jsonpath, json

# API url
url = 'https://reqres.in/api/users?page=2'

# Send GET request
response = requests.get(url)

# Display response content
# print(response.content)
# print(response.headers)


# Validate status code

# assert response.status_code == 200

# Fetch specific response header content
# print(response.headers.get('Date'))
# print(response.headers.get('Server'))

# Fetch cookies
# print(response.cookies)

# Fetch Encoding
# print(response.encoding)

# Fetch Elapse time
# print(response.elapsed)

# Validate specific value from response

json_response = json.loads(response.text)
# print(json_response)

# Fatch value using Json Path
# pages = jsonpath.jsonpath(json_response, 'total_pages')
# data = jsonpath.jsonpath(json_response, 'data')
# print(pages[0])
# first_user = dict(data[0][0])
# print(first_user.get('first_name'))
# print(data[0][0])
# assert pages[0] == 2
#
# test_data_dict = {'id': 7, 'email': 'michael.lawson@reqres.in', 'first_name': 'Michael', 'last_name': 'Lawson', 'avatar': 'https://reqres.in/img/faces/7-image.jpg'}
# assert data[0][0] == test_data_dict
# first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
# print(first_name)
#
# for i in range(0,3):
#     first_name = jsonpath.jsonpath(json_response, f'data[{i}].first_name')
#     print(first_name)

