import requests
response1 = requests.get('https://akabab.github.io/superhero-api/api/all.json')
names_list = ['Hulk', 'Captain America', 'Thanos']
max_int = 0
name = ''
for item in response1.json():
    if item['name'] in names_list:
        if item['powerstats']['intelligence'] > max_int:
            max_int = item['powerstats']['intelligence']
            name = item['name']
print(f'{name} is clever!!!')
