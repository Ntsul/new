import requests
import json

BASE_URL = "https://rickandmortyapi.com/api/character"

character_episodes = {}

while BASE_URL:
    response = requests.get(BASE_URL)
    data = response.json()
    characters = data['results']

    for character in characters:
        character_name = character['name']
        episode_urls = character['episode']
        episode_names = []

        for url in episode_urls:
            episode_data = requests.get(url).json()
            episode_names.append(episode_data['name'])

        character_episodes[character_name] = episode_names

    BASE_URL = data['info']['next']

with open('character_episodes_version1.json', 'w', encoding='utf-8') as file:
    json.dump(character_episodes, file, ensure_ascii=False, indent=4)

print("DataSavedTo character_episodes_version1.json")

