import requests
import json

url = 'https://www.breakingbadapi.com/api/deaths'

my_req = requests.get(url=url)

res = json.loads(my_req.text)

max_value = 0

# TODO, предлагаю упростить выборку словаря с максимальным количеством смертей.
#  Стоит передать список словарей deaths в функцию max, если в параметр key функции передать lambda функцию,
#  То, сможет найти словарь с максимальным значением по интересующему нас ключу в одну строку кода.
#  Обратите внимание, id Эпизода необходимо взять по этой ссылке https://www.breakingbadapi.com/api/episodes =)


for i in res:
    if i['number_of_deaths'] > max_value:
        max_value = i['number_of_deaths']

for i in res:
    if i['number_of_deaths'] == max_value:
        print(json.dumps(i, indent=4))
# print (json.dumps(res,indent=4))
