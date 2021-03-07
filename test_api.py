import sys
import requests
import pprint
import json

import wincred

CHOIX_CODE_DEPARTEMENT = (
    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05'),
    ('06', '06'),
    ('07', '07'),
    ('08', '08'),
    ('09', '09'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('2A', '2A'),
    ('2B', '2B'),
    ('30', '30'),
    ('31', '31'),
    ('32', '32'),
    ('33', '33'),
    ('34', '34'),
    ('35', '35'),
    ('36', '36'),
    ('37', '37'),
    ('38', '38'),
    ('39', '39'),
    ('40', '40'),
    ('41', '41'),
    ('42', '42'),
    ('43', '43'),
    ('44', '44'),
    ('45', '45'),
    ('46', '46'),
    ('47', '47'),
    ('48', '48'),
    ('49', '49'),
    ('50', '50'),
    ('51', '51'),
    ('52', '52'),
    ('53', '53'),
    ('54', '54'),
    ('55', '55'),
    ('56', '56'),
    ('57', '57'),
    ('58', '58'),
    ('59', '59'),
    ('60', '60'),
    ('61', '61'),
    ('62', '62'),
    ('63', '63'),
    ('64', '64'),
    ('65', '65'),
    ('66', '66'),
    ('67', '67'),
    ('68', '68'),
    ('69', '69'),
    ('70', '70'),
    ('71', '71'),
    ('72', '72'),
    ('73', '73'),
    ('74', '74'),
    ('75', '75'),
    ('76', '76'),
    ('77', '77'),
    ('78', '78'),
    ('79', '79'),
    ('80', '80'),
    ('81', '81'),
    ('82', '82'),
    ('83', '83'),
    ('84', '84'),
    ('85', '85'),
    ('86', '86'),
    ('87', '87'),
    ('88', '88'),
    ('89', '89'),
    ('90', '90'),
    ('91', '91'),
    ('92', '92'),
    ('93', '93'),
    ('94', '94'),
    ('95', '95'),
    ('971', '971'),
    ('972', '972'),
    ('973', '973'),
    ('974', '974'),
    ('976', '976'),

)

local = False

credential = wincred.get_generic_credential('proxy-surf.rte-france.com')
IDENT = credential.username
MDP = credential.password

ADRESSE = 'proxy-surf.rte-france.com'
PORT = '3128'

URL_LOCALE = "http://127.0.0.1:8000/api/v1/orgues/"
URL_SERVEUR = "https://inventaire-des-orgues.fr/api/v1/orgues/"

PROXIES = {
    'https': 'https://{}:{}@{}:{}'.format(IDENT, MDP, ADRESSE, PORT),
    'http': 'http://{}:{}@{}:{}'.format(IDENT, MDP, ADRESSE, PORT)
    }

headers = {'Authorization': 'Token bae43c6b34b56c429e2723ae1f19fb431c4456da'}
headers_local = {'Authorization': 'Token 1ed30d32655cfeab92640e36114d8da755494c7b'}

#departements = ['72', '50', '35', '14', '56', '75', '44', '13', '92', '26', '29']

#departements = ['08']

for code_dep in [doublet[0] for doublet in CHOIX_CODE_DEPARTEMENT]:
    if local:
        response = requests.get(URL_LOCALE,
                                params={"code_departement": code_dep},
                                headers=headers_local)
    else:
        response = requests.get(URL_SERVEUR,
                                params={"code_departement": code_dep},
                                headers=headers,
                                proxies=PROXIES)

    pprint.pprint(response.content)
    if local:
        f = open('../98-indexes/exports-api-local/sortie-api-{}.json'.format(str(code_dep)), 'w', encoding='utf-8')
    else:
        f = open('../98-indexes/exports-api/sortie-api-{}.json'.format(str(code_dep)), 'w', encoding='utf-8')
    print('Export via API du departement {}'.format(code_dep))
    json.dump(response.json()['results'], f)
    f.close()

if __name__ == '__main__':
    pass
