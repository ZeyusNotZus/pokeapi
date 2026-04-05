import asyncio
import json
from pyscript import document
from pyscript.fetch import fetch

url = "https://pokeapi.co/api/v2/"

app = document.querySelector("#app")

search_input = document.createElement("input")
search_input.type = "text"
search_input.placeholder = "Search for a Pokemon"

search_button = document.createElement("button")
search_button.innerText = "Search!"

display = document.createElement("pre")


app.append(search_input)
app.append(search_button)
app.append(display)

async def search_pokemon(ev):
    pokemon_name = search_input.value.lower()
    response = await fetch(f"{url}pokemon/{pokemon_name}")

    if not pokemon_name:
        display.innerText = "Please enter a Pokemon name!"
        return
        
    if response.ok:
        data = await response.json()

        filtered_data = {
            "name": data["name"],
            "types": [t["type"]["name"] for t in data["types"]],
            "height": data["height"],
            "weight": data["weight"],

        }

        display.innerText = json.dumps(filtered_data, indent=4)

    else:
        display.innerText = "Pokemon not found!"

search_button.onclick = lambda ev: asyncio.ensure_future(search_pokemon(ev))