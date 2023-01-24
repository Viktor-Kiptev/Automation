import requests, json, jsonpath

# API url (response 201)
url = "https://reqres.in/api/users"

# Read input Json file
file = open('test_json.json', 'r')
json_input = file.read()
requests_json = json.loads(json_input)
# print(requests_json)

# Make POST request with json input body
respone = requests.post(url, requests_json)
print(respone.content)

# Validation response code
assert respone.status_code == 201

# Fetch Header from response
print(respone.headers.get('Content-Length'))

# Fetch response to Json format
respone_json = json.loads(respone.text)

# Pick id using Json path
id = jsonpath.jsonpath(respone_json, 'id')
print(id[0])
