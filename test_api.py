import requests
import pprint
import json

import wincred


credential = wincred.get_generic_credential('proxy')
IDENT = credential.username
MDP = credential.password
ADRESSE = 'proxy-surf.rte-france.com'
PORT = '3128'

PROXIES = {
    'https': 'https://{}:{}@{}:{}'.format(IDENT, MDP, ADRESSE, PORT),
    'http': 'http://{}:{}@{}:{}'.format(IDENT, MDP, ADRESSE, PORT)
    }

headers = {'Authorization': 'Token bae43c6b34b56c429e2723ae1f19fb431c4456da'}
headers_local = {'Authorization': 'Token 566391d77db3ccd29784470360823a0a365ade3c'}

departements = [50, 35, 14, 56, 75, 44, 13, 92, 26, 72]

for code_dep in departements:
    response = requests.get("https://inventaire-des-orgues.fr/api/v1/orgues/",
                            params={"code_departement": code_dep},
                            headers=headers,
                            proxies=PROXIES)

    # response = requests.get("http://127.0.0.1:8000/api/v1/orgues/",
    # params={"code_departement": 72}, headers=headers_local)


    # pprint.pprint(response.json())
    f = open('../98-indexes/exports-api/sortie-api-{}.json'.format(str(code_dep)), 'w', encoding='utf-8')
    print('Export via API du departement {}'.format(code_dep))
    json.dump(response.json()['results'], f)
    f.close()

