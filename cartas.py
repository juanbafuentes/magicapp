import requests

def carta(id):

    url = f'https://api.magicthegathering.io/v1/cards/?number=333'
    
    requests.post(url)
    response = requests.post(url)

    return response