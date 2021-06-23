import requests
import json

url = 'https://www.breakingbadapi.com/api/deaths'
url_episodes = 'https://www.breakingbadapi.com/api/episodes'

my_req = requests.get(url=url)
res = json.loads(my_req.text)

req_episodes = requests.get('https://www.breakingbadapi.com/api/episodes')
res_episodes = json.loads(req_episodes.text)
# print (json.dumps(res_episodes,indent=4))

dict_max_value = max(res, key=lambda x: x['number_of_deaths'])
print(json.dumps(dict_max_value, indent=4))

for i_dict in res_episodes:
    if i_dict["season"] == '2' and i_dict["episode"] == '13':
        print("episode_id: ", i_dict["episode_id"])

# TODO, после того, как данные собраны, необходимо сохранить их в файл формата json.
#  Пожалуйста, обратите внимание на условие задания. в нём указано, какие ключи должны присутствовать в словаре =)
