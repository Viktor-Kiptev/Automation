import requests, json, jsonpath

def test_oAuth_api():
    token_url = 'https://thetestingworldapi.com/Token'
    data = {'grand+type' : 'password', 'username' : 'admin', 'pasword' : '********'}
    response = requests.post(token_url, data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')
    auth = {'Authorization' : f'Bearer {token_value}'}
    print(response.text)
    api_url = 'https://thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(api_url, headers=auth)
    print(response.text)