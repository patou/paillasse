"""
Parse les fichiers json exportés par API.
Indique si le facteur n'est pas présent en configuration.
"""

import json

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

facteurs_bdd = []

for code_dep in CHOIX_CODE_DEPARTEMENT:
    f = open('../98-indexes/exports-api/sortie-api-{}.json'.format(code_dep[0]))
    for orgue in json.load(f):
        for ev in orgue['evenements']:
            fs = ev['facteurs']
            facteurs_bdd.extend(fs)
    f.close()
facteurs_bdd = set(facteurs_bdd)

config = open('../90-site/portail/orgues/management/commands/config.json', 'r')
facteurs_config = json.load(config)['facteurs']
for facteur in facteurs_bdd:
    if facteur not in facteurs_config:
        print('Facteur non présent en configuration {}'.format(facteur))
config.close()

print('La base de donnée exportée via API contient {} facteurs.'.format(str(len(facteurs_bdd))))
fichier_facteurs = open('../98-indexes/exports-api/facteurs_bdd.csv', 'w')
fichier_facteurs.writelines(facteurs_bdd)
fichier_facteurs.close()
