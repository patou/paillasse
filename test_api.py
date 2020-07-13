import requests
import pprint
import json

headers = {'Authorization': 'Token bae43c6b34b56c429e2723ae1f19fb431c4456da'}
headers_local = {'Authorization': 'Token 566391d77db3ccd29784470360823a0a365ade3c'}
response = requests.get("https://inventaire-des-orgues.fr/api/v1/orgues/", params={"code_departement": 50}, headers=headers)
#response = requests.get("https://inventaire-des-orgues.fr/api/v1/orgues/", params={"code_departement": 72}, headers=headers)
#response = requests.get("http://127.0.0.1:8000/api/v1/orgues/", params={"code_departement": 72}, headers=headers_local)


pprint.pprint(response.json())
f = open('../../98-indexes/sortie-api-50.json', 'w', encoding='utf-8')
json.dump(response.json()['results'][0], f)
f.close()

