import requests
import zlib
import json
import logging

g=[]
def aea2(url):
    try:
        logging.captureWarnings(True)
        proxies = {'http': None, 'https': None}
        aa = requests.get(url, proxies=proxies, verify=False, timeout=(6, 15))
        cd3 = url.replace('http://', '').replace('https://', '').replace('/', '')
        a3 = cd3
        de = ['https', 'http']
        for i in de:
            def ap():
                try:
                    for cai in range(1):
                        url1 = i + '://' + a3 + '/'
                        response = requests.get(url1)
                        whatweb_dict = {"url": response.url, "text": response.text, "headers": dict(response.headers)}
                        whatweb_dict = json.dumps(whatweb_dict)
                        whatweb_dict = whatweb_dict.encode()
                        whatweb_dict = zlib.compress(whatweb_dict)
                        data = {"info": whatweb_dict}
                        c = requests.post("http://whatweb.bugscaner.com/api.go", files=data)
                        d1 = c.json()
                        return d1
                except:
                    pass
            try:
                for ke, values in ap().items():
                    cg = ke, values
                    g.append(cg)
                if len(ap()) != 0:
                    break
            except:
                pass
    except:
        pass
def sca2():
    return g
def qca2():
    g.clear()