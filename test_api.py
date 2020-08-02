import sys
import requests
import pprint
import json

import wincred


local = True

credential = wincred.get_generic_credential('proxy')
IDENT = credential.username
MDP = credential.password
ADRESSE = 'proxy-surf.rte-france.com'
PORT = '3128'

URL_LOCALE = "http://127.0.0.1:8000/api/v1/orgues/"
URL_SERVEUR = "https://www.inventaire-des-orgues.fr/api/v1/orgues/"

PROXIES = {
    'https': 'https://{}:{}@{}:{}'.format(IDENT, MDP, ADRESSE, PORT),
    'http': 'http://{}:{}@{}:{}'.format(IDENT, MDP, ADRESSE, PORT)
    }

headers = {'Authorization': 'Token bae43c6b34b56c429e2723ae1f19fb431c4456da'}
headers_local = {'Authorization': 'Token 1ed30d32655cfeab92640e36114d8da755494c7b'}

departements = [1, 72, 50, 35, 14, 56, 75, 44, 13, 92, 26, 29]

for code_dep in departements:
    if local:
        response = requests.get(URL_LOCALE,
                                params={"code_departement": code_dep},
                                headers=headers_local)
    else:
        response = requests.get(URL_SERVEUR,
                                params={"code_departement": code_dep},
                                headers=headers,
                                proxies=PROXIES)

    # pprint.pprint(response.json())
    if local:
        f = open('../98-indexes/exports-api-local/sortie-api-{}.json'.format(str(code_dep)), 'w', encoding='utf-8')
    else:
        f = open('../98-indexes/exports-api/sortie-api-{}.json'.format(str(code_dep)), 'w', encoding='utf-8')
    print('Export via API du departement {}'.format(code_dep))
    json.dump(response.json()['results'], f)
    f.close()

if __name__ == '__main__':
    pass
