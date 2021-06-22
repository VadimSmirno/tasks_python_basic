import requests
import json

url = 'https://www.breakingbadapi.com/api/deaths'

my_req = requests.get(url=url)

res = json.loads(my_req.text)

max_value = 0

for i in res:
    if i['number_of_deaths'] > max_value:
        max_value = i['number_of_deaths']

for i in res:
    if i['number_of_deaths'] == max_value:
        print (json.dumps(i,indent=4))
# print (json.dumps(res,indent=4))