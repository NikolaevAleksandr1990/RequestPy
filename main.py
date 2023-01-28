import requests


def hulk_intelligence():
    url = 'https://akabab.github.io/superhero-api/api/powerstats/332.json'
    response = requests.get(url=url)
    x = response.json()
    return x['intelligence']


def captain_intelligence():
    url = 'https://akabab.github.io/superhero-api/api/powerstats/149.json'
    response = requests.get(url=url)
    x = response.json()
    return x['intelligence']


def thanos_intelligence():
    url = 'https://akabab.github.io/superhero-api/api/powerstats/665.json'
    response = requests.get(url=url)
    x = response.json()
    return x['intelligence']


def most_intelligences():
    hero = {'Hulk': hulk_intelligence(), 'Captain America': captain_intelligence(), 'Thanos': thanos_intelligence()}
    i = 0
    name = str
    for names, intelleg in hero.items():
        if intelleg > i:
            i = intelleg
            name = names
    print(name)


if __name__ == '__main__':
    most_intelligences()
