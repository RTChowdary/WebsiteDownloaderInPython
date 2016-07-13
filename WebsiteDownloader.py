
import requests, os, re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def getUrls(name, url):
    
    req = requests.get(url)
    
    # Catching Exceptions
    try:
        req.raise_for_status()
    except Exception as e:
        print('Problem: %s'%(e))

    namepar = name.split('/')
    if not namepar[-1].endswith('.html'):
        filename = namepar[-1]+'.html'
    
    # Saving file in the hard-drive
    try:
        file = open(filename,'wb')
        for chunk in req.iter_content(10000):
            file.write(chunk)
        file.close()
        filepath = '.\\'+'\\'.join(namepar[:-1])

        # Creating the path for folders and files
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
        if href != None:
            hrf = lnk in href
        else:
            hrf = False
        upar = urlparse(href)
        if not href in [None, lnk] and not 'login' in href and (re.search(r'(http(s?):|www.|mailto:)?',href)==None or hrf == True):
            if hrf:
                url = href
                href = upar.path[1:]
                if href.endswith('/'): href = href[:-1]
                print('True')
            else:
                if href.startswith('/'): url = url + href[1:]
                else: url = url + href
                print('False')
            if not url in urls and not href.find('.pdf'or'.epub'or'.docx')!=-1:
                urls.append(url)
                getUrls(href, url)
        print(url)
            
# Calling the function to get urls from a web page to download content in it
urls = list()
lnk = 'http://eloquentjavascript.net/'
urls.append(lnk)
getUrls('index', lnk)
