import requests

def fetch_data(url):
    """Helper function to fetch data from a URL and return JSON."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - Unable to fetch data from {url}")
        return None

def get_pokemon_info(pokemon):
    """Fetch and display basic information about a Pokémon."""
    data = fetch_data(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    if data:
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

def get_evolution_chain(pokemon):
    """Fetch and display the evolution chain of a Pokémon."""
    species_data = fetch_data(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}")
    if species_data:
        evolution_chain_url = species_data['evolution_chain']['url']
        evolution_data = fetch_data(evolution_chain_url)
        if evolution_data:
            chain = evolution_data['chain']
            evolutions = []
            while chain:
                evolutions.append(chain['species']['name'])
                chain = chain['evolves_to'][0] if chain['evolves_to'] else None
            print("Evolution Chain: " + " -> ".join(evolutions))

def get_pokemon_games(pokemon):
    """Fetch and display the video games in which a Pokémon has appeared."""
    data = fetch_data(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    if data:
        games = {game['version']['name'] for game in data['game_indices']}
        print("Games: " + ", ".join(games))

if __name__ == "__main__":
    pokemon = input("Enter the name or number of the Pokémon: ").lower()
    get_pokemon_info(pokemon)
    get_evolution_chain(pokemon)
    get_pokemon_games(pokemon)

