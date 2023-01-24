import json

some_dic = '{'k1' : 'val1', 'k2' : 'val2'}'

json_result = json.load(some_dic)

print(json_result('k1'))