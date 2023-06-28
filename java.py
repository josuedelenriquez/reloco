# NOMBRE_DEL_DUEÑO_CODIGO: JaneDoe456
# TEMATICA_DEL_CODIGO: Web scraping con BeautifulSoup
# IEM_ESCUELA_NORMAL_PASTO: IEM Normal de Pasto
# CURSO: Programación Web

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading").text
print("Title:", title)

content = soup.find(id="mw-content-text").find(class_="mw-parser-output").p.text
print("Content:", content)
