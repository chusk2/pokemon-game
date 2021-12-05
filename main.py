# <span class="mini">Bulbasaur</span>
from bs4 import BeautifulSoup as bs
import csv
import requests
import time


# define a timing decorator
def howlong(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Elapsed time: {end-start:.2f} seconds.')
    return wrapper
    

#@howlong
def get_pokemons():
    pokemon_list = []

    nums = [i for i in range(1, 10)]
    url='https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/' \
        'pkmn&pk='
    for number in nums:
        html = requests.get(f'{url}{number}#rby')
        html.status_code == requests.codes.ok
        soup = bs(html.text, 'html.parser')
        pokemon_name = soup.select('.mini')[0].getText()
        img_tags = soup.find_all("img")
        types = []
        for img in img_tags:
            if 'tipos' in img['src']:
                tipo = img['alt']
                if tipo not in types:
                    types.append(tipo)
        poke_dict = {}
        poke_dict['name'] = pokemon_name
        poke_dict['types'] = types
        pokemon_list.append(poke_dict)
        # evolutions
        row_evolution = soup.find(text='Linea Evolutiva')
        # ataques
        # https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/ \
        # 'movimientos_nivel&pk=1#rby'
        pokemon = {
        'name' : 'name', 'level' : 1,
        'attacks' :
            [
                {'attack_name' : '',
                'damage' : 10,
                'attack_type' : '',
                'minimum_level' : 1
                },
            ],
        'health' : 100}

    return pokemon_list
    # with open('pokedex.csv', 'w') as file:
    #     writer = csv.writer(file)
    #     # csv writer expects each row to be a list
    #     # if just i is given as writerow argument
    #     # writerow will decompose string in a list of chars:
    #     # ['B', 'u', 'l', 'b', 'a', 's', 'a', 'u', 'r']
    #     for i in poke_list:
    #         writer.writerow([i])

pokemons = get_pokemons()
for item in pokemons:
    # use plurar in case needed
    if len(item['types']) > 1:
        tipo_suffix ='s'
    else:
        tipo_suffix =''
    
    print(f"Nombre: {item['name']}. Tipo{tipo_suffix}:", end=' ')
    print(*item['types'], sep=',')
    
# with open('pokedex.csv', 'r') as f:
#     content = csv.reader(f)
#     for item in content:
#         print(item[0])#
