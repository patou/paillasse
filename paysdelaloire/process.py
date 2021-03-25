9
import os
import logging
import json
import pprint
import re

logger = logging.getLogger('paysdelaloire')
logger.setLevel(logging.DEBUG)

def loadFile(file):
    with open('export/'+file) as fichier:
        return json.load(fichier)[2]['data']

def loadImport(departement):
    with open('currentinventaire/'+departement+'.json') as renseignements:
        return json.load(renseignements)['results']

def toDict(data):
    return {item['id']:item for item in data}

def loadImports():
    return {
        '44': loadImport('44'),
        '49': loadImport('49'),
        '53': loadImport('53'),
        '72': loadImport('72'),
        '85': loadImport('85'),
    }

def extractNumeroDepartement(departement):
    return re.search('\\(([0-9]+)\\)', departement, re.IGNORECASE).group(1)

def findCurrentOrgan(current, departement, id):
    link = "http://orguepaysdelaloire.fr/inventory/admin_orgue.php?id=" + id
    for item in current[departement]:
        for source in item['sources']:
            if source['lien'] == link:
                return item
    return {}

def generateSoufflerie(mecanique):
    result = mecanique['soufflerie_type']
    if mecanique['soufflerie_spec']:
        result += ", " + mecanique['soufflerie_spec']
    return result

def generateSommiers(mecanique):
    result = mecanique['sommiers_type']
    if mecanique['sommiers_spec']:
        result += ", " + mecanique['sommiers_spec']
    return result

def generateProprietaire(etat):
    if etat is None:
        return ''
    elif 'ville' in etat.lower():
        return "commune"
    elif etat == 'État' or etat == 'Etat':
        return "etat"
    elif etat == 'AOCN':
        return "association_culturelle"
    elif etat == 'Diocèse':
        return "diocese"
    elif etat == 'Paroisse':
        return "paroisse"
    elif (st in etat for st in ['Communauté', 'Congrégation', 'Prieuré']):
        return "congregation"
    elif etat == 'Collège':
        return "etablissement_scolaire"
    elif etat == 'Institut':
        return "conservatoire"
    elif etat == 'Hopital':
        return "hopital"
    else:
        return None

def generateEtat(etat):
    if etat == 'Excellent':
        return "tres_bon"
    elif etat == 'Bon':
        return "bon"
    elif etat == 'Moyen':
        return "altere"
    elif etat == 'Mauvais':
        return "altere"
    elif etat == 'Injouable':
        return "degrade"
    else:
        return None

def generateTransmission(transmission):
    if transmission == 'Mécanique':
        return "mecanique"
    elif transmission == 'Pneumatique Barker':
        return "mecanique_barker"
    elif transmission == 'Électrique':
        return "electrique"
    elif transmission == 'Électropneumatique':
        return "electro_pneumatique"
    elif transmission == 'Tubulaire':
        return "pneumatique"
    elif transmission == 'Informatique':
        return "electrique"
    else:
        return None

def generateTirage(transmission):
    if transmission == 'Mécanique':
        return "mecanique"
    elif transmission == 'Électrique':
        return "electrique"
    elif transmission == 'Électropneumatique':
        return "electro_pneumatique"
    elif transmission == 'Tubulaire':
        return "pneumatique_basse_pression"
    elif transmission == 'Informatique':
        return "electrique"
    else:
        return None

def generateTransmissionCommentaire(transmission):
    if transmission == 'Informatique':
        return transmission
    else:
        return None

def generateTirageCommentaire(transmission):
    if transmission == 'Pneumatique Barker' or transmission == 'Tubulaire' or transmission == 'Informatique':
        return transmission
    else:
        return None

def process():
    current = loadImports()
    pprint.pprint(current, depth=1)
    renseignements = loadFile('inventaire_renseignements.json')
    mecaniques = toDict(loadFile('inventaire_mecanique.json'))
    administratif = toDict(loadFile('inventaire_administratif.json'))
    historique = toDict(loadFile('inventaire_historique.json'))
    sources = toDict(loadFile('inventaire_sources.json'))
    clavier1 = toDict(loadFile('inventaire_clavier1.json'))
    clavier2 = toDict(loadFile('inventaire_clavier2.json'))
    clavier3 = toDict(loadFile('inventaire_clavier3.json'))
    clavier4 = toDict(loadFile('inventaire_clavier4.json'))
    pedalier = toDict(loadFile('inventaire_pedalier.json'))
    result = []

    for orgue in renseignements:
        if (orgue['statut'] == "3"):
            id = orgue['id']
            departement = extractNumeroDepartement(orgue['departement'])
            obj = findCurrentOrgan(current, departement, id)
            if obj:
                print(id, obj['codification'], orgue['edifice'], orgue['ville'])
                # Renseignements
                obj['emplacement'] = orgue['emplacement'] if obj['emplacement'] is None else obj['emplacement']
                obj['designation'] = orgue['instrument'] if obj['designation'] is None else obj['designation']
                obj['buffet'] = orgue['buffet'] if obj['buffet'] is None else obj['buffet']
                obj['diapason'] = orgue['diapason'] if obj['diapason'] is None else obj['diapason']
                obj['temperament'] = orgue['temperament'] if obj['temperament'] is None else obj['temperament']
                obj['buffet'] = orgue['buffet'] if obj['buffet'] is None else obj['buffet']
                if len(obj['images']) == 0:
                    obj['images'].append({
                        "credit": orgue['credit'] if orgue['credit'] else 'www.orguepaysdelaloire.fr',
                        "is_principale": True,
                        "image": "http://orguepaysdelaloire.fr/inventory/upload/"+orgue['image']
                    })
                # Mécanique
                obj['transmission_notes'] = generateTransmission(mecaniques[id]['traction_notes']) if obj['transmission_notes'] is None else obj['transmission_notes']
                obj['transmission_commentaire'] = generateTransmissionCommentaire(mecaniques[id]['traction_notes']) if obj['transmission_commentaire'] is None else obj['transmission_commentaire']
                obj['tirage_jeux'] = generateTirage(mecaniques[id]['traction_jeux']) if obj['tirage_jeux'] is None else obj['tirage_jeux']
                obj['tirage_commentaire'] = generateTirageCommentaire(mecaniques[id]['traction_jeux']) if obj['tirage_commentaire'] is None else obj['tirage_commentaire']
                obj['console'] = mecaniques[id]['console'] if obj['console'] is None else obj['console']
                obj['sommiers'] = generateSommiers(mecaniques[id]) if obj['sommiers'] is None else obj['sommiers']
                obj['soufflerie'] = generateSoufflerie(mecaniques[id]) if obj['soufflerie'] is None else obj['soufflerie']
                # Administratif
                obj['proprietaire'] = generateProprietaire(administratif[id]['proprietaire']) if obj['proprietaire'] is None else obj['proprietaire']
                obj['etat'] = generateEtat(administratif[id]['etat']) if obj['etat'] is None else obj['etat']
                
                
                result.append(obj)
    
    with open('paysdelaloire.json', 'w') as outfile:
        json.dump(result, outfile, indent = 4, ensure_ascii=False)
            # print(mecaniques[id-1])
    


if __name__ == '__main__':
    process()
