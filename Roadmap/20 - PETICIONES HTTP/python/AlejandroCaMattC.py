import requests

"""HTTP Request with Python"""

response = requests.get('https://google.com')
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")

"""Exercise"""

# From the PokéAPI (https://pokeapi.co), build a program that you can:
# get specific information about a Pokémon (e.g., name, type, abilities).
# Show the name, id, weight, height, and types of the Pokémon.

pokemon = input("Enter the name of number of the Pokémon: ").lower()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
if response.status_code == 200:
    data = response.json()
    name = data['name']
    id = data['id']
    weight = data['weight']
    height = data['height']
    types = [t['type']['name'] for t in data['types']]

    print(f"Name: {name}")
    print(f"ID: {id}")
    print(f"Weight: {weight}")
    print(f"Height: {height}")
    print(f"Types: {', '.join(types)}")
else:
    print(f"Error: {response.status_code} pokémon not found")

# get the evolution chain of a Pokémon (e.g., Bulbasaur -> Ivysaur -> Venusaur).
response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}")
if response.status_code == 200:
    data = response.json()
    evolution_chain_url = data['evolution_chain']['url']
    evolution_response = requests.get(evolution_chain_url)
    if evolution_response.status_code == 200:
        evolution_data = evolution_response.json()
        chain = evolution_data['chain']
        evolutions = []
        while chain:
            evolutions.append(chain['species']['name'])
            if chain['evolves_to']:
                chain = chain['evolves_to'][0]  # Take the first evolution in the chain
            else:
                chain = None
        print("Evolution Chain: " + " -> ".join(evolutions))
    else:
        print(f"Error: {evolution_response.status_code} evolution chain not found")
