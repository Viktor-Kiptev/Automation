import requests
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.post('https://api.github.com/user', auth=HTTPBasicAuth("Viktor-Kiptev", "Edge415263"))
    print(response.text)
    print(response.status_code)

