import urllib.parse as parse
import os.path as path

def getFileName(url) :
    p = parse.urlparse(url).path
    return path.basename(p)

def getHostname(url, withProtocol = False):
    p = parse.urlparse(url)
    if withProtocol:
        return "{}://{}".format(p.scheme, p.hostname)
    else:
        return p.hostname

def urljoin(url, p):
<<<<<<< HEAD
    return parse.urljoin(url, p)
=======
    return parse.urljoin(url, p)
>>>>>>> 83ce84027e56df72f4809163d0e39cf8904faa07
