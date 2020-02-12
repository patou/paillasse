# -*- coding: utf-8 -*-
"""
Codification d'un orgue
"""
import csv
import logging


logger_codification = logging.getLogger('codification')
logger_codification.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('./inventaire.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger_codification.addHandler(fh)
logger_codification.addHandler(ch)

communes_tests = [
    'La Rochelle',
    'Bellevue',
    'Montluel',
    'Digne-les-Bains',
    'Champagnier',
    'Entrevaux',
    'Forcalquier',
    'Les Mées',
    'Manosque',
    'Foix',
    'Riez',
    'Saint-Auban',
    "Saint-Michel-l'Observatoire"]

def codifier_instrument(orgue):
    """
    Codification d'un orgue de l'inventaire.
    :param orgue: objet de la classe OrgueInventaire
    :return: codification (str)
    """
    logger_codification.debug('codifier_instrument {} {}'.format(str(orgue), str(orgue.commune_insee)))
    code_orgue = ''
    code_orgue += 'FR'
    code_orgue += '-'
    # code_orgue += orgue.code_departement
    code_orgue += orgue.code_insee
    code_orgue += '-'
    code_orgue += codifie_commune(orgue.commune_insee)
    code_orgue += '-'
    code_orgue += codifie_edifice(orgue.edifice_standard)
    code_orgue += '-'
    code_orgue += codifie_denomination(orgue.denomination)
    return code_orgue


def codifie_edifice(edifice):
    """
    Codification d'un édifice sur 6 caractères.
    :param edifice: nom standardisé de l'édifice
    :return: codification
    """
    # FIXME : FR-92073-SURES-COEUR -X;Suresnes;Église du Cœur Immaculé de Marie;
    # FIXME : FR-2B124-GHISO--------X;Ghisoni;église de la nativité de la Très-Sainte-Vierge;
    # FIXME : FR-13055-MARSE---IRIS-X;Marseille;institution Les Iris;
    # FIXME : FR-78646-VERSA-DU CHA-X;Versailles;Chapelle du Château;du Château [chapelle]
    # FIXME : FR-33009-ARCAC-ECOLE -X;Arcachon;Chapelle de l'Ecole Saint Elme;d
    # FIXME : FR-30341-VAUVE-GRAND -T;Vauvert;Grand temple;Grand Temple;
    code_edifice = '------'
    if edifice != '':
        # Si l'edifice n'a pas de nom (qu'un type), exemple fréquent : '[Temple]'
        if edifice[0] == '[' and ']' in edifice:
            edifice = edifice[1:].replace(']','').lower()
            if edifice == 'temple':
                code_edifice = 'TEMPLE'
            elif edifice == 'eglise anglicane':
                code_edifice = 'ANGLIC'
            elif edifice == 'eglise protestante':
                code_edifice = 'PROTES'
            elif edifice == 'eglise lutherienne':
                code_edifice = 'LUTHER'
            elif edifice == 'eglise paroissiale':
                code_edifice = 'EGLISE'
        # On ne garde que le nom d'édifice, pas le type entre crochets
        edifice = edifice.split('[')[0].rstrip(' ')
        # On supprime jusqu'à deux articles en début de nom :
        edifice = _supprimer_article(edifice)
        edifice = _supprimer_article(edifice)
        # On corrige les e dans l'o:
        edifice = edifice.replace('œ', 'OE')
        if edifice[:6] == 'Saint-':
            saint = edifice[6:]
            code_edifice = 'ST' + saint[:4]
        elif edifice[:7] == 'Sainte-':
            sainte = edifice[7:]
            code_edifice = 'ST' + sainte[:4]
        elif edifice in ['Notre-Dame', 'notre-dame']:
            code_edifice = 'NDAME.'
        elif edifice[:10] in ['Notre-Dame', 'notre-dame']:
            notre_dame = edifice[10:]
            # On force les titres de Notre-Dame avec des traits d'union :
            notre_dame = notre_dame.replace(' ', '-')
            fin_notre_dame = notre_dame
            if '-' in notre_dame:
                fin_notre_dame = notre_dame.split('-')[-1]
                # TODO : Suppression de l'article.
            code_edifice = 'ND' + _supprimer_article(fin_notre_dame)[:4]
        elif edifice[:8] in ['Nativité', 'nativité']:
            nativite = edifice[8:]
            if 'B.V.M' in nativite:
                code_edifice = 'NATBVM'
            if 'Notre-Dame' in nativite:
                code_edifice = 'NATNDM'
            if 'Sainte-Vierge' in nativite:
                code_edifice = 'NATSVI'
        else:
            code_edifice = edifice[:6]
        # On complète les caractères manquant par de tirets.
        code_edifice = code_edifice.rjust(6, '-')
        code_edifice = code_edifice.upper()
        code_edifice = supprimer_accents(code_edifice)
    return code_edifice


def codifie_denomination(denomination):
    """
    Codification de la dénomination d'un orgue.
    :param denomination: (str)
    :return: code (str)
    """
    denominations_orgue = {'G.O.': 'T',
                           'O.C.': 'C',
                           'Polyphone': 'P',
                           '' : 'X'}
    if denomination in denominations_orgue.keys():
        code_denomination = denominations_orgue[denomination]
    else:
        logger_codification.error('Dénomination inconnue, je ne reconnais que {} : {}'.format(" | ".join(denominations_orgue.keys()), denomination))
        code_denomination = 'Z'
    return code_denomination


abreviations_4 = {'BEAU': 'BX',
                  'BOUR': 'BZ',
                  'BONN': 'BN',
                  'CHAU': 'CX',
                  'COUR': 'CZ',
                  'FONT': 'FT',
                  'MONT': 'MT',
                  'PONT': 'PT',
                  'VIGN': 'VN',
                  'VILL': 'VL'}

abreviations_5 = {'CASTE': 'CS',
                  'CHAMB': 'CB',
                  'CHAMP': 'CP',
                  'CHATE': 'CT',
                  'MARQU': 'MQ',
                  'MARTI': 'MR',
                  'ROQUE': 'RQ'}

abreviations_6 = {'BELLEV': 'BV',
                  'CHANTE': 'CN',
                  'PIERRE': 'PRR'}

abreviations_8 = {'CHAMPAGN': 'CPN'}


def _supprimer_article(terme):
    """
    Suppression de l'article défini en début de terme.
    :param terme: un nom d'édifice
    :return: nom d'édifice corrigé
    """
    if terme[:2] in ["L'", "l'"]:
        terme_modifie = terme[2:]
    elif terme[:3] in ["Le ", "le ", "La ", "la ", "Le-", "le-", "La-", "la-"]:
        terme_modifie = terme[3:]
    elif terme[:4] in ['Les ', 'les ']:
        terme_modifie = terme[4:]
    elif terme[:2] in ["D'", "d'"]:
        terme_modifie = terme[2:]
    elif terme[:3] in ["De ", "de ", "De-", "de-", "Du ", "du "]:
        terme_modifie = terme[3:]
    elif terme[:4] in ["Des ", "des ", "Des-", "des-"]:
        terme_modifie = terme[4:]
    else:
        terme_modifie = terme
    return terme_modifie


def codifie_commune(commune):
    """
    Codification d'une commune française, sur cinq lettres.
    :param commune:
    :return: code
    """
    # REGLE : L'article inital est omis.
    commune_modifiee = _supprimer_article(commune)
    #
    code = commune_modifiee.upper()
    # REGLE : Abréviations, pour les noms de plus de cinq caractères :
    if len(commune_modifiee) > 5:
        if commune_modifiee[:8] in abreviations_8:
            code = abreviations_8[commune_modifiee[:8]] + commune_modifiee[8:10]
        elif commune_modifiee[:6] in abreviations_6:
            code = abreviations_6[commune_modifiee[:6]] + commune_modifiee[6:9]
        elif commune_modifiee[:5] in abreviations_5:
            code = abreviations_5[commune_modifiee[:5]] + commune_modifiee[4:7]
        elif commune_modifiee[:4] in abreviations_4:
            code = abreviations_4[commune_modifiee[:4]] + commune_modifiee[4:7]
    # REGLE : Si moins de cinq caractères, on répète le dernier jusqu'à cinq.
    if len(code) < 5:
        code = code + code[-1]*(5 - len(code))
    # REGLE : Noms composés :
    # TODO : tirets et espaces cohabitent
    # Les espaces sont considérés comme des tirets
    if ' ' in commune_modifiee:
        commune_modifiee.replace(' ', '-')
    if '-' in commune_modifiee:
        mots = commune_modifiee.split('-')
        mots = [_supprimer_article(m) for m in mots]
        code = commune_modifiee[0] + '.' + mots[-1][:3]
        # REGLE : Saint :
        if mots[0] in ['Saint', 'Sainte', 'Saints', 'Saintes']:
            code = 'SS' + mots[-1][:3]
            # REGLE : MARC devient MC et MAUR devient MR :
            if mots[-1][:4] in ['MARC', 'MAUR']:
                code = 'SS' + 'M' + mots[-1][4] + mots[-1][5]
    if code == commune_modifiee.upper():
        code = commune_modifiee[:5]
    # Post-traitements :
    code = supprimer_accents(code).upper()
    return code


def supprimer_accents(chaine):
    """
    Supprime les accents.
    """
    accents = {'E': ['É','È'],
               'A': ['Â'],
               'e': ['é', 'è', 'ê', 'ë'],
               'a': ['à', 'ã', 'á', 'â'],
               'i': ['î', 'ï'],
               'u': ['ù', 'ü', 'û'],
               'o': ['ô', 'ö']}
    for (char, accented_chars) in accents.items():
        for accented_char in accented_chars:
            chaine = chaine.replace(accented_char, char)
    return chaine

def test_codifie_edifice():
    print(codifie_edifice("notre-dame-de-l'Assomption [eglise]"))
    print(codifie_edifice("de la Nativité de la Sainte-Vierge [eglise]"))

if __name__ == '__main__':
    for com in communes_tests:
        print('Codage {} {}'.format(com, codifie_commune(com)))
    test_codifie_edifice()