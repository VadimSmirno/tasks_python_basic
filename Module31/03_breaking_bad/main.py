import requests
import json

url = 'https://www.breakingbadapi.com/api/deaths'
url_episodes = 'https://www.breakingbadapi.com/api/episodes'

my_req = requests.get(url=url)
res = json.loads(my_req.text)

req_episodes = requests.get('https://www.breakingbadapi.com/api/episodes')
res_episodes = json.loads(req_episodes.text)
# print (json.dumps(res_episodes,indent=4))

for i_dict in res_episodes:
    if i_dict["season"] == '2' and i_dict["episode"] == '13':
        result = {"episode_id": i_dict["episode_id"]}
        with open('Breaking_Bad.json', 'w') as file:
           json.dump(result,file,indent=4)
        print("episode_id: ", i_dict["episode_id"])

dict_max_value = max(res, key=lambda x: x['number_of_deaths'])
dict = {
"season: ": dict_max_value["season"],
"episode: ": dict_max_value["episode"],
"number_of_deaths: ": dict_max_value["number_of_deaths"]
}

print(dict)

with open('Breaking_Bad.json', 'a') as file:
    json.dump(dict,file,indent=4)
