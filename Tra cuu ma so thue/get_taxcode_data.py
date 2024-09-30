import  requests

import requests

response = requests.get('http://127.0.0.1:5011/get-taxcode')
taxcodedata = response.json()
data = taxcodedata.get('taxcode', '')

print(data)