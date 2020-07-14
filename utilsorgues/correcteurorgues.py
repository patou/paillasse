"""
Fonctions utilitaires pour corriger ou simplifier (dégénéréscence) des noms d'édifices.
"""
import re
import logging

# FIXME : Saint-Pierre-ès-Liens Saint-Pierre-Es-Liens

loggerCorrecteurorgues = logging.getLogger('correcteurogues')
loggerCorrecteurorgues.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fhc = logging.FileHandler('./logs/inventaire--correcteurorgues.log')
fhc.setLevel(logging.DEBUG)
# create console handler with a higher log level
chc = logging.StreamHandler()
chc.setLevel(logging.WARNING)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
fhc.setFormatter(formatter)
chc.setFormatter(formatter)
# add the handlers to the logger
loggerCorrecteurorgues.addHandler(fhc)
loggerCorrecteurorgues.addHandler(chc)


listeMinuscule = ["le", "la", "les", "de", "des", "du", "en", "et"]
listeMajuscule = ["ND"]


def corriger_casse(chaine):
    """
    https://georezo.net/forum/viewtopic.php?pid=256458
    :param chaine:
    :return:
    """
    # Tous les mots de la chaine doivent etre en minuscule
    chaine = chaine.lower()

    # Separation de la chaine par les espaces
    liste_mot = chaine.split(' ')
    new_liste_mot = list()
    for mot in liste_mot:
        liste_mini_mots = mot.split('-')
        new_liste_mini_mots = list()
        for mini_mot in liste_mini_mots:
            if mini_mot not in listeMinuscule:
                mini_mot = mini_mot.title()
            # Mise en miniscule des mots avec apostrophe si non au début du nom.
            if "'" in mini_mot:
                if mini_mot[1] == "'" and mini_mot != liste_mini_mots[0]:
                    mini_mot = mini_mot[0].lower() + mini_mot[1:]
            new_liste_mini_mots.append(mini_mot)
        mot = "-".join(new_liste_mini_mots)
        new_liste_mot.append(mot)
    new_chaine = " ".join(new_liste_mot)
    return new_chaine


def supprimer_accents(chaine):
    """
    Supprime les accents.
    """
    accents = {'E': ['É'],
               'e': ['é', 'è', 'ê', 'ë'],
               'a': ['à', 'ã', 'á', 'â'],
               'i': ['î', 'ï'],
               'u': ['ù', 'ü', 'û'],
               'o': ['ô', 'ö']}
    for (char, accented_chars) in accents.items():
        for accented_char in accented_chars:
            chaine = chaine.replace(accented_char, char)
    return chaine


