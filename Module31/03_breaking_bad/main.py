import requests
import json

url = 'https://www.breakingbadapi.com/api/deaths'
url_episodes = 'https://www.breakingbadapi.com/api/episodes'

my_req = requests.get(url=url)
res = json.loads(my_req.text)

req_episodes = requests.get('https://www.breakingbadapi.com/api/episodes')
res_episodes = json.loads(req_episodes.text)
# print (json.dumps(res_episodes,indent=4))

# TODO, было бы правильней, сначала получить словарь с максимальным количеством смертей из res
#  Далее, создать 2 переменные для текстовых значения по ключам season и episode словаря res
#  И в цикле ниже искать нужный словарь при помощи этих переменных.
#  Когда словарь найден, нам необходимо создать переменную для хранения Id эпизода и выйти из цикла

for i_dict in res_episodes:
    if i_dict["season"] == '2' and i_dict["episode"] == '13':
        result = {"episode_id": i_dict["episode_id"]}
        # TODO, запись в файл в этом месте лишняя.
        #  Предлагаю записать 1 раз весь словарь целиком, после добавления ключа episode_id в наш словарь с данными.
        with open('Breaking_Bad.json', 'w') as file:
           json.dump(result,file,indent=4)
        print("episode_id: ", i_dict["episode_id"])

dict_max_value = max(res, key=lambda x: x['number_of_deaths'])

# TODO, стоит создать переменную с именем, отличным от dict, иначе, после этой строки, словарь при помощи dict() не создать =)
dict = {
"season: ": dict_max_value["season"],
"episode: ": dict_max_value["episode"],
"number_of_deaths: ": dict_max_value["number_of_deaths"]
}


print(dict)

with open('Breaking_Bad.json', 'a') as file:
    json.dump(dict,file,indent=4)
