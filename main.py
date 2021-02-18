# libraries
import requests
from bs4 import BeautifulSoup
import json

def init():
    r = requests.get('https://alert-train.surge.sh/')
    data = r.content.decode('utf-8', errors="replace")
    soup = BeautifulSoup(data, 'lxml')

    contentFind = soup.find_all('li', class_="estilo-publico")

    content = []
    for child in contentFind:
        link = child.a.get('href')
        title = child.h2.span.text
        description = child.p.span.text
        content.append({
            "link": link,
            "title": title,
            "description": description
        })

    print(json.dumps(content, indent=2))

init()
