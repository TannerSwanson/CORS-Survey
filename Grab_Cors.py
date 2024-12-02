import requests
from bs4 import BeautifulSoup
import csv
import json
import pandas as pd
import matplotlib.pyplot as plt

def find_api_urls(webpage_url):
    """Get HTML page, scrape all URLs from the given webpage."""
    try:
        response = requests.get(webpage_url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # scans all script and a href lines, adds their value to api_urls set
        api_urls = set()
        for script in soup.find_all('script'):
            if script.get('src'):
                api_urls.add(script['src'])
        for link in soup.find_all('a', href=True):
            api_urls.add(link['href'])
        return api_urls
    except requests.exceptions.RequestException as e:
        print("error")
        return set()  # Return an empty set on error

def check_cors_headers(url):
    """Runs preflight to get CORS headers for the given URL. Writes relevant CORS headers to JSON"""
    try:
        response = requests.options(url) # Preflight request to get CORS headers
        cors_info = {
            "url": url,
            "allowed_origins": response.headers.get('Access-Control-Allow-Origin'),
            "allowed_methods": response.headers.get('Access-Control-Allow-Methods'),
            "allowed_headers": response.headers.get('Access-Control-Allow-Headers'),
            "request_methods": response.headers.get('Access-Control-Request-Methods'),
            "request_headers": response.headers.get('Access-Control-Request-Headers')
        }
        return cors_info
    except requests.exceptions.RequestException as e:
        return None

def run(webpage):
    # Step 1: Find API URLs
    api_urls = find_api_urls(webpage)
    if not api_urls:
        return []
    # Step 2: Check CORS headers for each API URL found
    result = []

    for url in api_urls:
        try:
            if (url != None):
                data = check_cors_headers(url)
                if (data):
                    print(data)
                    result.append(data)
        except:
            continue
    return result

if __name__ == "__main__":
    result = []
    with open('ListOfSites.txt', mode='r') as file:
        listOfVals = file.readlines()
        for f in listOfVals:
            print(f)
            result.append(run(f[0:len(f)-1])) # [0:len(f)-1] somehow fixed it including the \n
    with open('Cors_Data.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)
