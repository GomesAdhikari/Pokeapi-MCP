import requests

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Structure the data nicely
        pokemon_info = {
            "name": data["name"],
            "id": data["id"],
            "base_experience": data.get("base_experience"),
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"]],
            "stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]},
            "sprites": {
                "front_default": data["sprites"]["front_default"],
                "back_default": data["sprites"]["back_default"]
            }
        }
        print("Data retrieved successfully.")
        return pokemon_info
    else:
        print(f"Failed to retrieve data: Status code {response.status_code}")
        return None

pokemon_name = "bulbasaur"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Base Experience: {pokemon_info['base_experience']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
    print(f"Types: {', '.join(pokemon_info['types'])}")
    print(f"Abilities: {', '.join(pokemon_info['abilities'])}")
    print("Stats:")
    for stat_name, stat_value in pokemon_info["stats"].items():
        print(f"  {stat_name}: {stat_value}")
    print("Sprites URLs:")
    print(f"  Front: {pokemon_info['sprites']['front_default']}")
    print(f"  Back: {pokemon_info['sprites']['back_default']}")
