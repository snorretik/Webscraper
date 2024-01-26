import sys
import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

urlStart = "https://www.startpagina.nl"

# Main functionality ----------------------------------

def get_links_from_url(currentURL):
    retrievedURLs = []

    try:
        r = requests.get(currentURL)
        soup = BeautifulSoup(r.text, 'html.parser')
    
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(currentURL, path)
            retrievedURLs.append(path)      
    except requests.exceptions.ConnectionError:
        print("connection refused")
        retrievedURLs.append(currentURL)
    
    return retrievedURLs

def pre_analysis(urlString):
    schema = urlparse(urlString).scheme
    tweedeDeel = urlparse(urlString).netloc

    if (tweedeDeel == "www.startpagina.nl"):
        return True
    else: 
        return False

def get_robotstxt_file(urlString):
    schema = urlparse(urlString).scheme
    tweedeDeel = urlparse(urlString).netloc

    locationRobotsFile = str(schema + "://" + tweedeDeel + "/robots.txt")
    r = requests.get(locationRobotsFile)
    
    return r.text


# Using file reading and writing ------------------

def read_from_file(nameFile):
    with open(nameFile, 'r') as fileIn:
        textFileInput = fileIn.readlines()
        return textFileInput

def write_to_file(listOfStrings, nameFile):
    with open(nameFile, 'a') as fileOut:
        for singleString in listOfStrings:
            if (singleString):
                fileOut.writelines(str(singleString + "\n"))
            else:
                fileOut.writelines("empty\n")


# Defining the loops with which to call ------------

def startInitialLoop():
    result = get_links_from_url(urlStart)
    write_to_file(result, 'output.txt')

def furtherLoop():
    inputList = read_from_file('output.txt')
    result2 = set()

    for currentURL in inputList:
        print(currentURL)
        # time.sleep(1)
        if (pre_analysis(currentURL)):
            # result2 = get_robotstxt_file(currentURL)
            listLinks = get_links_from_url(currentURL)
            
            for linkSingle in listLinks:
                result2.add(linkSingle)
        else:
            result2.add(currentURL)

    write_to_file(result2, 'output2.txt')

furtherLoop()