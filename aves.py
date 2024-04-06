import requests
import json
from html_maker import listado_aves
from html_maker import cuerpo_html

def request_get(url):
    return json.loads(requests.get(url).text)

aves = request_get('https://aves.ninjas.cl/api/birds')
# print(aves)

listado = listado_aves(aves)

html_template = cuerpo_html(listado)

def crear_html():
    with open('index.html', 'w', encoding = 'utf-8') as f:
        return f.write(html_template)
crear_html()

