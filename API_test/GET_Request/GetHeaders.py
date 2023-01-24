import requests
header_data = {'T1':'Viktor', 'T2':'AQA'}
response = requests.get('http://httpbin.org/get', headers = header_data)
print(response.text)