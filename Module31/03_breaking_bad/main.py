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
season = dict_max_value['season']
episode = dict_max_value['episode']

dct = {
    "season: ": dict_max_value["season"],
    "episode: ": dict_max_value["episode"],
    "number_of_deaths: ": dict_max_value["number_of_deaths"]
}

for i_dict in res_episodes:
    if i_dict["season"] == str(season) and i_dict["episode"] == str(episode):
        result = {
            "episode_id": i_dict["episode_id"]
        }
        dct.update(result)
        break

print(dct)
with open('Breaking_Bad.json', 'w') as file:
    json.dump(dct, file, indent=4)

# зачёт!
