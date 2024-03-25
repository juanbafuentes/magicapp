import requests
import json

def carta(id) -> str:

    url = "https://api.magicthegathering.io/v1/cards?number={id}"
    response = requests.get(url)

    if response.status_code == 200:
        # La solicitud fue exitosa
        datos = response.json()
        with open("resultado.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)
    else:
        # La solicitud falló
        print("Error:", response.status_code)

    # # Obtiene el nombre del primer resultado.
    name = datos["cards"][0]["foreignNames"][1]["name"]
    manacost = datos["cards"][0]["manaCost"]
    type = datos["cards"][0]["foreignNames"][1]["type"]
    rarity = datos["cards"][0]["rarity"]
    foreignNames = datos["cards"][0]["foreignNames"][1]["text"]
    imageURL = datos["cards"][0]["foreignNames"][1]["imageUrl"]


    print(f"""Nombre: {name}
        Coste: {manacost}
        Tipo: {type}
        Rareza: {rarity}
        Descripción: {foreignNames}
        Imagen: {imageURL}
    """)