def detecter_type_edifice(chaine):
    """
    Détecte si l'édifice est d'un type standard.
    Transforme le nom d'édifice.
    Par exemple "église Saint-Georges" devient "Saint-Georges [eglise]"
    :param chaine: dénomination de l'édifice
    :return: dénomination standardisée
    """
    #FIXME : [co-Cathédrale] au lieu de [co-cathédrale]
    #FIXME : FR-78646-VERSA-CHAPEL-X;Versailles;Chapelle du Grand Séminaire
    #FIXME : FR-33063-BORDE-ANCIEN-T;Bordeaux;Ancienne Abbatiale Sainte-Croix;
    new_chaine = ''
    # Attention, l'ordre de la liste compte : mettre d'abord église catholique, ensuite église...
    types_edifice = ['église catholique',
                     'temple protestant',
                     'temple réformé',
                     'ancienne collégiale',
                     'collégiale',
                     'cathédrale metropole',
                     'métropole',
                     'co-cathédrale',
                     'cathédrale église',
                     'cathédrale',
                     'ancienne cathédrale',
                     'basilique',
                     'basilique collegiale',
                     'synagogue',
                     'communauté',
                     'congrégation',
                     'couvent',
                     'carmel',
                     'monastère',
                     'abbaye de bénédictins',
                     'abbaye de bénédictines',
                     'abbaye',
                     'ancienne abbaye',
                     'ancienne abbatiale',
                     'primatiale',
                     'abbatiale',
                     'chapelle royale',
                     'chapelle paroissiale',
                     'chapelle protestante',
                     'chapelle catholique',
                     'chapelle du college',
                     "chapelle de l'ecole",
                     'chapelle du lycee',
                     "chapelle de l'institution",
                     "chapelle de l'orphelinat",
                     'chapelle du pensionnat',
                     "chapelle de l'hopital",
                     "chapelle de la congregation",
                     'chapelle',
                     'sanctuaire',
                     'séminaire',
                     'grand séminaire',
                     'oratoire',
                     'ancienne église',
                     'église abbatiale',
                     'église paroissiale',
                     'église réformée',
                     'église collégiale'
                     'église réformée protestante',
                     'église anglicane',
                     'église protestante reformée',
                     'église protestante',
                     'église mixte',
                     'église anglo-américaine',
                     'église simultanée',
                     'église luthérienne',
                     'école de musique',
                     'école',
                     'collège privé',
                     'collège',
                     'église',
                     'prieuré',
                     'grand temple',
                     'temple',
                     'institution libre',
                     'institution',
                     'institut',
                     'théâtre',
                     'lycée privé',
                     'lycée',
                     'salle',
                     'musée',
                     'conservatoire municipal',
                     'conservatoire national de musique',
                     'conservatoire national de région',
                     'conservatoire national régional',
                     'conservatoire',
                     'clinique']
    if chaine:
        chaine_minuscule = supprimer_accents(chaine).lower()
        type_trouve = False
        for _type_edifice in types_edifice:
            index_denomination = chaine_minuscule.find(supprimer_accents(_type_edifice))
            # Si la chaîne ne comprend pas dénomination connue :
            if index_denomination == -1:
                pass
            elif index_denomination == 0 and not type_trouve:
                type_trouve = True
                type_edifice = _type_edifice
                new_chaine = corriger_casse(chaine[len(type_edifice):].strip(' ')) + ' ' + '[' + type_edifice + ']'
            elif index_denomination > 0 and not type_trouve:
                type_trouve = False
        if not type_trouve:
            new_chaine = corriger_casse(chaine)
            type_edifice = None
            loggerCorrecteurorgues.debug("Aucun type d'édifice reconnu dans : {}.".format(chaine))
        else:
            loggerCorrecteurorgues.debug("Type d'édifice reconnu dans : {}.".format(chaine))
    else:
        loggerCorrecteurorgues.warning("Pas de libellé d'édifice.")
    return new_chaine, type_edifice


