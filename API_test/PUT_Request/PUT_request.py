import requests, json, jsonpath

# API url (response 200)
url = "https://reqres.in/api/users/2"


# Read input Json file
file = open('test_json_put.json', 'r')
json_input = file.read()
requests_json = json.loads(json_input)
# print(requests_json)

# Make PUT request with json input body
respone = requests.put(url, requests_json)
print(respone.content)

# Validation response code
assert respone.status_code == 200

# Parse response content
respone_json = json.loads(respone.text)
updated_at = jsonpath.jsonpath(respone_json, 'updatedAt')
print(updated_at[0])
