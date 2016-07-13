import requests, os, re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def getUrls(name, url):
    
    req = requests.get(url)
    
    # Checking the request status of the url
    try:
        req.raise_for_status()
    except Exception as e:
        print('Problem: %s'%(e))

    #Parsing the name/ href to make a folder if needed
    namepar = name.split('/')
    filename = namepar[-1]+'.html'
    
    # Saving html files in the hard-drive
    try:
        file = open(filename,'wb')
        for chunk in req.iter_content(10000):
            file.write(chunk)
        file.close()
        filepath = '.\\'+'\\'.join(namepar[:-1])
        if not os.path.exists(filepath):
            os.path.makedirs(filepath)
        os.rename(filename,filepath+'\\'+filename)
    except Exception:
        print('Let it go!')
    
    # Parsing and getting urls from the page
    soup = BeautifulSoup(req.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        try:
            hrf = lnk in href
        except TypeError:
            hrf = False
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
