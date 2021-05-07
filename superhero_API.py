# Кто самый умный супергерой?
# Есть API по информации о супергероях.
# Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
# Для определения id нужно использовать метод /search/name
#
# Токен, который нужно использовать для доступа к API: 2619421814940190.
# Таким образом, все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/

import requests

url = "https://superheroapi.com/api/2619421814940190/"

def search_by_name(name):
    response = requests.get(url + 'search/' + name)
    return response.json()


def get_intelligence_param(info):
    response = requests.get(url + info['results'][0]['id'] + '/powerstats')
    return {'name': response.json()['name'], 'intelligence': response.json()['intelligence']}


def compare_intelligence(dict1, dict2, dict3):
    summary_hero_list = [dict1, dict2, dict3]
    sorted_hero_list = sorted(summary_hero_list, key=lambda k: k['intelligence'])
    return sorted_hero_list[0]['name']


hulk_info = search_by_name('Hulk')
captain_America_info = search_by_name('Captain America')
Thanos_info = search_by_name('Thanos')

# print(hulk_info)
# print(captain_America_info)
# print(Thanos_info)

hulk = get_intelligence_param(hulk_info)
captain_America = get_intelligence_param(captain_America_info)
thanos = get_intelligence_param(Thanos_info)

# print(hulk)
# print(captain_America)
# print(thanos)

super_smart_hero = compare_intelligence(hulk, captain_America, thanos)
print(super_smart_hero)