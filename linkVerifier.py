#Web Scrapping
"""
#This program opens a web page in the browser using the webbrowser module.
import webbrowser, sys, pyperclip, requests
#webbrowser.open('http://inventwithpython.com/')

if len(sys.argv) > 1:
    #Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
"""

import requests
from bs4 import BeautifulSoup

def check_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')

    print("Checking links on:", url)

    for link in links:
        href = link.get('href')
        if href is not None and href.startswith('http'):  # Verifica si href no es None antes de llamar a startswith()
            response = requests.head(href)
            if response.status_code == 404:
                print("Broken link:", href)

# URL de ejemplo
url = input("Ingresa la URL de la página web: ")

check_links(url)