# -*- coding: utf-8 -*-
"""
Codification d'un orgue
"""
import logging

logger_codification = logging.getLogger('codification')
logger_codification.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('./logs/inventaire--codification.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger_codification.addHandler(fh)
logger_codification.addHandler(ch)

communes_tests = [
    'Champcueil',
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
    "Saint-Michel-l'Observatoire",
    "Les Ponts-de-Cé",
    "Val de Moder",
    "Île-d'Arz",
    "L'Île-d'Yeu",
    "Luçon",
]

edifices_tests = [
    "Collégiale Saint-Quentin [basilique]",
    "de Monneaux [temple]",
    "[école de musique]",
    "de l'Institution Lamartine [chapelle]",
    "Saint-Côme & Saint-Damien [église]",
    "Saint-Leu [église]",
    "Notre-Dame-de-L’Assomption [église]",
    "Saint-Amour & Saint-Victor [église]",
    "notre-dame-de-l'Assomption [eglise]",
    "notre-dame-de-L'Assomption [eglise]",
    "Notre-dame-de-L'Assomption [eglise]",
    "Nativité de la Très-Sainte-Vierge [église]",
    "de la Nativité de la Sainte-Vierge [eglise]",
    "Nativité de la Sainte-Vierge [église]",
    "de la Nativité de la Sainte-Vierge [église]",
    "de la Nativité-de-la-Sainte-Vierge [église]",
    "de la Nativité de la Très-Sainte-Vierge [église]",
    "de la Nativité de Notre-Dame [église]",
]

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


def supprimer_accents(chaine):
    """
    Supprime les accents et cédilles.
    """
    accents = {'E': ['É', 'È', 'Ê', 'Ë'],
               'A': ['À', 'Á', 'Â', 'Ã'],
               'I': ['Î', 'Ï'],
               'U': ['Ù', 'Ü', 'Û'],
               'O': ['Ô', 'Ö'],
               'C': ['Ç'],
               'e': ['é', 'è', 'ê', 'ë'],
               'a': ['à', 'á', 'â', 'ã'],
               'i': ['î', 'ï'],
               'u': ['ù', 'ü', 'û'],
               'o': ['ô', 'ö'],
               'c': ['ç']
               }
    for (char, accented_chars) in accents.items():
        for accented_char in accented_chars:
            chaine = chaine.replace(accented_char, char)
    return chaine


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
    code_orgue += orgue.code_insee
    code_orgue += '-'
    code_orgue += codifie_commune(orgue.commune_insee)
    code_orgue += '-'
    code_orgue += codifie_edifice(orgue.edifice_standard)
    code_orgue += '-'
    code_orgue += codifie_denomination(orgue.designation)
    return code_orgue


def codifie_edifice(edifice):
    """
    Codification d'un édifice sur 6 caractères.
    :param edifice: nom standardisé de l'édifice
    :return: codification
    """
    # FIXME : FR-38544-VIENN-STANDR-X
    # FIXME : FR-92073-SURES-COEUR -X;Suresnes;Église du Cœur Immaculé de Marie;
    # FIXME : EVANGE
    # FIXME : FR - 25262 - FUANS - -------X;
    # FIXME : FR-70526-VAUVI--------X;Vauvillers;église de la Nativité

    code_edifice = '------'
    if edifice == '':
        logger_codification.error("Pas de nom d'édifice :")
    else:
        # Si l'edifice n'a pas de nom (qu'un type), exemple fréquent : '[Temple]'
        if edifice[0] == '[' and ']' in edifice:
            edifice = edifice[1:].replace(']', '').lower()
            if edifice in [
                    'temple',
                    'grand temple',
                    'temple protestant',
                    'temple réformé',
                    ]:
                code_edifice = 'TEMPLE'
            elif edifice in [
                    'église protestante',
                    'temple prostestant',
                    'chapelle protestante',
                    ]:
                code_edifice = 'PROTES'
            elif edifice == 'église réformée':
                code_edifice = 'REFORM'
            elif edifice == 'église luthérienne':
                code_edifice = 'LUTHER'
            elif edifice in [
                    'église catholique',
                    'église paroissiale',
                    'église',
                    'église abbatiale',
                    ]:
                code_edifice = 'EGLISE'
            elif edifice == 'église mixte':
                code_edifice = 'EMIXTE'
            elif edifice == 'église anglicane':
                code_edifice = 'ANGLIC'
            elif edifice == 'synagogue':
                code_edifice = 'SYNAGO'
            elif edifice in [
                    'conservatoire national de région',
                    'conservatoire national régional',
                    'conservatoire',
                    'conservatoire municipal',
                    'école de musique',
                    ]:
                code_edifice = 'MUSIQU'
            elif edifice == 'séminaire':
                code_edifice = 'SEMINA'
            elif edifice == "chapelle de l'hopital":
                code_edifice = 'HOPITA'
            elif edifice == "chapelle du college":
                code_edifice = 'COLLEG'
            else:
                logger_codification.error("Absence codification avec type seul, sans nom : {}".format(edifice))
        else:
            # On ne garde que le nom d'édifice, pas le type entre crochets
            edifice = edifice.split('[')[0].rstrip(' ')
            # On supprime jusqu'à deux articles en début de nom :
            edifice = _supprimer_article(edifice)
            edifice = _supprimer_article(edifice)
            # On corrige les e dans l'o (car deux caractères au lieu d'un seul):
            edifice = edifice.replace('œ', 'oe')
            # Sacré-Coeur:
            if 'Sacré-Coeur' in edifice:
                code_edifice = 'SCOEUR'
            # Codification des GRAND (séminaire, théâtre, casino, ...)
            elif edifice[:5] == 'grand':
                if len(edifice) >= 10:
                    code_edifice = 'GD' + edifice[6:10]
                else:
                    code_edifice = 'GRANDD'
            # Codification des églises au sein d'une congrégation :
            if edifice[:12] == 'congrégation':
                edifice = edifice[12:]
                edifice = _supprimer_article(edifice)
                edifice = _supprimer_article(edifice)
            # Codification Missions étrangères
            if 'Missions Étrangères' in edifice:
                code_edifice = 'MISSET'
            # Codification des églises au sein d'une école :
            if edifice[:5] == 'école' or edifice[:5] == 'ecole' or edifice[:7] == 'collège':
                if len(edifice) < 5:
                    code_edifice = 'ECOLEE'
                else:
                    # TODO : appeler codification de façon récursive ou tout simplement supprimer école
                    code_edifice = 'ECO' + edifice[-3:]
            # Codification des églises dédicacées à un saint ou une sainte :
            # FIXME : Saint-Jean-Marie Vianney (Basilique Sainte-Philomène, Basilique Saint-Sixte)
            # FIXME : Saint-Jacques (Abbaye de Chanoines Réguliers de Saint Augustin Saint-Rémy)
            # FIXME : Saint-Martin-Notre-Dame et Saint-André
            # FIXME : Saint-François-Xavier (Saint-Joseph)
            # FIXME : Saint-Pierre & Saint-Paul (Église Notre-Dame)
            # Cas particuliers :
            if edifice == 'Saint-Pierre-ès-Liens':
                code_edifice = 'STPIEL'
            elif edifice == 'Saint-Marceau':
                code_edifice = 'STMARU'
            elif edifice == 'Saint-Martin-ès-Vignes':
                code_edifice = 'STMAEV'
            elif edifice == "Sainte-Thérèse d'Avila":
                code_edifice = 'STTHEA'
            elif edifice == "Sainte-Thérèse de l'Enfant-Jésus":
                code_edifice = 'STTHEL'
            elif edifice == 'Saint-Jean-Bosco':
                code_edifice = 'STJBOS'
            elif edifice == 'Saint-Jean-Baptiste':
                code_edifice = 'STJBAP'
            elif edifice == 'Saint-Jean-Baptiste-de-la-Salle':
                code_edifice = 'STJDLS'
            elif edifice == "Saint-François d'Assise":
                code_edifice = 'STFASS'
            elif edifice == "Saint-François de Paule":
                code_edifice = 'STFPAU'
            elif edifice == "Sainte-Jeanne d'Arc":
                code_edifice = 'STJARC'
            elif edifice[:6] == 'Saint-':
                saint = edifice[6:]
                # Exception : Plusieurs saints, mais sans regarder dans les parenthèses :
                # FIXME : Saint-Pierre & Saint-Paul (Église Notre-Dame)
                if 'Saint' in saint and saint.find('(') <= saint.find('Saint'):
                    if saint == 'Denis du Saint-Sacrement':
                        code_edifice = 'ST' + 'DSSS'
                    elif '&' in saint:
                        premier_saint = saint.split('&')[0].rstrip()
                        deuxieme_saint = saint.split('&')[1].lstrip().lstrip('Saint-')
                        code_edifice = 'SS' + premier_saint[0] + premier_saint[-1] + deuxieme_saint[0] + deuxieme_saint[-1]
                    else:
                        logger_codification.error("Nom d'édifice avec plusieurs saints non géré : {}".format(edifice))
                        code_edifice = 'SS' + saint[:4]
                    """
                    elif saint == 'Paul & Saint-Louis':
                        code_edifice = 'SS' + 'PLLS'
                    elif saint == 'Cyr & Sainte-Julitte' or saint == 'Cyr & Sainte-Juliette':
                        code_edifice = 'SS' + 'JNMN'
                    elif saint == 'Jean & Saint-Martin':
                        code_edifice = 'SS' + 'JNMN'
                    elif saint == 'Nicolas & Saint-Guillaume':
                        code_edifice = 'SS' + 'NSGE'
                    elif saint == 'Côme & Saint-Damien':
                        code_edifice = 'SS' + 'CEDN'
                    elif saint == 'Julien & Saint-Antoine':
                        code_edifice = 'SS' + 'JNAE'
                    elif saint == 'Simon & Saint-Jude':
                        code_edifice = 'SS' + 'SNJE'
                    elif saint == 'Gervais & Saint-Protais':
                        code_edifice = 'SS' + 'GSPS'
                    elif saint == 'Georges & Saint-Ludan':
                        code_edifice = 'SS' + 'GSLN'
                    elif saint == 'Nazaire & Saint-Celse':
                        code_edifice = 'SS' + 'NZCE'
                    elif saint == 'Paul & Saint-Serge':
                        code_edifice = 'SS' + 'PLSE'
                    elif saint == 'Juste & Saint-Pasteur' or saint == 'Just-Saint-Pasteur':
                        code_edifice = 'SS' + 'JEPR'
                    elif saint == 'Philippe & Saint-Jacques':
                        code_edifice = 'SS' + 'PEJS'
                    elif saint == 'Pierre & Saint-Paul':
                        code_edifice = 'SS' + 'PEPL'
                    """
                else:
                    code_edifice = 'ST' + saint[:4]
            elif edifice[:7] == 'Sainte-':
                sainte = edifice[7:]
                code_edifice = 'ST' + sainte[:4]
            # Eglises dédicacées à Saint-Jean-Baptiste :
            elif 'Nativité-de-Saint-Jean-Baptiste' in edifice:
                code_edifice = 'NATSJB'
            # Codification des églises dédicacées à la Sainte-Vierge :
            elif edifice.lower() == 'notre-dame':
                code_edifice = 'NDAMEV'
            elif edifice[:10].lower() == 'notre-dame':
                notre_dame = edifice[10:]
                # On force les titres de Notre-Dame avec des traits d'union :
                notre_dame = notre_dame.replace(' ', '-')
                fin_notre_dame = notre_dame
                if '-' in notre_dame:
                    fin_notre_dame = notre_dame.split('-')[-1]
                    # TODO : Suppression de l'article.
                code_edifice = 'ND' + _supprimer_article(fin_notre_dame)[:4]
            # Nativité :
            elif edifice[:8].lower() == 'nativité':
                nativite = edifice[8:]
                if nativite == '':
                    code_edifice = 'NATIVI'
                elif 'B.V.M' in nativite:
                    code_edifice = 'NATBVM'
                elif 'Notre-Dame' in nativite:
                    code_edifice = 'NATNDM'
                elif 'Sainte-Vierge' in nativite or 'Vierge' in nativite:
                    code_edifice = 'NATSVI'
                else:
                    code_edifice = 'NATIVI'
            # Ramasse-miettes
            elif code_edifice == '------':
                code_edifice = edifice[:6]
            # On complète les caractères manquant par le dernier caractère.
            # FIXME : FR-75056-PARIS-COEUR -T;Paris;église du Cœur Eucharistique;
            code_edifice = code_edifice.ljust(6, code_edifice[-1])
            code_edifice = code_edifice.upper()
            code_edifice = supprimer_accents(code_edifice)
            code_edifice = code_edifice.replace(' ', '_')
            code_edifice = code_edifice.replace('.', '_')
        # Contrôle final
        if code_edifice == '------':
            logger_codification.critical("Echec de la codification de l'édifice : {}".format(edifice))
    return code_edifice


def codifie_denomination(denomination):
    """
    Codification de la dénomination d'un orgue.
    :param denomination: (str)
    :return: code (str)
    Dans les ouvrages d'inventaire, et d'une façon générale, dénomination et emplacement sont souvent confondus.
    """
    denominations_orgue = {'G.O.': 'T',
                           'Grand Orgue': 'T',
                           'orgue de tribune': 'T',
                           'orgue de transept': 'C',
                           'orgue positif': 'D',
                           "orgue d'accompagnement": 'C',
                           'petit orgue': 'D',
                           'positif': 'D',
                           'grand positif': 'D',
                           'chapelle': 'D',
                           "chapelle d'hiver": 'D',
                           'chapelle de la Vierge': 'D',
                           'sacristie': 'D',
                           'O.C.': 'C',
                           'O.C.1': 'C',
                           'O.C.2': 'D',
                           'O.C. 1': 'C',
                           'O.C. 2': 'D',
                           'Crypte': 'Y',
                           'coffre': '0',
                           'Coffre': '0',
                           'orgue coffre': '0',
                           'auditorium': '1',
                           'orgue 1': '1',
                           'orgue 2': '2',
                           'ancien': '1',
                           'nouveau': '2',
                           '1': '1',
                           '2': '2',
                           '3': '3',
                           '4': '4',
                           '5': '5',
                           '6': '6',
                           '7': '7',
                           'I': '1',
                           'II': '2',
                           'III': '3',
                           'IV': '4',
                           'V': '5',
                           'VI': '6',
                           'VII': '7',
                           "Orgue d'étude": '1',
                           'Orgue espagnol': '2',
                           'Orgue majorquin': '3',
                           'Orgue napolitain': '4',
                           "orgue d'étude (1982)": '1',
                           "orgue d'étude (1968)": '2',
                           'polyphone': 'P',
                           'buffet': 'B',
                           'orgue à rouleau': 'R',
                           '': 'X'}
    if denomination in denominations_orgue.keys():
        code_denomination = denominations_orgue[denomination]
    # Les dénominations de type 1--blabla sont décryptées
    elif '--' in denomination:
        code_denomination = denomination.split('--')[0]
    # Code dénomination par défaut :
    else:
        logger_codification.error('Dénomination inconnue : {}'.format(denomination))
        code_denomination = 'A'
    return code_denomination


def _supprimer_article(terme):
    """
    Suppression de l'article défini en début de terme.
    :param terme: un nom d'édifice
    :return: nom d'édifice corrigé
    """
    if terme[:2] in ["L'", "l'", "L’", "l’"]:
        terme_modifie = terme[2:]
    elif terme[:3] in ["Le ", "le ", "La ", "la ", "Le-", "le-", "La-", "la-"]:
        terme_modifie = terme[3:]
    elif terme[:4] in ['Les ', 'les ']:
        terme_modifie = terme[4:]
    elif terme[:2] in ["D'", "d'", "D’", "d’"]:
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
    Source : Codification nationale de sites du réseau public de transport d'électricité.
    Nota : Une codification n'est pas unique, car plusieurs communes peuvent avoir même codification.
    """
    # REGLE : L'article inital est omis.
    commune_modifiee = _supprimer_article(commune)
    #
    code = commune_modifiee.upper()
    # REGLE : Abréviations, pour les noms de plus de cinq caractères :
    if len(commune_modifiee) > 5:
        # FIXME : 3 ou 2 car abbr
        if code[:8] in abreviations_8:
            code = abreviations_8[code[:8]] + code[8:10]
        # FIXME : 3 ou 2 car abbr
        elif code[:6] in abreviations_6:
            code = abreviations_6[code[:6]] + code[6:9]
        elif code[:5] in abreviations_5:
            code = abreviations_5[code[:5]] + code[5:8]
        elif code[:4] in abreviations_4:
            code = abreviations_4[code[:4]] + code[4:7]
    # REGLE : Noms composés :
    # Les espaces sont considérés comme des tirets
    if ' ' in commune_modifiee:
        commune_modifiee = commune_modifiee.replace(' ', '-')
    # REGLE : on ne prend que le premier et dernier des mots, sans article :
    if '-' in commune_modifiee:
        mots = commune_modifiee.split('-')
        mots = [_supprimer_article(m) for m in mots]
        code = commune_modifiee[0] + '_' + mots[-1][:3]
        # REGLE : Saint devient SS :
        if mots[0] in ['Saint', 'Sainte', 'Saints', 'Saintes']:
            code = 'SS' + mots[-1][:3]
            # REGLE : MARC devient MC et MAUR devient MR :
            if mots[-1][:4] in ['MARC', 'MAUR']:
                code = 'SS' + 'M' + mots[-1][4] + mots[-1][5]
    if code == commune_modifiee.upper():
        code = commune_modifiee[:5]
    # REGLE : Si moins de cinq caractères, on répète le dernier jusqu'à cinq.
    if len(code) < 5:
        code = code + code[-1] * (5 - len(code))
    # Post-traitements :
    code = supprimer_accents(code).upper()
    return code


def test_codifie_edifice():
    for edifice in edifices_tests:
        print('Codage édifice : {} {}'.format(codifie_edifice(edifice), edifice))


def test_codifie_commune():
    for com in communes_tests:
        print('Codage commune : {} {}'.format(codifie_commune(com), com))


if __name__ == '__main__':
    test_codifie_commune()
    test_codifie_edifice()
