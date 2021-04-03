import os
import logging
import json
import pprint
import re
import unidecode
import csv

logger = logging.getLogger('paysdelaloire')
logger.setLevel(logging.DEBUG)

def loadFile(file):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'export', file)) as fichier:
        return json.load(fichier)[2]['data']

def loadImport(departement):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'currentinventaire', departement+'.json')) as renseignements:
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

def generateProprietaire(context, proprietaire):
    if proprietaire is None:
        return ''
    elif 'ville' in proprietaire.lower():
        return "commune"
    elif proprietaire == 'État' or proprietaire == 'Etat':
        return "etat"
    elif proprietaire == 'AOCN':
        return "association_culturelle"
    elif proprietaire == 'Diocèse':
        return "diocese"
    elif proprietaire == 'Paroisse':
        return "paroisse"
    elif (st in proprietaire for st in ['Communauté', 'Congrégation', 'Prieuré']):
        return "congregation"
    elif proprietaire == 'Collège':
        return "etablissement_scolaire"
    elif proprietaire == 'Institut':
        return "conservatoire"
    elif proprietaire == 'Hopital':
        return "hopital"
    else:
        context.log("Proprietaire {} n'héxiste pas".format(proprietaire))
        return None

def generateEtat(context, etat):
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
        context.log("Etat {} n'héxiste pas".format(etat))
        return None

def generateTransmission(context, transmission):
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
        return "numeriques"
    else:
        context.log("Transmission {} n'existe pas".format(transmission))
        return None

def generateTirage(context, transmission):
    if transmission == 'Mécanique':
        return "mecanique"
    elif transmission == 'Électrique':
        return "electrique"
    elif transmission == 'Électropneumatique':
        return "electro_pneumatique"
    elif transmission == 'Tubulaire':
        return "pneumatique_basse_pression"
    elif transmission == 'Informatique':
        return "numerique"
    else:
        context.log("Tirage {} n'existe pas".format(transmission))
        return None

def generateTransmissionCommentaire(transmission):
        return None

def generateTirageCommentaire(transmission):
    if transmission == 'Pneumatique Barker' or transmission == 'Tubulaire':
        return transmission
    else:
        return None

def buildAccessoires(context, combinaisons):
    accessoires = []
    for i in range(1, 41):
        nom = combinaisons["comb_"+str(i)+"_nom"]
        if nom:
            # if accessoire not exit, log message
            accessoires.append(nom)
    return accessoires

def cleanHauteur(hauteur):
    if not hauteur:
        return None
    s = re.search('([-0-9IV/ ]+)', hauteur.replace("'", ""), re.IGNORECASE)
    return s.group(1) if s is not None else None

def cleanJeuNom(nom):
    if not nom:
        return ""
    return unidecode.unidecode(nom.strip().lower().replace("\\\'", "\'"))

def cleanAccessoire(accessoire):
    if not accessoire:
        return ""
    return unidecode.unidecode(accessoire.replace("\\\'", "").replace("\'", "").replace("  ", " ").strip().lower())

def extractFacteur(facteur):
    match = re.search(r"^([^(]*)(\((.*)\))?$", facteur)
    return (cleanFacteurName(match.group(1)), match.group(3)) if match else (None, None)

def cleanFacteurName(nom):
    if not nom:
        return ""
    return re.sub(r"[^a-z]+", " ", unidecode.unidecode(nom).lower().replace("\\\'", "\'")).strip()

def buildJeu(context, nom, hauteur, description):
    return {
        "type": {
            "nom": cleanJeuNom(nom),
            "hauteur": cleanHauteur(hauteur),
        },
        "commentaire": description,
    }

def buildJeux(context, type, definition):
    jeux = []
    for i in range(1, 25 if type != 'ped' else 20):
        if definition[type+"_"+str(i)+"_nom"]:
            jeux.append(buildJeu(context, definition[type+"_"+str(i)+"_nom"], definition[type+"_"+str(i)+"_hauteur"], definition[type+"_"+str(i)+"_spec"]))
    return jeux

def buildClavier(context, type, definition):
    if definition[type + "_notes"]:
        return {
            "type": definition[type] if type != 'ped' else 'Pédalier',
            "etendue": definition[type + "_notes"],
            "jeux": buildJeux(context, type, definition)
        }
    else:
        return None

siecles = {
    "XV": 1450,
    "XVI": 1550,
    "XVII": 1650,
    "XVIII": 1750,
    "XIX": 1850,
    "XX": 1950,
    "XXI": 2000,
}

def extractDate(text):
    match = re.search(r"([0-9]{4}|[XVI]+)(-[0-9]{2,4})?", text)
    if not match:
        return (None, None, None)
    circa = not ("v." in text or "?" in text)
    annee = match.group(1)
    if "X" in annee:
        annee = siecles.get(annee) if annee in siecles else None
        circa = False
    annee_fin = match.group(2)
    if annee_fin and len(annee_fin) == 3:
        annee_fin = annee[:2] + annee_fin[1:]
    return (annee, annee_fin, circa)

