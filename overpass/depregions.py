import requests
import json

PROXIES = {'https': 'https://I24853:Montava36@proxy-surf.rte-france.com:3128',
                            'http': 'http://I24853:Montava36@proxy-surf.rte-france.com:3128'}

f = open('D:\\Users\\poullennecgwi\\Downloads\\OSM\\regions.json', 'r')
jregions = json.load(f)
f.close()

regions = list()
for region in jregions:
    regions.append(region['nom'])
print(regions)

for region in jregions:
    code_region = region['code']
    url = 'https://geo.api.gouv.fr/regions/{}/departements?fields=nom,code'.format(code_region)
    r = requests.get(url, proxies = PROXIES)
    j = eval(r.text)
    deps = list()
    for dep in j:
        #print(dep['nom'], dep['code'])
        deps.append(dep['code'])
    print(region['nom'], code_region, deps)
