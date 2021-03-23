
import os
import logging
import json

logger = logging.getLogger('paysdelaloire')
logger.setLevel(logging.DEBUG)

def loadFile(file):
    with open(file) as renseignements:
        return json.load(renseignements)[2]['data']

def toDict(data):
    return {item['id']:item for item in data}


def process():
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

    for orgue in renseignements:
        if (orgue['statut'] == "3"):
            id = orgue['id']
            print(id, orgue['edifice'], administratif[id]['proprietaire'], mecaniques[id]['traction_notes'])
            # print(mecaniques[id-1])
    


if __name__ == '__main__':
    process()