evenementTypes = (
    ("construction", ["construction", "orgue neuf", "orgue de", "orgue par", "premier orgue"]),
    ("reconstruction", ["reconstruction"]),
    ("destruction", ["destruction", "incendit"]),
    ("restauration", ["restauration"]),
    ("deplacement", ["deplacement", "demenagement", "installation"]),
    ("relevage", ["relevage", "entretien", "travaux", "reparation", "installe"]),
    ("modifications", ["modification", "transformation", "reharmonisation", "agrandissement"]),
    ("disparition", ["disparition", "destruction"]),
    ("degats", ["degat"]),
    ("inauguration", ["inauguration", "inaugure"]),
    ("classement_mh", ["classement"]),
    ("inscription_mh", ["inscription"]),
)

def extractType(line):
    '''
    Essaye d'extraire le type de l'événement
    '''
    line = unidecode.unidecode(line.lower())
    for type, list in evenementTypes:
        for test in list:
            if test in line:
                return type
    return None

def normalizeFacteur(facteur):
    '''
    Todo utiliser la liste dans le csv.json pour retourner le bon facteur
    '''
    return facteur

def extractEvenementFacteur(context, line, annee, facteurs):
    found = set()
    line = unidecode.unidecode(line.lower())
    for nom, facteurAnnee in facteurs:
        if facteurAnnee == annee:
            found.add(normalizeFacteur(nom))
        else:
            for part in nom.split(" "):
                if part in line:
                    found.add(normalizeFacteur(nom))
    if len(found) == 0:
        # Chercher dans la liste complète des facteurs
        context.log("Pas de facteur trouvé dans {} pour {}".format(line, facteurs))
    return list(found)



def buildEvenements(context, historique, facteurs):
    evenements = []

    if historique['historique']:
        historiques = historique['historique'].split("\n")
        for line in historiques:
            match = re.search(r"(.*) : (.*)", line)
            resume = match.group(2) if match else line
            annee, annee_fin, circa = extractDate(match.group(0)) if match else extractDate(line)
            type = extractType(line)
            facteur = extractEvenementFacteur(context, line, annee, facteurs)
            if annee is None or type is None:
                context.log("Historique : {}".format(line))
                pass
            evenement = {
                "type": type,
                "resume": resume,
                "annee": int(annee),
                "annee_fin": int(annee_fin) if annee_fin is not None else None,
                "circa": circa,
                "facteurs": facteur
            }
            evenements.append(evenement)
    return evenements

def hasNotEvenements(evenements):
    return (len(evenements) == 0) or all('mh' in event["type"] for event in evenements)


class Export:
    '''
        Classes contenant les exports de l'inventaire des paysdelaloire
    '''
    def __init__(self):
        self.renseignements = loadFile('inventaire_renseignements.json')
        self.mecaniques = toDict(loadFile('inventaire_mecanique.json'))
        self.administratif = toDict(loadFile('inventaire_administratif.json'))
        self.historique = toDict(loadFile('inventaire_historique.json'))
        self.sources = toDict(loadFile('inventaire_sources.json'))
        self.combinaisons = toDict(loadFile('inventaire_combinaisons.json'))
        self.claviers = {
            'c1': toDict(loadFile('inventaire_clavier1.json')),
            'c2': toDict(loadFile('inventaire_clavier2.json')),
            'c3': toDict(loadFile('inventaire_clavier3.json')),
            'c4': toDict(loadFile('inventaire_clavier4.json')),
            'ped': toDict(loadFile('inventaire_pedalier.json'))
        }

    def exportCSV(self):
        '''
            Export la liste de facteurs, des jeux et des accessoires
            pour construire ensuite une liste avec la valeur contenu sur l'inventaire
        '''
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'csv', 'jeux.csv'), mode='wt') as file_jeux,\
            open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'csv', 'accessoires.csv'), mode='wt') as file_accessoires,\
            open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'csv', 'facteurs.csv'), mode='wt') as file_facteurs:
            csv_jeux = csv.writer(file_jeux, dialect='excel')
            jeux = set()
            for type in self.claviers.keys():
                for definition in self.claviers[type].values():
                    for i in range(1, 25 if type != 'ped' else 20):
                        if definition[type+"_"+str(i)+"_nom"]:
                            jeux.add((cleanJeuNom(definition[type+"_"+str(i)+"_nom"]), cleanHauteur(definition[type+"_"+str(i)+"_hauteur"])))
            csv_jeux.writerows([[j[0], j[1], ''] for j in sorted(jeux, key=lambda tup: tup[0])])

            facteurs = set()
            for orgue in self.renseignements:
                for i in range(1, 8):
                    if orgue["facteur"+str(i)]:
                        facteurs.add(extractFacteur(orgue["facteur"+str(i)])[0])
            csv_facteurs = csv.writer(file_facteurs, dialect='excel')
            [csv_facteurs.writerow([f, '']) for f in sorted(facteurs)]

            csv_accessoires = csv.writer(file_accessoires, dialect='excel')
            accessoires = set()
            for combinaison in self.combinaisons.values():
                for i in range(1, 41):
                    nom = combinaison["comb_"+str(i)+"_nom"]
                    if nom:
                        accessoires.add(cleanAccessoire(nom))
            csv_accessoires.writerows([[a, ''] for a in sorted(accessoires)])