def corriger_nom_edifice(chaine, commune=''):
    """
    Corrige le nom de l'édifice.
    Par exemple "St-Georges [église]" devient "Saint-Georges [église]".

    On tient compte de la commune :
    si la commune est dans le nom de l'édifice (à l'exception des Saint...), elle est supprimée de l'édifice.
    # FIXME : FR-35281-SSLAN-EGLISE-X;Saint-Jacques-de-la-Lande;église Saint-Jacques-de-la-Lande;[eglise]
    :param chaine: nom de l'édifice
    :param commune: nom de la commune
    :return: (nom corrigé de l'édifice, trace du traitement)
    """
    #
    # Par défaut :
    new_chaine = 'NOM_EDIFICE_NON_STANDARD'
    # église sans nom :
    if chaine == '[église]':
        new_chaine = chaine
    if 'saint' != chaine.lower()[:5]:
        #
        # Si l'édifice est le nom de la commune, à l'exception des "Saint..." :
        if commune.lower() == chaine.lower():
            new_chaine = 'UN_EDIFICE'
        # Si la commune est présente en surcharge dans l'édifice : Dannemarie (Sainte Anne)
        # (Attention à la casse, variable.)
        elif commune.lower() == chaine.split('(')[0].lower().rstrip(' ') \
                and '(' in chaine \
                and ')' in chaine:
            # Recherche du vrai nom de l'édifice, entre parenthèses.
            match = re.match(r".*[(](.*)[)]", chaine)
            new_chaine = match.group(1)
            # On réinjecte dans la suite des traitements :
            chaine = new_chaine
        # Si la commune est en surcharge, mais une autre information se trouve entre parenthèses
        # [TODO]
        # Si le nom de la commune débute le nom de l'édifice, à l'exception des "Saint..." :
        elif commune.lower() == (chaine[:len(commune)]).lower():
            new_chaine = chaine[len(commune):].lstrip(' ')
            # On réinjecte dans la suite des traitements :
            chaine = new_chaine
        # Si le début du nom de la commune débute le nom de l'édifice :
        elif commune.lower().split(' ')[0] == (chaine[:len(commune.lower().split(' ')[0])]).lower():
            new_chaine = chaine[len(commune.lower().split(' ')[0]):].lstrip(' ')
    #
    # Ajout des traits d'union*
    #TODO : de l'Assomption de Notre-Dame
    #TODO : de la Décollation de Saint-Jean-Baptiste [église]
    #TODO : Toussaints
    if chaine[:3] == 'St ':
        new_chaine = 'Saint-{}'.format(chaine[3:])
    if chaine[:4] == 'St. ':
        new_chaine = 'Saint-{}'.format(chaine[4:])
    if chaine[:4] == 'Ste ':
        new_chaine = 'Sainte-{}'.format(chaine[4:])
    if chaine[:6] == 'Saint ':
        new_chaine = 'Saint-{}'.format(chaine[6:])
    if chaine[:6] == 'Saint-':
        new_chaine = 'Saint-{}'.format(chaine[6:])
    if chaine[:7] == 'Sainte ':
        new_chaine = 'Sainte-{}'.format(chaine[7:])
    if chaine[:7] == 'Sainte-':
        new_chaine = 'Sainte-{}'.format(chaine[7:])
    if chaine[:7] == 'Saints ':
        new_chaine = 'Saints-{}'.format(chaine[7:])
    if chaine[:10] == 'Notre Dame':
        new_chaine = 'Notre-Dame{}'.format(chaine[10:])
    if chaine[:5] == 'N.-D.' or chaine[:2] == 'ND':
        new_chaine = 'Notre-Dame{}'.format(chaine[5:])
    if chaine[:10] == 'Notre-Dame':
        new_chaine = chaine
    if chaine[:14] == 'du Sacré Coeur':#FIXME
        new_chaine = 'du Sacré-Cœur{}'.format(chaine[14:])
    if chaine[:13] == 'du Sacré Cœur':
        new_chaine = 'du Sacré-Cœur{}'.format(chaine[13:])
    if chaine[:13] == 'du Sacré-Cœur':
        new_chaine = 'du Sacré-Cœur{}'.format(chaine[13:])
    if chaine[:11] == 'Sacré Coeur':
        new_chaine = 'Sacré-Cœur{}'.format(chaine[11:])
    if chaine[:11] == 'Sacré-Coeur':
        new_chaine = 'Sacré-Cœur{}'.format(chaine[11:])
    if chaine[:10] == 'Sacré Cœur':
        new_chaine = 'Sacré-Cœur{}'.format(chaine[10:])
    if chaine[:10] == 'Christ Roi'\
            or chaine[:10] == 'CHRIST ROI':
        new_chaine = 'Christ-Roi{}'.format(chaine[10:])
    if chaine[:13] == 'Le Christ Roi':
        new_chaine = 'Christ-Roi{}'.format(chaine[13:])
    if chaine[:8] == 'Nativité':
        new_chaine = 'Nativité{}'.format(chaine[8:])
    if chaine[:11] == 'La Nativité' or chaine[:11] == 'la Nativité':
        new_chaine = 'Nativité{}'.format(chaine[11:])
    if chaine[:14] == 'de la Nativité':
        new_chaine = 'Nativité{}'.format(chaine[14:])
    if chaine[:10] == 'Assomption' or chaine[:12] == "L'Assomption":
        new_chaine = 'Assomption'
    if chaine[:13] == 'La Providence' or chaine[:13] == 'la Providence':
        new_chaine = 'La Providence'
    if chaine[:20] == 'Immaculée Conception' or chaine[:20] == 'Immaculée-Conception':
        new_chaine = 'Immaculée Conception'
    if chaine[:10] == 'La Trinité' or chaine[:10] == 'la Trinité' or chaine[:7] == 'Trinité':
        new_chaine = 'La Trinité'
    # Ramasse-miettes :
    if new_chaine == 'NOM_EDIFICE_NON_STANDARD':
        loggerCorrecteurorgues.debug('NOM_EDIFICE_NON_STANDARD {}'.format(chaine))
        info = new_chaine
        new_chaine = chaine
    else:
        info = 'NOM_EDIFICE_STANDARD'
    #
    # Commune non renseignée :
    if commune == '':
        info = 'EDIFICE_SANS_COMMUNE'
        new_chaine = chaine
    # Suppression espaces
    new_chaine = new_chaine.strip(' ').lstrip('-')
    return new_chaine, info


def simplifier_nom_edifice(nom):
    """
    Suppression de l'information du type d'édifice, supposé balisé par des crochets [].
    Suppression des informations annexes, supposées balisées par des parenthèses ().
    :param nom:
    :return:
    """
    if '[' in nom:
        chaine_plus_simple = nom.split('[')[0].rstrip(' ')
    else:
        chaine_plus_simple = nom
    # On ignore le texte restant entre parenthèses
    chaine_plus_simple = chaine_plus_simple.split('(')[0].rstrip(' ')
    # Remplacemnt des espaces et accents
    chaine_plus_simple = chaine_plus_simple.replace(' ', '-').lower()
    # Nettoyage
    chaine_plus_simple = chaine_plus_simple.rstrip(' ')
    return chaine_plus_simple


