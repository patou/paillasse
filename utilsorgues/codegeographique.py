"""
Classes de gestion du code géographique national français de l'INSEE.

Codification des collectivités d'outre-mer (COM)
https://www.insee.fr/fr/information/2028040
"""

import logging


REP_GEODATA = '../99-geodata/'

FIC_FRANCE_COMMUNES_INSEE = REP_GEODATA + 'France2018.txt'
FIC_FRANCE_DEPARTEMENTS_INSEE = REP_GEODATA + 'depts2018.txt'
FIC_FRANCE_REGIONS_INSEE = REP_GEODATA + 'reg2018.txt'

loggerCodegeogaphique = logging.getLogger('codegeographique')
loggerCodegeogaphique.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('inventaire.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
loggerCodegeogaphique.addHandler(fh)
loggerCodegeogaphique.addHandler(ch)


class Region(object):
    """
    Une région
    """
    def __init__(self, _code, _cheflieu, _typenomenclair, _nomenclairmaj, _nomenclair):
        self.code = _code
        self.cheflieu = _cheflieu
        self.typenomenclair = _typenomenclair
        self.nomenclairmaj = _nomenclairmaj
        self.nomenclair = _nomenclair

    def __repr__(self):
        return 'Région : {}, {}'.format(self.nomenclair, self.code)


class Regions(dict):
    """
    Dictionnaire des régions
    """
    def __init__(self):
        super().__init__()
        with open(FIC_FRANCE_REGIONS_INSEE, 'r', encoding='ansi') as fic_csv:
            # on ignore l'entête
            lignes = fic_csv.readlines()[1:]
            ll = [item.strip('\n').split('\t') for item in lignes]
            regions = [Region(*ligne) for ligne in ll]
            # Construction d'un dictionnaire {nom: commune}
            for region in regions:
                if region.code not in self.keys():
                    self[region.code] = region
            return


class Departement(object):
    """
    Un département
    """
    def __init__(self, _region, _code, _cheflieu, _typenomenclair, _nomenclairmaj, _nomenclair):
        self.region = _region
        self.code = _code
        self.cheflieu = _cheflieu
        self.typenomenclair = _typenomenclair
        self.nomenclairmaj = _nomenclairmaj
        self.nomenclair = _nomenclair

    def __repr__(self):
        return '{}, {}, {}'.format(self.nomenclair, self.code, self.region)


class Departements(dict):
    """
    Dictionnaire des départements
    """
    def __init__(self):
        super().__init__()
        with open(FIC_FRANCE_DEPARTEMENTS_INSEE, 'r', encoding='ansi') as fic_csv:
            # on ignore l'entête
            lignes = fic_csv.readlines()[1:]
            ll = [item.strip('\n').split('\t') for item in lignes]
            departements = [Departement(*ligne) for ligne in ll]
            # Construction d'un dictionnaire {nom: commune}
            for departement in departements:
                if departement.code not in self.keys():
                    self[departement.code] = departement
            return

    def to_dict_nom_code(self):
        dict_nom_code = dict()
        for departement in self.values():
            dict_nom_code[departement.nomenclair] = departement.code
        return dict_nom_code


class Commune(object):
    """
    Une commune de France
    https://www.insee.fr/fr/information/2668350
    """
    def __init__(self, _actual, _coderegion, _codedepartement, _codecommune,
                 _rattachement, _typenomenclair, _article, _nomenclair, les_departements):
        """
        :param _actual:
        actual =
        1 	commune actuelle
        2 	commune « associée » : loi Marcellin de 1971
        3 	commune périmée
        4 	ancien code dû à un changement de département
        5 	arrondissement municipal
        6 	commune déléguée
        9 	fraction cantonale
        :param _coderegion:
        :param _codedepartement:
        :param _codecommune:
        :param _rattachement:
        :param _typenomenclair:
        :param _article:
        :param _nomenclair:
        :param les_departements:
        """
        signification_actual = {'1': 'ACTUELLE',
                                '2': 'ASSOCIEE',
                                '3': 'PERIMEE',
                                '4': 'CHANGEMENT_DEP',
                                '5': 'ARR_MUNICIPAL',
                                '6': 'DELEGUEE',
                                '9': 'FRACTION_CANTON'}
        self.actual = _actual
        self.statut = signification_actual.get(self.actual, 'ETAT_COMMUNE_INCONNU')
        self.coderegion = _coderegion
        self.nomregion = ''
        self.codedepartement = _codedepartement
        self.nomdepartement = les_departements[self.codedepartement].nomenclair
        self.codecommune = _codecommune
        self.rattachement = _rattachement
        self.typenomenclair = _typenomenclair
        self.article = _article
        self.nomenclair = _nomenclair
        if self.typenomenclair in ['0', '1']:  # Pas d'article
            self.nom = self.nomenclair
        elif self.typenomenclair == '5':  # L'
            self.nom = self.article[1:-1] + self.nomenclair
        else:  # Le, La, Les, Aux, Las, Los
            self.nom = self.article[1:-1] + ' ' + self.nomenclair
        self.code_insee = self.codedepartement + self.codecommune

    def __repr__(self):
        if self.actual == '1' or self.actual == '3':
            return '<{}, {}, {}, {}, {}>'.format(
                self.nom, self.code_insee, self.codedepartement, self.nomdepartement, self.statut)
        else:
            return '<{}, {}, {}, {}, {} : {}>'.format(
                self.nom, self.code_insee, self.codedepartement, self.nomdepartement, self.statut, self.rattachement)


class Communes(dict):
    """
    Dictionnaire des ommunes de France
    clés : nom INSEE des communes ET code INSEE des communes
    valeur : objet commune
    """
    def __init__(self, transform=None):
        #
        # On charge les départements.
        departements_francais = Departements()
        #
        if transform is None:

            def identite(x):
                return x

            transform = identite
        super().__init__()
        #
        with open(FIC_FRANCE_COMMUNES_INSEE, 'r', encoding='ansi') as fic_csv:
            # on ignore l'entête
            lignes_fic_communes = fic_csv.readlines()[1:]
            ll = [item.split('\t') for item in lignes_fic_communes]
            # Attention : numéro de département = int dans le fichier INSEE

            def _wrap(ligne):
                wrap = ligne[0], ligne[4], ligne[5], ligne[6], ligne[10], ligne[11],\
                       transform(ligne[14]), transform(ligne[15])
                return wrap

            # On ne prend que les communes actuelles, associées et déléguées
            communes = [Commune(*_wrap(ligne), departements_francais) for ligne in ll
                        if ligne[0] in ['1', '2', '3', '6']]
            # Construction d'un dictionnaire {nom: commune}
            for commune in communes:
                # Clés = noms
                if commune.nom not in self.keys():
                    self[commune.nom] = [commune]
                else:
                    # Si la commune n'existe pas déjà (l'unicité est donnée par le code INSEE) :
                    if commune.code_insee not in [com.code_insee for com in self[commune.nom]]:
                        self[commune.nom].append(commune)
                    else:
                        del commune
                # Clés = code INSEE
                if commune.code_insee not in self.keys():
                    self[commune.code_insee] = commune
                else:
                    print("ERROR : CODE INSEE EN DOUBLE !")
            return


def test_dict_communes():
    communes_francaises = Communes()
    print(communes_francaises["Rochefort"])
    print(communes_francaises["Rochefort"][1])
    print(communes_francaises["Corcelles"][0])
    print(communes_francaises["Corcelles"][0].statut)
    print(communes_francaises["Corcelles"][0].rattachement)
    print(communes_francaises["Cordieux"])
    print(communes_francaises["Bagnoles-de-l'Orne"])
    #
    print(communes_francaises['01262'])
    return


def test_dict_departements():
    departements_francais = Departements()
    print(departements_francais["22"])
    return


def test_dict_inverse_departements():
    departements_francais = Departements()
    print(departements_francais.to_dict_nom_code()["Côtes-d'Armor"])
    return


def test_dict_regions():
    regions_francaises = Regions()
    print(regions_francaises["93"])
    return


if __name__ == '__main__':
    test_dict_communes()
    test_dict_departements()
    test_dict_inverse_departements()
    test_dict_regions()
