import requests

# API url (response 204)
url = "https://reqres.in/api/users/2"

respone = requests.delete(url)
# print(respone)

#  Fetch response code
print(respone.status_code)

assert respone.status_code == 204