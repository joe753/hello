from bs4 import BeautifulSoup
import requests
import urls


def request_url(site, uri):
    res = requests.get(site)
    soup = BeautifulSoup(res.text, 'html.parser')
    uri = uri
    url = soup.select_one(uri)
    result = url.get('src')
    # print (r
    # esult)
    # print(urls.getHostname(site, True))
    iframe = urls.urljoin(urls.getHostname(site, True), result)
    # print (iframe)
    print (iframe)
    return iframe
    # return (iframe)