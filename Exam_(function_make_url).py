from bs4 import BeautifulSoup
import requests
import urls


def request_url(site, uri):
    res = requests.get(site)

    soup = BeautifulSoup(res.text, 'html.parser')
    uri = uri
    url = soup.select_one(uri)
    if url == None : 
        return ("none")
    else :
        result = url.get('src')
      
        iframe = urls.urljoin(urls.getHostname(site, True), result)
        return iframe
