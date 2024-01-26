import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

urlStart = ["https://www.startpagina.nl"]
urlsVisited = set()

def get_all_links(urlsInside):
    
    urlsCollected = []
    
    for url in urlsInside:
        if ((url in urlsVisited) == False):
            try:
                print("Visiting " + url + " ...")
                r = requests.get(url)
                soup = BeautifulSoup(r.text, 'html.parser')

                for link in soup.find_all('a'):
                    path = link.get('href')
                    if path and path.startswith('/'):
                        path = urljoin(url, path)
                    urlsCollected.append(path)
                    
                urlsVisited.add(str(url))
                print("Visited succesfully: " + str(url))
            except Exception:
                print("Visited unsuccesfully: " + str(url))
                continue
        elif ((url in urlsVisited) == True):
            print("Already visited: " + str(url))
            continue
        else:
            print("error in checking urlsVisited")
    
    return urlsCollected

# def read_robots_file():


def write_to_file(arrayOfStrings):
    with open('output.txt', 'w') as f:
        f.writelines(arrayOfStrings)

def run_the_crawler(urlToStart):
    linksThusFar = get_all_links(urlToStart)
    moreLinksThanBefore = get_all_links(linksThusFar)
    if (len(urlsVisited) > 0):
        write_to_file(urlsVisited)

run_the_crawler(urlStart)