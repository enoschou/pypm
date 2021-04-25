#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests, json

class WeaG:
    
    def __init__(self, key):
        self.URL = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/'
        self.DATAID = ['O-A0001-001', 'O-A0003-001']
        self.API = [f'{self.URL}/{d}' for d in self.DATAID]
        self.AUTH = key
        self.ELEMENTS = [{'T':'TEMP','H':'HUMD','R':'H_24R'}, {'T':'TEMP','H':'HUMD','R':'24R'}]
        self.PARAMS = [{'Authorization': self.AUTH, 'elementName': ','.join(e.values())}
                       for e in self.ELEMENTS]
    
    def grab(self, location):
        for i, api in enumerate(self.API):
            p = self.PARAMS[i]
            p['locationName'] = location
            r = requests.get(api, params=p)
            if r.status_code == 200:
                j = json.loads(r.text)
                r.close()
                locs = j['records']['location']
                wea = self._extract(location, locs, self.ELEMENTS[i])
                if wea:
                    return wea
            else:
                r.close()
        
        return None
    
    def _extract(self, location, locations, elements):
        for loc in locations:
            r = {}
            if loc['locationName'] == location:
                r['O'] = loc['time']['obsTime']
                for ename in loc['weatherElement']:
                    for e in elements:
                        if ename['elementName'] == elements[e]:
                            r[e] = float(ename['elementValue'])
                            break
                return r

        return None


# In[2]:


if __name__ == '__main__':
    from sys import argv
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('location', help='location weather to be grabbed')
    parser.add_argument('-k', '--key', type=str, required=True, help='氣象局授權碼')
    args = parser.parse_args()
    
    w = WeaG(args.key)
    r = w.grab(args.location)
    if r:
        print(f'{args.location} 觀測時間: {r["O"]} 溫度: {r["T"]:.1f}度C, 濕度: {r["H"]:.0%}, 雨量: {r["R"]:.1f}mm')
    else:
        print(f'{args.location} 查無此站！')

