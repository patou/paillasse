import requests


"""
https://geo.api.gouv.fr/communes?lat=49.16555601714287&lon=0.4502110057142857&
fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre
"""
_proxies={'https': 'https://I24853:Montava36@proxy-surf.rte-france.com:3128',
                            'http': 'http://I24853:Montava36@proxy-surf.rte-france.com:3128'}

(_lat, _lon) = (49.16555601714287,0.4502110057142857)
url = 'https://geo.api.gouv.fr/communes'
param = {'lat': _lat, 'lon': _lon, 'fields': 'nom,code,codesPostaux,codeDepartement,codeRegion,population', 'format': 'json', 'geometry': 'centre'}
r = requests.get(url, params = param, proxies = _proxies)
print(r.text)
j = eval(r.text)
print(j[0]['nom'], j[0]['code'])