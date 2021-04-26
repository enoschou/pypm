#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

class WeaG:
    
    def __init__(self):
        self._url = 'https://www.cwb.gov.tw/V8/C/W/Observe/MOD/24hr/TBD.html'
        self._load()
    
    def grab(self, location):
        rtn = {}
        if location in self._sites:
            url = self._url.replace('TBD', self._sites[location])
            r = requests.get(url)
            rtn = {}
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                rtn['O'] = soup.find(headers="time").text
                rtn['T'] = float(soup.find(headers="temp").find('span').text)
                rtn['H'] = float(soup.find(headers="hum").text)/100
                rtn['R'] = float(soup.find(headers="rain").text)
            
        return rtn
    
    def _load(self):
        url = 'https://www.cwb.gov.tw/Data/js/Observe/OSM/C/STMap.json'
        j = requests.get(url)
        self._sites = {i['STname']: i['ID'] for i in j.json()} if j.status_code == 200 else {}


# In[2]:


if __name__ == '__main__':
    from sys import argv
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('location', help='location weather to be grabbed')
    
    # avoid jupyter notebook exception
    if argv[0][-21:] == 'ipykernel_launcher.py':
        args = parser.parse_args(args=[])
    else:
        args = parser.parse_args()
    
    w = WeaG()
    r = w.grab(args.location)
    if r:
        print(f'{args.location} 觀測時間: {r["O"]} 溫度: {r["T"]:.1f}度C, 濕度: {r["H"]:.0%}, 雨量: {r["R"]:.1f}mm')
    else:
        print(f'{args.location} 查無此站！')


# In[ ]:




