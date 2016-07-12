''' It still can't create a folder to keep the html files.
    line 29: in getUrls,  hrf = lnk in href follows error
    TypeError: argument of type 'NoneType' is not iterable'''

import requests, os, re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def getUrls(name, url):
    
    res = requests.get(url)
    
    # Catching Exceptions
    try:
        res.raise_for_status()
    except Exception as e:
        print('Problem: %s'%(e))
    
    # Saving file in the hard-drive
    try:
        file = open(name+'.html','wb')
        for chunk in res.iter_content(10000):
            file.write(chunk)
        file.close()
    except Exception:
        print()
    
    # Parsing and getting urls from the page
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        hrf = lnk in href
        upar = urlparse(href)
        if not href in [None, lnk] and not 'login' in href and (re.search(r'(http(s?):|www.|mailto:)?',href)==None or hrf == True):
            if hrf:
                url = href
                href = upar.path[1:]
                if href.endswith('/'): href = href[:-1]
            else:
                if href.startswith('/'): url = url + href[1:]
                else: url = url + href
            if not url in urls:
                urls.append(url)
                getUrls(href, url)
            
# Calling the function to get urls from a web page to download content in it
urls = list()
lnk = 'https://automatetheboringstuff.com/'
urls.append(lnk)
getUrls('index', lnk)
