import requests
param = {'name':'Viktor', 'email':'AQA@hotmail.com'}
response = requests.get('http://httpbin.org/get', params = param)
print(response.text)