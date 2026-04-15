# type: ignore

import asyncio
import json
from pyscript import document, web
from pyscript.fetch import fetch

url = "https://pokeapi.co/api/v2/"

app = document.getElementById("app")

style = document.createElement("style")
style.innerHTML = """
    #app {font-family: sans-serif;}
    .pokemon_box {display: flex; gap: 15px;}
    .pokemon_image {max-width: 100%; height: auto; object-fit: contain}
    .pokemon_info h1 {font-size: 30; margin: 0; font-weight: bold;}
    .pokemon_info p {font-size: 20; margin: 10px 0;}
    """

search_input = document.createElement("input")
search_input.type = "text"
search_input.placeholder = "Search for a Pokemon"

search_button = document.createElement("button")
search_button.innerText = "Search!"

display = document.createElement("div")

async def search_pokemon(ev):
    pokemon_name = search_input.value.lower()
    response = await fetch(f"{url}pokemon/{pokemon_name}")

    if not pokemon_name:
        display.innerText = "Please enter a Pokemon name!"
        return
        
    if response.ok:
        data = await response.json()    

        # Data
        name = data["name"].capitalize()
        types = " | ".join([t["type"]["name"].capitalize() for t in data["types"]])
        height = data["height"] / 10
        weight = data["weight"] / 10
        image = data["sprites"]["front_default"]

        display.innerHTML = f"""
            <div class = "pokemon_box">
                <img src = {image} class = "pokemon_image"> 
                <div class = "pokemon_info">
                    <h1>{name}</h1>
                    <code>{types}</code>
                    <p>Height: {height}m</p>
                    <p>Weight: {weight}kg</p>
                </div>
            </div>
            """

    else:
        display.innerText = "Pokemon not found!"

search_button.onclick = lambda ev: asyncio.ensure_future(search_pokemon(ev))

document.head.appendChild(style)
app.appendChild(search_input)
app.appendChild(search_button)
app.appendChild(display)
