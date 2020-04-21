import requests
import pprint
import json

headers = {'Authorization': 'Token bae43c6b34b56c429e2723ae1f19fb431c4456da'}
#response = requests.get("https://inventaire-des-orgues.fr/api/v1/orgues/", params={"code_departement": 51}, headers=headers)
response = requests.get("https://inventaire-des-orgues.fr/api/v1/orgues/", params={"code_departement": 72}, headers=headers)

pprint.pprint(response.json())
f = open('../../98-indexes/sortie-api.json', 'w', encoding='utf-8')
json.dump(response.json()['results'][0], f)
f.close()