class Context:
    def __init__(self, id, codification, orgue, export):
        self.id = id
        self.codification = codification
        self.orgue = orgue
        self.export = export

    def log(self, message):
        print(self.codification, ":", message)

def process():
    '''
    Process l'inventaire des pays de la loire
    '''
    current = loadImports()
    export = Export()
    export.exportCSV()

    result = []

    for renseignement in export.renseignements:
        if (renseignement['statut'] == "3"):
            id = renseignement['id']
            departement = extractNumeroDepartement(renseignement['departement'])
            orgue = findCurrentOrgan(current, departement, id)
            if orgue:
                context = Context(id, orgue['codification'], orgue, export)
                try:
                    print('===', id, orgue['codification'], renseignement['edifice'], renseignement['ville'])
                    # Renseignements
                    orgue['emplacement'] = renseignement['emplacement'] if orgue['emplacement'] is None else orgue['emplacement']
                    orgue['designation'] = renseignement['instrument'] if orgue['designation'] is None else orgue['designation']
                    orgue['buffet'] = renseignement['buffet'] if orgue['buffet'] is None else orgue['buffet']
                    orgue['diapason'] = renseignement['diapason'] if orgue['diapason'] is None else orgue['diapason']
                    orgue['temperament'] = renseignement['temperament'] if orgue['temperament'] is None else orgue['temperament']
                    orgue['buffet'] = renseignement['buffet'] if orgue['buffet'] is None else orgue['buffet']
                    if len(orgue['images']) == 0:
                        orgue['images'].append({
                            "credit": renseignement['credit'] if renseignement['credit'] else 'www.orguepaysdelaloire.fr',
                            "url": "http://orguepaysdelaloire.fr/inventory/upload/"+renseignement['image']
                        })
                    # Mécanique
                    orgue['transmission_notes'] = generateTransmission(context, export.mecaniques[id]['traction_notes']) if orgue['transmission_notes'] is None else orgue['transmission_notes']
                    orgue['transmission_commentaire'] = generateTransmissionCommentaire(export.mecaniques[id]['traction_notes']) if orgue['transmission_commentaire'] is None else orgue['transmission_commentaire']
                    orgue['tirage_jeux'] = generateTirage(context, export.mecaniques[id]['traction_jeux']) if orgue['tirage_jeux'] is None else orgue['tirage_jeux']
                    orgue['tirage_commentaire'] = generateTirageCommentaire(export.mecaniques[id]['traction_jeux']) if orgue['tirage_commentaire'] is None else orgue['tirage_commentaire']
                    orgue['console'] = export.mecaniques[id]['console'] if orgue['console'] is None else orgue['console']
                    orgue['sommiers'] = generateSommiers(export.mecaniques[id]) if orgue['sommiers'] is None else orgue['sommiers']
                    orgue['soufflerie'] = generateSoufflerie(export.mecaniques[id]) if orgue['soufflerie'] is None else orgue['soufflerie']
                    # Administratif
                    orgue['proprietaire'] = generateProprietaire(context, export.administratif[id]['proprietaire']) if orgue['proprietaire'] is None else orgue['proprietaire']
                    orgue['etat'] = generateEtat(context, export.administratif[id]['etat']) if orgue['etat'] is None else orgue['etat']
                    if len(orgue['accessoires']) == 0:
                        orgue['accessoires'] = buildAccessoires(context, export.combinaisons[id])
                    if len(orgue['claviers']) == 0:
                        for c in ['c1', 'c2', 'c3', 'c4', 'ped']:
                            clavier = buildClavier(context, c, export.claviers[c][id])
                            if clavier is not None:
                                orgue['claviers'].append(clavier)
                    # Evenments
                    facteurs = []
                    for i in range(1, 8):
                        if renseignement["facteur"+str(i)]:
                            facteurs.append(extractFacteur(renseignement["facteur"+str(i)]))
                    if hasNotEvenements(orgue['evenements']):
                        orgue['evenements'].extend(buildEvenements(context, export.historique[id], facteurs))
                        orgue['evenements'] = sorted(orgue['evenements'], key = lambda i: i['annee'])

                    result.append(orgue)
                except e:
                    context.log(e)

    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'paysdelaloire.json'), 'w') as outfile:
        json.dump(result, outfile, indent = 4, ensure_ascii=False)



if __name__ == '__main__':
    process()