def simplifier_nom_edifice_parentheses(nom):
    """
    Suppression de l'information du type d'édifice, supposé balisé par des crochets [].
    On ne garde que l'information intéressante, supposée balisée par des parenthèses ().
    :param nom:
    :return:
    """
    if '[' in nom:
        chaine_plus_simple = nom.split('[')[0].rstrip(' ')
    else:
        chaine_plus_simple = nom
    # On prend uniquement le texte restant entre parenthèses
    if '(' in chaine_plus_simple and ')' in chaine_plus_simple:
        chaine_plus_simple = chaine_plus_simple.split('(')[1].rstrip(')')
    # Remplacemnt des espaces et accents
    chaine_plus_simple = chaine_plus_simple.replace(' ', '-').lower()
    return chaine_plus_simple


def reduire_edifice(edifice):
    # On supprime les termes après parenthèse ouvrante
    edifice2 = edifice.split('(')[0].rstrip(' ')
    # On supprimer les terms après première virgule
    edifice2 = edifice2.split(',')[0].rstrip(' ')
    # On cherche le type d'édifice
    edifice3 = detecter_type_edifice(edifice2)
    edifice4, info = corriger_nom_edifice(edifice3)
    edifice5 = simplifier_nom_edifice(edifice4)
    return edifice5


def test_simplifier_nom_edifice():
    print(simplifier_nom_edifice('Saint-Maurice [eglise]'))
    print(simplifier_nom_edifice('Sainte Elisabeth de Hongrie (Sainte Elisabeth)'))
    print(simplifier_nom_edifice('Saint Jean-Baptiste (Cathédrale de Belley)'))
    return


def test_detecter_type_edifice():
    for nom in [
                'église de la nativité de la Très-Sainte-Vierge',
                'Eglise de la Nativité de la Sainte-Vierge',
                "église de la Nativité-de-la-Sainte-Vierge",
                "église de la nativité de la Très-Sainte-Vierge",
                'église de la Nativité de Notre-Dame',
                "église Notre-Dame-de-l'Assomption",
                "église Notre-Dame-de-l'Assomption",
                "église Notre-Dame-de-l'Assomption",
                "église Notre-Dame-de-l’Assomption",
                'Ancienne Cathédrale Notre-Dame',
                "Co-Cathédrale Notre-Dame-de-l'Annonciation",
                'église Saint-Amour & Saint-Victor',
                'Ecole de musique',
                'église CATHOLIQUE Saint-ALOYSE DE NEUDORF',
                "Cathédrale Saint-Gervais et Saint-Protais",
                "église du Sacré Coeur",
                'Chapelle du Grand Séminaire',
                'Eglise',
                'LES CHAPELLES BOURBON Saint Vincent',
                'église Notre-Dame',
                'église Notre-Dame (ancienne cathédrale)',
                "église du Vœu",
                "Ecole d'orgue de Guyane",
                "église Notre-Dame",
                "Église du Cœur Immaculé de Marie",
                "institution Les Iris",
                "Chapelle du Château",
                "Chapelle de l'Ecole Saint Elme",
                "Grand Temple",
                ]:
        print("{} ---> {}".format(nom, detecter_type_edifice(nom)))
    return


def test_corriger_nom_edifice():
    print(corriger_nom_edifice("Saint-Amour & Saint-Victor [église]", "Saint-Amour"))
    print(corriger_nom_edifice("de la Nativité de la Sainte-Vierge [église]", "Versailles"))
    print(corriger_nom_edifice("notre-dame-de-l'Annonciation [co-cathédrale]", "Bourg-en-Bresse"))
    print(corriger_nom_edifice("notre-dame-de-l'Assomption [église]", "Jassans-Riottier"))
    print(corriger_nom_edifice('les Chapelles Bourbon Saint Vincent', 'LES CHAPELLES BOURBON'))
    return


def test_reduire_edifice():
    print(reduire_edifice('église Notre-Dame (ancienne cathédrale)'))
    print(reduire_edifice('église Saint-Jacques'))
    print(reduire_edifice("Eglise de la Nativité de la Sainte-Vierge"))


if __name__ == '__main__':
    # test_reduire_edifice()
    test_detecter_type_edifice()
    test_corriger_nom_edifice()
    #test_simplifier_nom_edifice()
