"""
Classes représentant le modèle de données de l'index des orgues de France.
"""

# TODO : implémenter Images, Claviers, Accessoires.
# TODO : init from json

# TODO : JSON cassé par les guillemets d'Open Office...
# TODO : protection du segment json dans évènements (pour l'instant on remplace les ; de Palissy.

# TODO : Supprimer les vieilles fonctions Palissy pour ne garder que POP.

import logging
import json
import re

import utilsorgues as uo
import utilsorgues.codification as cod
import palissy
import gpsmessesinfo
import orgbase

loggerInventaire = logging.getLogger('inventaire')
loggerInventaire.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('./logs/inventaire.log', mode='w', encoding='utf-8')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
loggerInventaire.addHandler(fh)
loggerInventaire.addHandler(ch)

logger_palissy = logging.getLogger('inventaire.Palissy')
logger_palissy.setLevel(logging.INFO)
# create file handler which logs even debug messages
fhp = logging.FileHandler('./logs/inventaire--palissy.log', mode='w', encoding='utf-8')
fhp.setLevel(logging.DEBUG)
# create console handler with a higher log level
shp = logging.StreamHandler()
shp.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatterp = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
fhp.setFormatter(formatterp)
shp.setFormatter(formatterp)
# add the handlers to the logger
logger_palissy.addHandler(fhp)
logger_palissy.addHandler(shp)

loggerGps = logging.getLogger('inventaire.GPS')

loggerInsee = logging.getLogger('inventaire.Insee')


def xstr(s):
    """
    Retourne une chaîne vide si None.
    """
    return s if s is not None else ""


class Accessoires(list):
    """
    Liste d'accessoires
    Un accessoire est décrit par une chaîne, qui normalement doit respecter le config.json de portail.
    """

    def __init__(self, accessoires):
        if accessoires != '':
            self = accessoires.split(',')


class Claviers(list):
    pass


class Clavier(object):
    def __init__(self):
        self.type = str()
        self.is_expressif = bool()
        self.etendue = str()
        self.jeux = list()


class Jeu(object):
    def __init__(self):
        self.type = {'nom': '', 'hauteur': ''}
        self.commentaire = ''
        self.configuration = ''


class Fichiers(list):
    """
    Fichiers sur serveur associés à un orgue.
    """
    def __init__(self, extrait_json=None):
        if extrait_json:
            self.from_json(extrait_json)

    def from_json(self, my_json):
        _json = json.loads(my_json)
        for _fichier in _json:
            self.append(Fichier(json.dumps(_fichier)))

    def to_json(self):
        _liste = list()
        for _fichier in self:
            _liste.append(_fichier.to_dict())
        return json.dumps(_liste)

    def to_list(self):
        _liste = list()
        for _fichier in self:
            _liste.append(_fichier.to_dict())
        return _liste

    def __repr__(self):
        return '<object Fichiers : {} Fichier>'.format(len(self))


class Fichier(object):
    """
    Fichier de la chronologie.
    """
    def __init__(self, extrait_json=None):
        if extrait_json:
            self.from_json(extrait_json)
        else:
            self.file = ''
            self.description = ''

    def from_json(self, my_json):
        _json = json.loads(my_json)
        self.file = _json['file']
        self.description = _json['description']

    def from_str(self, chaine):
        attributs = eval(chaine)
        self.file = attributs['file']
        self.description = attributs['description']

    def to_dict(self):
        return self.__dict__

    def to_str(self):
        return str(self.to_dict())

    def to_json(self):
        return json.dumps(self.__dict__)


class Sources(list):
    """
    Sources.
    """
    def __init__(self, extrait_json=None):
        if extrait_json:
            self.from_json(extrait_json)

    def from_json(self, my_json):
        _json = json.loads(my_json)
        for _source in _json:
            self.append(Source(json.dumps(_source)))

    def to_json(self):
        _liste = list()
        for _source in self:
            _liste.append(_source.to_dict())
        return json.dumps(_liste)

    def to_list(self):
        _liste = list()
        for _source in self:
            _liste.append(_source.to_dict())
        return _liste

    def __repr__(self):
        return '<object Sources : {} sources>'.format(len(self))


class Source(object):
    """
    Source.
    """
    def __init__(self, extrait_json=None):
        if extrait_json:
            self.from_json(extrait_json)
        else:
            self.type = ''
            self.description = ''
            self.lien = ''

    def from_json(self, my_json):
        _json = json.loads(my_json)
        self.type = _json['type']
        self.description = _json['description']
        self.lien = _json['lien']

    def from_str(self, chaine):
        attributs = eval(chaine)
        self.type = attributs['type']
        self.description = attributs['description']
        self.lien = attributs['lien']

    def to_dict(self):
        return self.__dict__

    def to_str(self):
        return str(self.to_dict())

    def to_json(self):
        return json.dumps(self.__dict__)


class Evenements(list):
    """
    Evènements de la chronologie.
    """

    def __init__(self, extrait_json=None):
        if extrait_json:
            self.from_json(extrait_json)

    def from_json(self, my_json):
        _json = json.loads(my_json)
        for _evenement in _json:
            self.append(Evenement(json.dumps(_evenement)))

    def to_json(self):
        _liste = list()
        for _evenement in self:
            _liste.append(_evenement.to_dict())
        return json.dumps(_liste)

    def to_list(self):
        _liste = list()
        for _evenement in self:
            _liste.append(_evenement.to_dict())
        return _liste

    def __repr__(self):
        return '<object Evenements : {} Evenement>'.format(len(self))


class Evenement(object):
    """
    Evènement de la chronologie.
    """

    def __init__(self, extrait_json=None):
        if extrait_json:
            self.from_json(extrait_json)
        else:
            self.annee = None
            self.type = ''
            self.resume = ''
            self.facteurs = list()

    def from_json(self, my_json):
        _json = json.loads(my_json)
        self.annee = _json['annee']
        self.type = _json['type']
        self.resume = _json['resume']
        self.facteurs = _json['facteurs']

    def from_str(self, chaine):
        attributs = eval(chaine)
        self.annee = attributs['annee']
        self.type = attributs['type']
        self.resume = attributs['resume']
        self.facteurs = attributs['facteurs']

    def to_dict(self):
        return self.__dict__

    def to_str(self):
        return str(self.to_dict())

    def to_json(self):
        return json.dumps(self.__dict__)


class OrgueInventaire(object):
    """
    Orgue de l'inventaire national.
    """
    entete = ['Codification',
              'Commune',
              'Edifice',
              'Edifice_standard',
              'Type_edifice',
              'Codification_edifice',
              'Nom_departement',
              'Code_depertament',
              'Nom_region',
              'Code_insee',
              'Ancienne_commune',
              'Adresse',
              'Désignation',
              'Livre',
              'Pages_pdf',
              'Pages_livre',
              'Pages_livre_complement',
              'Latitude',
              'Longitude',
              'OSM_type',
              'OSM_id',
              'Orgbase_manu',
              'Orgbase_commune',
              'Orgbase_auto',
              'Orgbase_desc',
              'Orgbase_facteurs',
              'Orgbase_minicompo',
              'Orgbase_edifice_standard',
              'Orgbase_edifice_log',
              'Orgbase_commune_insee',
              'Reference_palissy',
              'denomination_palissy',
              'Edifice_palissy',
              'protection_palissy',
              'Résumé',
              'Propriétaire',
              'Organisme',
              'Lien de référence',
              'Polyphone',
              'Etat',
              'Elévation',
              'Buffet',
              'Console',
              'Commentaire admin',
              'Diapason',
              'Sommiers',
              'Soufflerie',
              'Transmission notes',
              'Transmission commentaire',
              'Tirage jeux',
              'Tirage commentaire',
              'Commentaire tuyauterie',
              'Evènements',
              'Accessoires',
              'Claviers',
              'Images',
              'Sources',
              'id',
              'user',
              'url',
              'fichiers',
              ]

    def __init__(self, _liste):
        [
            self.codification,
            self.commune,
            self.edifice,
            self.edifice_standard,
            self.type_edifice,
            self.codification_edifice,
            self.nomdepartement,
            self.code_departement,
            self.nomregion,
            self.code_insee,
            self.ancienne_commune,
            self.adresse,
            self.designation,
            self.livre,
            self.pages_pdf,
            self.pages_livre,
            self.pages_livre_complement,
            self.latitude,
            self.longitude,
            self.osm_type,
            self.osm_id,
            self.orgbase_manu,
            self.orgbase_commune,
            self.orgbase_auto,
            self.orgbase_desc,
            self.orgbase_facteurs,
            self.orgbase_minicomposition,
            self.orgbase_edifice_standard,
            self.orgbase_edifice_log,
            self.orgbase_commune_insee,
            self.references_palissy,
            self.denomination_palissy,
            self.edifice_palissy,
            self.protection_palissy,  #
            self.resume,
            self.proprietaire,
            self.organisme,
            self.lien_reference,
            self.is_polyphone,
            self.etat,
            self.elevation,
            self.buffet,
            self.console,
            self.commentaire_admin,
            self.diapason,
            self.sommiers,
            self.soufflerie,
            self.transmission_notes,
            self.transmission_commentaire,
            self.tirage_jeux,
            self.tirage_commentaire,
            self.commentaire_tuyauterie,
            _evenements,
            _accessoires,
            self.claviers,
            self.images,
            _sources,
            self.id,
            self.user,
            self.url,
            _fichiers,
        ] = _liste

        # Retraitement des champs

        # Champs mis à '' par défaut.
        self.designation = xstr(self.designation)
        self.edifice = xstr(self.edifice)

        if self.references_palissy:
            self.references_palissy = self.references_palissy.split(',')
        self.evenements = Evenements(_evenements)
        if _accessoires:
            self.accessoires = Accessoires(_accessoires)
        else:
            self.accessoires = None
        self.fichiers = Fichiers(_fichiers)
        self.sources = Sources(_sources)
        return

    def __repr__(self):
        return '{} {}'.format(self.commune, self.edifice)

    def to_record(self):
        if self.references_palissy is not None:
            _refs_palissy = ",".join(self.references_palissy)
        else:
            _refs_palissy = ''
        if self.accessoires is not None:
            _accessoires = ",".join(self.accessoires)
        else:
            _accessoires = ''
        champs = [self.codification,
                  self.commune,
                  self.edifice,
                  self.edifice_standard,
                  str(self.type_edifice),
                  self.codification_edifice,
                  self.nomdepartement,
                  self.code_departement,
                  self.nomregion,
                  self.code_insee,
                  self.ancienne_commune,
                  self.adresse,
                  self.designation,
                  self.livre,
                  self.pages_pdf,
                  self.pages_livre,
                  self.pages_livre_complement,
                  self.latitude,
                  self.longitude,
                  self.osm_type,
                  self.osm_id,
                  self.orgbase_manu,
                  self.orgbase_commune,
                  self.orgbase_auto,
                  self.orgbase_desc,
                  self.orgbase_facteurs,
                  self.orgbase_minicomposition,
                  self.orgbase_edifice_standard,
                  self.orgbase_edifice_log,
                  self.orgbase_commune_insee,
                  _refs_palissy,
                  self.denomination_palissy,
                  self.edifice_palissy,
                  self.protection_palissy,
                  self.resume,
                  self.proprietaire,
                  self.organisme,
                  self.lien_reference,
                  str(self.is_polyphone),
                  self.etat,
                  self.elevation,
                  self.buffet,
                  self.console,
                  self.commentaire_admin,
                  self.diapason,
                  self.sommiers,
                  self.soufflerie,
                  self.transmission_notes,
                  self.transmission_commentaire,
                  self.tirage_jeux,
                  self.tirage_commentaire,
                  self.commentaire_tuyauterie,
                  self.evenements.to_json(),
                  _accessoires,
                  self.claviers,
                  self.images,
                  self.sources.to_json(),
                  self.id,
                  self.user,
                  self.url,
                  self.fichiers.to_json()
                  ]
        _champs = list()
        for champ in champs:
            if champ is None:
                champ = ''
            _champs.append(champ)
        record = ';'.join(_champs)
        return record

    def to_dict(self):
        """
        TODO : diapason sort null (à modifier dans portail ?)
        TODO : ancienne_commune sort null (à modifier dans portail ?)
        TODO : elevation sort null
        TODO : etat sort null
        TODO : latitude, longitude sort null
        TODO : organisme null
        TODO : osm_id, osm_type null
        TODO : references_palissy null
        TODO : tirages et transmissions null
        TODO : Champs non exportés en JSON :

            self.adresse
            self.edifice_standard,
            self.is_edificestandard,
            self.codification_edifice,

            self.livre,
            self.pages_pdf,
            self.pages_livre,
            self.pages_livre_complement,

            self.orgbase_manu,
            self.orgbase_commune,
            self.orgbase_auto,
            self.orgbase_desc,
            self.orgbase_facteurs,
            self.orgbase_minicomposition,
            self.orgbase_edifice_standard,
            self.orgbase_edifice_log,
            self.orgbase_commune_insee,


            self.denomination_palissy,
            self.edifice_palissy,
            self.protection_palissy,
            self.accessoires,

        """
        if self. references_palissy is not None:
            _refs_palissy = ",".join(self.references_palissy)
        else:
            _refs_palissy = None
        dict_orgue = {
            "id": self.id,
            "updated_by_user": self.user,
            "url": self.url,
            "user": self.user,
            "codification": self.codification,
            "designation": self.designation,
            "is_polyphone": self.is_polyphone,
            "elevation": self.elevation,
            "etat": self.etat,
            "proprietaire": self.proprietaire,
            "commune": self.commune,
            "ancienne_commune": self.ancienne_commune,
            "adresse": self.adresse,
            "edifice": self.edifice,
            "departement": self.nomdepartement,
            "code_departement": self.code_departement,
            "region": self.nomregion,
            "code_insee": self.code_insee,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "osm_type": self.osm_type,
            "osm_id": self.osm_id,
            "commentaire_admin": self.commentaire_admin,
            "resume": self.resume,
            "organisme": self.organisme,
            "lien_reference": self.lien_reference,
            "references_palissy": _refs_palissy,
            "transmission_notes": self.transmission_notes,
            "transmission_commentaire": self.transmission_commentaire,
            "tirage_jeux": self.tirage_jeux,
            "tirage_commentaire": self.tirage_commentaire,
            "buffet": self.buffet,
            "console": self.console,
            "diapason": self.diapason,
            "sommiers": self.sommiers,
            "soufflerie": self.soufflerie,
            "commentaire_tuyauterie": self.commentaire_tuyauterie,
            "claviers": [],
            "evenements": self.evenements.to_list(),
            "images": [],
            "fichiers": self.fichiers.to_list(),
            "sources": self.sources.to_list(),
        }
        if self.accessoires is not None:
            dict_orgue["accessoires"] = self.accessoires
        else:
            dict_orgue["accessoires"] = []
        return dict_orgue

    def standardiser_edifice(self):
        """
        standardiser_edifice :
        - detecter_type_edifice
        - corriger_nom_edifice
        :return:
        """
        if self.edifice != '':
            (edifice_type_extrait, self.type_edifice) = uo.detecter_type_edifice(self.edifice)
            self.edifice_standard = uo.corriger_nom_edifice(edifice_type_extrait, self.commune)
        return

    def codifier_edifice(self):
        """
        codifier_edifice = (detecter_type_edifice + corriger_nom_edifice) + codifier_edifice
        :return:
        """
        if self.edifice_standard != '' and self.edifice_standard is not None:
            self.codification_edifice = cod.codifie_edifice(self.edifice_standard, self.type_edifice)
        else:
            loggerInventaire.info("Pas de nom d'édifice pour l'orgue {}".format(self))
        return

    def get_codification(self):
        return uo.codifier_instrument(self)

    def verifier_existence_insee(self, communes_francaises_par_nom, regions_francaises):
        #
        # Recherche exacte de la commune
        communes_possibles = communes_francaises_par_nom.get(self.commune)
        #
        # Choix de la commune en fixant le département
        if communes_possibles is not None:
            commune_trouvee = None
            for commune in communes_possibles:
                if commune.codedepartement == self.code_departement:
                    commune_trouvee = commune
            #
            if commune_trouvee is not None:
                # Si la commune est de pleins droits :
                if commune_trouvee.typecom == 'COM':
                    self.code_insee = commune_trouvee.code_insee
                    commune_insee = commune_trouvee.nom
                # S'il s'agit d'une commune associée ou déléguée, on renvoie le nom de la commune chef-lieu.
                elif commune_trouvee.typecom == 'COMA' or commune_trouvee.typecom == 'COMD':
                    # Mise à jour de l'ancienne commune
                    self.code_insee = commune_trouvee.comparent
                    commune_insee = commune_trouvee.nom_comparent
                    if self.ancienne_commune == '':
                        self.ancienne_commune = self.commune
                        loggerInsee.debug("Commune trouvée associée ou déléguée : {} {} -> {}"
                                          .format(self.nomdepartement,
                                                  self.commune,
                                                  commune_insee))
                    else:
                        loggerInsee.debug("Ancienne commune déjà renseignée : {}".format(self.ancienne_commune))
                        if self.ancienne_commune != self.commune:
                            loggerInsee.error(
                                "Conflit ancienne commune <{}> et nom de commune associée ou déléguée <{}>"
                                    .format(self.ancienne_commune, self.commune)
                            )
                #
                # Ajout de la région:
                self.nomregion = regions_francaises[commune_trouvee.coderegion].libelle
            else:
                if self.nomdepartement not in ['Nouvelle-Calédonie', 'Saint-Pierre-et-Miquelon']:
                    loggerInsee.critical("MAIS COMMUNE DANS UN AUTRE DEPARTEMENT : {} {} {}".format(self.nomdepartement,
                                                                                                    self.commune,
                                                                                                    communes_possibles))
        else:
            if self.nomdepartement not in ['Nouvelle-Calédonie', 'Saint-Pierre-et-Miquelon']:
                loggerInsee.fatal("COMMUNE_NON_TROUVEE : {} {}".format(self.nomdepartement, self.commune))
        return


class OrguesInventaire(list):
    """
    Index général des orgues de France.
    """

    def __init__(self, fic_csv, presence_entete=True):
        super().__init__()
        with open('./{}'.format(fic_csv), 'r', encoding='utf-8') as fic_totale:  # encoding='iso-8859-1'
            for i, ligne in enumerate(fic_totale):
                # On peut éventuellement ne pas tenir compte de l'entête si présent.
                ligne_debut_lecture = 0
                if presence_entete:
                    ligne_debut_lecture = 1
                if i >= ligne_debut_lecture:
                    champs = ligne.rstrip('\r\n').split(';')
                    _champs = list()
                    for item in champs:
                        if item == '':
                            item = None
                        _champs.append(item)
                    champs = _champs
                    # Vérification du format :
                    if len(champs) != len(OrgueInventaire.entete):
                        loggerInventaire.error('La ligne {} comporte {} champs.'.format(i + 1, len(champs)))
                        for j, champ_entete in enumerate(OrgueInventaire.entete):
                            print(champ_entete, champs[j])
                    # Si tous les champs sont présents :
                    else:
                        orgue = OrgueInventaire(champs)
                    self.append(orgue)
        #
        self._ensemble_communes = set()
        return

    def to_console(self):
        for item in self:
            print(item)
        return None

    def liste_edifices_absents(self):
        for orgue in self:
            if orgue.edifice == '':
                loggerInventaire.warning("Edifice non renseigné {} {}".format(orgue.nomdepartement, orgue.commune))

    def __repr__(self):
        self._ensemble_communes = set([orgue.commune for orgue in self])
        resume = "L'inventaire contient {} orgues, dans {} communes.".format(len(self), len(self._ensemble_communes))
        loggerInventaire.info(resume)
        return resume

    def to_list(self):
        enregistrements = [item.to_record() for item in self]
        return enregistrements

    def to_csv(self, nom_fic_out):
        with open('./{}'.format(nom_fic_out), 'w', encoding='utf-8') as fic_out:
            entete_csv = ";".join(OrgueInventaire.entete)
            fic_out.write(entete_csv + '\n')
            for item in self.to_list():
                fic_out.write(item + '\n')
        return None

    def to_json(self, nom_fic_out_json, limit=-1):
        with open('./{}'.format(nom_fic_out_json), 'w', encoding='utf-8') as fic_out_json:
            # L'objet JSON sérialisé est une liste
            obj_pour_json = list()
            for orgue in self[:limit]:
                obj_pour_json.append(orgue.to_dict())
            chaine_json = json.dumps(obj_pour_json)
            fic_out_json.write(chaine_json)
        return None

    def codifier_departements(self):
        departements = uo.codegeographique.Departements()
        codes_departementaux = departements.to_dict_nom_code()
        for orgue in self:
            if orgue.nomdepartement == 'Saint-Pierre-et-Miquelon':
                orgue.code_departement = 'SP'
            elif orgue.nomdepartement == 'Nouvelle-Calédonie':
                orgue.code_departement = 'NC'
            else:
                orgue.code_departement = codes_departementaux[orgue.nomdepartement]

    def standardiser_edifices(self):
        for orgue in self:
            orgue.standardiser_edifice()

    def codifier_edifices(self):
        for orgue in self:
            orgue.codifier_edifice()

    def codifier_orgues(self):
        """
        A partir des codifications brutes, les discrimine dans le cas
        où elles sont identiques car il ne s'agit pas du même lieu.
        :return: None
        """
        # Création d'un dictionnaire code_court -> [orgues avec ce code_court]
        orgues_avec_meme_codif = dict()
        for orgue in self:
            code_natif = orgue.get_codification()
            code_court = code_natif[:-2]
            if code_court not in orgues_avec_meme_codif:
                orgues_avec_meme_codif[code_court] = [orgue]
            else:
                orgues_avec_meme_codif[code_court].append(orgue)
        # Parcours de ce dictionnaire :
        for code in orgues_avec_meme_codif:
            # Premier de la liste des doublons :
            code_natif = orgues_avec_meme_codif[code][0].get_codification()
            orgues_avec_meme_codif[code][0].codification = code_natif[:21] + '1' + code_natif[21:]
            # Si doublons il y a :
            if len(orgues_avec_meme_codif[code]) > 1:
                indice_edifice = 1
                for i, orgue in enumerate(orgues_avec_meme_codif[code][1:]):
                    # On ne résoud la redondance que si la commune ou l'adresse
                    # n'est pas le même que ceux des orgues précédents :
                    meme_lieu = False
                    for _orgue in orgues_avec_meme_codif[code][:i + 1]:
                        if _orgue.ancienne_commune == orgue.ancienne_commune \
                                and _orgue.adresse == orgue.adresse:
                            meme_lieu = True
                        if _orgue.type_edifice != orgue.type_edifice:
                            meme_lieu = False
                    code_natif = orgue.get_codification()
                    if not meme_lieu:
                        indice_edifice += 1
                        orgue.codification = code_natif[:21] + str(indice_edifice) + code_natif[21:]
                        loggerInventaire.info(
                            'Doublon, codification incrémentée : {} {}'.format(orgue.codification, orgue))
                    else:
                        orgue.codification = code_natif[:21] + str(indice_edifice) + code_natif[21:]
                        loggerInventaire.debug(
                            'Faux doublon, codification inchangée : {} {}'.format(orgue.codification, orgue))

    def detecter_doublons_codifsorgues(self):
        """
        https://webdevdesigner.com/q/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them-24374/
        :return: (list) des coublons
        """
        seen = set()
        doublons = set()
        seen_add = seen.add
        doublons_add = doublons.add
        for orgue in self:
            if orgue.codification in seen:
                doublons_add(orgue.codification)
                loggerInventaire.critical('Codification redondante : {} {}'.format(orgue.codification, orgue))
            else:
                seen_add(orgue.codification)
        return list(doublons)

    def verifier_existences_insee(self):
        communes_francaises_par_nom = uo.codegeographique.Communes().to_dict_par_nom()
        regions_francaises = uo.codegeographique.Regions()
        for orgue in self:
            orgue.verifier_existence_insee(communes_francaises_par_nom, regions_francaises)

    def fixer_polyphones(self):
        for orgue in self:
            if orgue.designation == 'polyphone':
                orgue.is_polyphone = True
            else:
                orgue.is_polyphone = False

    def fixer_liendereference(self):
        for orgue in self:
            if orgue.lien_reference == '':
                orgue.lien_reference = orgue.orgbase_manu

    def fixer_noms_edifices(self):
        for orgue in self:
            if orgue.type_edifice is None:
                type_edif = ''
            else:
                type_edif = orgue.type_edifice + ' '
            if orgue.edifice != type_edif + orgue.edifice_standard:
                loggerInventaire.warning("Vérifiez la correction du nom d'édifice : {}".format(orgue.edifice))
                loggerInventaire.warning("Vérifiez la correction du nom d'édifice : {}".format(type_edif + orgue.edifice_standard))
                orgue.edifice = type_edif + orgue.edifice_standard

    def fixer_fichiers(self, reset=False):
        """
        Ajout des liens vers les futurs fichiers PDF.
        http://inventaire-des-orgues.fr/media/<code_dep>/<code_orgue>/fichiers/<nomdufichier>
        :return:
        """
        url_site = 'http://inventaire-des-orgues.fr'
        for orgue in self:
            # Si option reset activée, on efface tous les fichiers.
            if reset or orgue.fichiers is None:
                orgue.fichiers = Fichiers()
            if orgue.livre != '' and orgue.livre is not None:
                fics = Fichiers()
                fic = Fichier()
                nomfic = '[extrait] ' + orgue.livre
                fic.file = '{}/media/{}/{}/fichiers/{}.pdf'.format(url_site, orgue.code_departement, orgue.codification, orgue.codification)
                fic.description = nomfic
                fics.append(fic)
                orgue.fichiers = fics
        return

    def fixer_sources(self, reset=False):
        """
        Ajout des livres dans les sources.
        :return:
        """
        for orgue in self:
            # Si option reset activée, on efface toutes les sources.
            if reset or orgue.sources is None:
                orgue.sources = Sources()
            if orgue.livre != '' and orgue.livre is not None:
                srcs = Sources()
                src = Source()
                src.type = 'ouvrage'
                src.description = '{}#{}#{}#{}'.format(orgue.livre,
                                                      xstr(orgue.pages_pdf),
                                                      xstr(orgue.pages_livre),
                                                      xstr(orgue.pages_livre_complement))
                src.lien = 'http://explore.inventaire-des-orgues.fr/'
                srcs.append(src)
                orgue.sources = srcs
        return

    def fixer_monumentshistoriques(self, ficbasepalissy, reset=False):
        """
        Ajout des évènements Palissy aux chronologies.
        :param ficbasepalissy : un fichier d'export POP Palissy
        :param reset: booléen : effacement préalable de tous les évènements.
        :return:
        """
        def _split_dpro(champ_dpro):
            """
            Séparation du champ Palissy Pop DPRO
            Liste de protections séparées par des points-virgules.
            (Attention, le format d'une protection n'est pas stable.)
            :return: liste
            """
            dpros = champ_dpro.split(';')
            lldpros = list()
            for dpro in dpros:
                if '\xa0: ' in dpro:
                    date_et_pro = dpro.split('\xa0: ')
                    date_et_pro[1] = date_et_pro[1].strip()
                    lldpros.append(date_et_pro)
                elif ' : ' in dpro:
                    date_et_pro = dpro.split(' : ')
                    date_et_pro[1] = date_et_pro[1].strip()
                    lldpros.append(date_et_pro)
                elif dpro != '':
                    index_sep = dpro.find(' classé')
                    date_et_pro = [dpro[:index_sep], dpro[index_sep + 1:]]
                    date_et_pro[1] = date_et_pro[1].strip()
                    lldpros.append(date_et_pro)
                    loggerInventaire.warning('Champ DPRO mal formatté : {}'.format(dpro))
                else:
                    loggerInventaire.error('Champ DPRO vide : {}'.format(dpro))
            return lldpros

        basepalissy = palissy.OrguesPalissyPop(ficbasepalissy)
        pms = basepalissy.to_dict_pm()
        for orgue in self:
            # Si option reset activée, on efface tous les évènements.
            if reset or orgue.evenements is None:
                orgue.evenements = Evenements()
            if orgue.references_palissy is not None:
                for pm in orgue.references_palissy:
                    if pm != '':
                        orguepalissy = pms.get(pm)
                        if not orguepalissy:
                            loggerInventaire.error(
                                "Fixer Palissy : Un des PM de l'orgue est introuvable dans Palissy : " \
                                + "<{}> {}".format(pm, orgue))
                        else:
                            # Certains champs DPRO ont plusieurs informations.
                            for infos_pro in _split_dpro(orguepalissy.DPRO):
                                evenement = Evenement()
                                # Recherche de l'année de protection
                                if '/' in infos_pro[0]:
                                    evenement.annee = infos_pro[0].split('/')[0]
                                else:
                                    evenement.annee = infos_pro[0]
                                # Type de protection
                                prot = infos_pro[1]
                                if prot == 'déclassé':
                                    # Supprimer evenement
                                    pass
                                elif prot in ['classé au titre objet',
                                              'classé au titre objet partiellement',
                                              'classé au titre immeuble',
                                              'classé MH']:
                                    evenement.type = 'classement_mh'
                                elif prot in ['inscrit au titre objet']:
                                    evenement.type = 'inscription_mh'
                                else:
                                    loggerInventaire.error(
                                        "Fixer Palissy : Champ PROT Palissy Pop illisible : {} {}".format(pm, prot))
                                # Recopie d'autres informations
                                evenement.resume = pm + '\n'
                                evenement.resume += orguepalissy.DPRO.replace(';', ',') + '\n'
                                evenement.resume += orguepalissy.DENO.replace(';', ',') + '\n'
                                evenement.resume += orguepalissy.DOSS.replace(';', ',') + '\n'
                                evenement.resume += orguepalissy.REFE.replace(';', ',') + '\n'
                                orgue.evenements.append(evenement)

    def denombrer_par_commune(self):
        # TODO : départements
        communes = [orgue.commune + ', ' + orgue.nomdepartement for orgue in self]
        compte = {}.fromkeys(set(communes), 0)
        for commune in communes:
            compte[commune] += 1
        return compte

    def mapper_orgbase_sur_inventaire(self):
        ma_orgbase = orgbase.OrguesOrgelbase('orgbase - correction2.csv')
        ma_orgbase.standardiser_edifices()
        for orgue in ma_orgbase:
            # TODO: finir
            print(self)
            # Créer un dico comme celui des communes et taper dedans.
            print(orgue)
            pass

    def mapper_palissypop_sur_inventaire(self, fic_palissy):
        """
        Cherche à associer à un orgue de l'inventaire sa référence Palissy.
        :param fic_palissy: fichier CSV exporté de Palissy
        :return:
        # FIXME : Gestion des accents é sur majuscule.
        # FIXME : Cas de Paris
        """

        def nettoyer_titre_courant_palissy(titre):
            """
            :param titre: titre courant Palissy
            :return: titre courant Palissy simplifié
            """
            titre_nettoye = titre.split(':')[0].rstrip(' ')
            return titre_nettoye

        base_palissy = palissy.OrguesPalissyPop(fic_palissy)
        base_palissy.corriger_insee()
        edifices_refs = base_palissy.to_dict_edifices_refs()

        nombre_orgues_mappes = 0

        def calculer_codes_palissy():
            """
            On calcule les codes d'édifice pour Palissy.
            :return: 
            """
            # FIXME : virgule et ", actuellement"
            # FIXME : codification vides "------" (ancienne cathédrale, cathédrale, etc. sans plus de précision).
            # FIXME : ------ PM12000916 12 Vabres-l'Abbaye 12286 ancienne cathédrale orgue de tribune>
            # FIXME : ,_TEMP PM67001038 67 Krautwiller 67249 église paroissiale, temple Saint-Ulrich orgue de tribune>
            # FIXME : ,_ANCI PM51001754 51 Hautvillers 51287 église paroissiale, ancienne abbatiale Saint-Sindulphe orgue de tribune>
            # FIXME : ------ PM80001682 80 Saint-Riquier 80716 ancienne abbaye orgue de tribune>
            # FIXME : ------ PM92000270 92  0  orgue de tribune : partie instrumentale de l'orgue>
            # FIXME : ------ PM26000485 26 Saint-Paul-Trois-Châteaux 26324 ancienne cathédrale orgue de tribune>
            # FIXME : ,_ANCI PM76001528 76 Rouen 76540 temple protestant, ancienne église Saint-Eloi orgue de tribune : buffet d'orgue>
            # FIXME : ------ PM83001465 83 Saint-Maximin-la-Sainte-Baume 83116 ancienne abbatiale orgue de tribune : buffet d'orgue>
            # FIXME : ...
            for _objet_palissy in base_palissy:
                edifice_palissy_denomination_corrigee, edifice_palissy_type = uo.detecter_type_edifice(_objet_palissy.EDIF)

                edifice_palissy_standard = \
                    uo.corriger_nom_edifice(edifice_palissy_denomination_corrigee, _objet_palissy.COM)

                if edifice_palissy_standard == '':
                    loggerInventaire.warning("Objet Palissy sans nom d'édifice standard : {}".format(_objet_palissy))
                else:
                    _objet_palissy.code_edifice = cod.codifie_edifice(edifice_palissy_standard, edifice_palissy_type)
                    logger_palissy.debug("Codification de l'édifice de l'item Palissy {} {}"
                                    .format(_objet_palissy.code_edifice, _objet_palissy))
            return

        calculer_codes_palissy()

        # Filtrage de la base Palissy pour ne pas chercher les références déjà présentes dans l'inventaire.
        ref_palissy_deja_presentes = sum([orgue_i.references_palissy for orgue_i in self], [])
        base_palissy_filtree = [orgue_pal for orgue_pal in base_palissy if
                                orgue_pal.REF not in ref_palissy_deja_presentes]

        def is_edifices_identiques(edif1, edif2):
            edif1_simple = uo.correcteurorgues.supprimer_accents(edif1)
            edif2_simple = uo.correcteurorgues.supprimer_accents(edif2)
            return edif1_simple == edif2_simple

        # Début de la recherche pour chaque orgue Palissy :
        communes = uo.codegeographique.Communes()
        transitions = uo.codegeographique.Evenements().to_list_anciennne_nouvelle()

        for objet_palissy in base_palissy_filtree:
            # FIXME : garder les accents dans Palissy.
            logger_palissy.info("")
            logger_palissy.info("*******************************")
            logger_palissy.info("Recherche de l'item Palissy {} dans l'inventaire".format(objet_palissy))

            # Vérification de la commune Palissy
            if objet_palissy.INSEE not in [c.codecommune for c in communes]:
                logger_palissy.error('Code INSEE de Palissy non valide {}'.format(objet_palissy))
                # On cherche dans les communes modifiées
                codes_insee_possibles = transitions.get(objet_palissy.INSEE)
                if codes_insee_possibles is None:
                    logger_palissy.critical('Code INSEE de Palissy absurde ! {}'.format(objet_palissy))
                else:
                    logger_palissy.error('Codes INSEE possibles : {}'.format(codes_insee_possibles))

            # Réduction du nom de l'édifice Palissy
            edifice_ply = uo.reduire_edifice(objet_palissy.EDIF, objet_palissy.COM)

            # Début recherche
            orgues_trouves_dans_edifice = []
            # Buffer pour les traces débug à n'afficher qu'en cas d'échec de recherche :
            log = []
            for orgue_inventaire in self:
                edifice_inv = uo._simplifier_nom_edifice(orgue_inventaire.edifice_standard)

                # Si la commune est Paris, on tente de trouver l'édifice :
                if objet_palissy.COM[:6] == 'Paris ' and orgue_inventaire.code_insee == '75056':
                    logger_palissy.debug("Paris")
                    log.append("Corres. Paris - Palissy    : {}".format(edifice_ply))
                    log.append("Corres. Paris - Inventaire : {}, {}".format(
                        edifice_inv,
                        orgue_inventaire.designation))
                    # Si l'édifice est le même
                    if is_edifices_identiques(edifice_inv, edifice_ply):
                        orgues_trouves_dans_edifice.append(orgue_inventaire)

                # Si le code INSEE commune correspond, on est sûr de la commune et on tente de trouver l'édifice :
                elif objet_palissy.INSEE == orgue_inventaire.code_insee:
                    logger_palissy.debug("Code INSEE Palissy trouvé dans l'inventaire {}".format(orgue_inventaire))
                    log.append("Corres. COM - Palissy    : {}".format(edifice_ply))
                    log.append("Corres. COM - Inventaire : {}, {}".format(edifice_inv, orgue_inventaire.designation))
                    # Si l'édifice est le même
                    if is_edifices_identiques(edifice_inv, edifice_ply):
                        orgues_trouves_dans_edifice.append(orgue_inventaire)

                # Sinon on cherche dans la commune associée/déléguée (fusion de communes, etc.)
                elif objet_palissy.COM in orgue_inventaire.ancienne_commune\
                        and objet_palissy.DPT == orgue_inventaire.code_departement:
                    logger_palissy.warning(
                        "Code INSEE Palissy non trouvé dans l'inventaire mais ancienne commune si. : {}.".format(
                            objet_palissy.INSEE))
                    log.append("Corres. COMA/COMD - Palissy    : {}".format(edifice_ply))
                    log.append("Corres. COMA/COMD - Inventaire : {}, {}".format(edifice_inv, orgue_inventaire.designation))
                    # Si l'édifice est le même
                    if edifice_inv.replace('é', 'e').replace('è', 'e') == edifice_ply.replace('é', 'e').replace('è', 'e'):
                        orgues_trouves_dans_edifice.append(orgue_inventaire)
                else:
                    pass
                    # TODO : Il faut aller creuser dans le fichier mouvements du code géographique.
                # En dernier recours, on ne compare que les codifications
                # elif objet_palissy.code_edifice == cod.codifie_edifice(orgue_inventaire.edifice_standard):
                #     log.append("Palissy    : {}".format(
                #         objet_palissy.code_edifice))
                #     log.append("Inventaire : {}".format(
                #         orgue_inventaire.codification))
            #
            # Fin de boucle
            # - Si recherche fructueuse :
            if len(orgues_trouves_dans_edifice) == 1:
                nombre_orgues_mappes += 1
                logger_palissy.info("Cet objet Palissy {} a été trouvé dans l'inventaire ! Correspondance possible !"
                                    .format(objet_palissy))
                # Recopie de la référence Palissy dans l'inventaire, si elle n'est pas déjà présente.
                if objet_palissy.REF not in orgues_trouves_dans_edifice[0].references_palissy:
                    orgues_trouves_dans_edifice[0].references_palissy.append(objet_palissy.REF)
            # - Si plusieurs orgues dans un même édifice, il faut descendre jusqu'à la dénomination :
            elif len(orgues_trouves_dans_edifice) > 1:
                logger_palissy.warning("Plus d'un édifice de l'inventaire correspondant à l'objet dans Palissy {} !"
                                       .format(objet_palissy))
                for orgue in orgues_trouves_dans_edifice:
                    logger_palissy.debug("Orgue trouvé dans l'édifice".format(orgue))
                    if orgue.designation == 'G.O.' \
                            and nettoyer_titre_courant_palissy(objet_palissy.TICO) in ['orgue de tribune',
                                                                                       "tribune d'orgue"]:
                        nombre_orgues_mappes += 1
                        logger_palissy.info("L'orgue Palissy {} a été trouvé dans l'inventaire !"
                                            .format(objet_palissy))
                        # Ajout de la référence si elle n'est pas déjà présente
                        if objet_palissy.REF not in orgue.references_palissy:
                            orgue.references_palissy.append(objet_palissy.REF)
                    if orgue.designation == 'O.C.' \
                            and nettoyer_titre_courant_palissy(objet_palissy.TICO) in ['orgue de choeur']:
                        nombre_orgues_mappes += 1
                        logger_palissy.info("L'orgue Palissy {} a été trouvé dans l'inventaire !"
                                            .format(objet_palissy))
                        # Ajout de la référence si elle n'est pas déjà présente
                        if objet_palissy.REF not in orgue.references_palissy:
                            orgue.references_palissy.append(objet_palissy.REF)
            # - Si le PM n'a pu être associé à l'inventaire :
            else:
                logger_palissy.error("")
                logger_palissy.error("Orgue Palissy non trouvé dans l'inventaire: {}".format(objet_palissy))
                pm_possibles = ",".join(edifices_refs[objet_palissy.INSEE + '---' + objet_palissy.EDIF])
                logger_palissy.error("PM possibles : {}".format(pm_possibles))
                for trace in log:
                    logger_palissy.error("   " + trace)

        logger_palissy.info("Fin de correspondance Inventaire vs. Palissy, {}/{} items de Palissy à injecter."
                            .format(nombre_orgues_mappes, len(base_palissy_filtree)))

    def mapper_coordonnees_gps_picardie(self, rep, dep):
        """
        Cherche à mapper les coordonnées GPS issues d'un fichier CSV extrait du kml.
        Source : site Orgues de Picardie.
        :return:
        """
        import kml_picardie
        orgues_de_picardie = kml_picardie.lecture_picardie(rep, dep)
        #
        for orgue_picard in orgues_de_picardie:
            for orgue in self:
                if orgue.commune == orgue_picard[1]:
                    # Si pas d'édifice, on ne raffine pas.
                    if orgue_picard[2] is None:
                        # On n'écrase pas les données déjà présentes.
                        if (orgue.longitude, orgue.latitude) == ('', ''):
                            orgue.longitude = orgue_picard[3]
                            orgue.latitude = orgue_picard[4]
                            loggerInventaire.info('Orgue picard mappé : {}'
                                                  .format(str(orgue_picard)))
                    # Si un édifice est présent, et trouvé dans l'inventaire :
                    elif orgue_picard[2] == orgue.edifice:
                        # On n'écrase pas les données déjà présentes.
                        if (orgue.longitude, orgue.latitude) == ('', ''):
                            orgue.longitude = orgue_picard[3]
                            orgue.latitude = orgue_picard[4]
                            loggerInventaire.info('Orgue picard mappé : {}'
                                                  .format(str(orgue_picard)))
                    # Sinon
                    pass
        return

    def rechercher_donnees_osm(self, _fic_simple_osm):
        data_osm = list()
        with open(_fic_simple_osm, 'r', encoding='utf-8') as fic_simple_osm:
            for ligne in fic_simple_osm:
                # way;23100587;Église Saint-Louis;45.18977948571429;5.725901744642857;Grenoble;38185;
                objet_osm = ligne.rstrip('\r\n').split(';')
                data_osm.append(objet_osm)
        # Boucle sur les orgues
        compteur = 0
        for orgue in self:
            # Boucle de recherche dans les objets OSM (qui représentent un édifice)
            for edifice_osm in data_osm:
                # La recherche se fait sur les codes INSEE ET nom d'édifice complet
                if orgue.code_insee == edifice_osm[6] and \
                        orgue.edifice == edifice_osm[2].replace('Église', 'église'):
                    compteur += 1
                    loggerInventaire.info(
                        "Edifice OSM trouvé {} {} {}".format(orgue.commune, orgue.edifice, str(compteur)))
                    orgue.osm_type = edifice_osm[0]
                    orgue.osm_id = edifice_osm[1]
                    orgue.latitude = edifice_osm[3]
                    orgue.longitude = edifice_osm[4]

    def rechercher_gps_osm_depuis_id(self):
        for orgue in self:
            if orgue.osm_type and orgue.osm_id:
                pass
                # TODO : Aller chercher XML sur OSM, le lire, calculer barycentre si way ou relation.

    def correction_directe_nom_edifice(self):
        for orgue in self:
            # Correction des édifices Saint ou Sainte sans dénomination : on écrit 'église' par défaut.
            if orgue.edifice[:6] == 'Saint-' or orgue.edifice[:7] == 'Sainte-':
                loggerInventaire.info(
                    'Correction directe édifice : Saint ou Sainte sans préfixe église {}'.format(orgue))
                orgue.edifice = 'église {}'.format(orgue.edifice)
            # Correction de la dénomination 'église paroissiale' en 'église'.
            if orgue.edifice.lower() == 'église paroissiale':
                loggerInventaire.info('Correction directe édifice : église paroissiale devient église {}'.format(orgue))
                orgue.edifice = 'église'
            # Correction de la casse de MIXTE:
            if 'MIXTE' in orgue.edifice:
                loggerInventaire.info('Correction directe édifice : église MIXTE devient église mixte {}'.format(orgue))
                orgue.edifice = orgue.edifice.replace('MIXTE', 'mixte')

    def detecter_noms_edifice_majuscules(self):
        for orgue in self:
            if re.search(".*[A-Z][A-Z].*", orgue.edifice):
                loggerInventaire.info("Pour cet orgue l'édifice est en majuscules : {}".format(orgue))

    def rechercher_coordonnees_gps(self):
        # Construction du dictionnaire des édifices MessesInfo:
        index = gpsmessesinfo.EdificesMessesInfo('../97-data/20181219-Lieux de culte MessesInfo.csv')
        index.standardiser_edifices()
        index.verifier_coordonnees()
        index.verifier_existences_insee()
        edifices_par_commune = index.to_dict()
        for orgue in self:
            # Dégénérescence du nom de l'édifice :
            orgue_edifice_simplifie = \
                uo.generiques.supprimer_accents(
                    uo.correcteurorgues._simplifier_nom_edifice(orgue.edifice_standard))
            edifices_possibles = edifices_par_commune.get(orgue.code_insee, None)
            # Si la commune est répertoriée dans MessesInfo :
            if edifices_possibles is not None:
                # Recherche par nom d'édifice :
                edifice_trouve = None
                for edifice in edifices_possibles:
                    # Dégénérescence du nom de l'édifice :
                    edifice_simplifie = uo.generiques.supprimer_accents(
                        uo.correcteurorgues._simplifier_nom_edifice(edifice.edifice_standard))
                    # TODO : Ajouter gestion des édifices entre parenthèses dans MessesInfo (redondance nom commune).
                    if edifice.edifice_standard == orgue.edifice_standard:
                        loggerGps.info('Edifice trouvé avec nom exact : {} {}'
                                       .format(orgue.commune, orgue.edifice_standard))
                        edifice_trouve = edifice
                    elif edifice_simplifie == orgue_edifice_simplifie:
                        loggerGps.info('Edifice trouvé avec nom simplifié : {} {}'
                                       .format(orgue.commune, orgue.edifice_standard))
                        edifice_trouve = edifice
                    elif edifice_simplifie == orgue_edifice_simplifie:
                        loggerGps.info('Edifice trouvé avec nom simplifié : {} {}'
                                       .format(orgue.commune, orgue.edifice_standard))
                        edifice_trouve = edifice
                    elif len(edifices_possibles) == 1:
                        loggerGps.error("Je ne vois qu'un édifice possible : {} {} celui-ci {}"
                                        .format(orgue.commune, orgue.edifice_standard, edifices_possibles[0]))
                        if 'église' in edifice.edifice_standard or 'eglise' in edifice.edifice_standard:
                            edifice_trouve = edifice
                            loggerGps.info("... et je le choisis !")
                # Conclusion de la recherche :
                if edifice_trouve is not None:
                    orgue.latitude = edifice_trouve.latitude
                    orgue.longitude = edifice_trouve.longitude
                else:
                    loggerGps.error('Edifice non trouvé : {} {}'.format(orgue.commune, orgue.edifice_standard))
            # Si la commmune n'est pas présente dans MessesInfo :
            else:
                loggerGps.error('Commune non trouvée dans la liste des édifices MessesInfo : {}'.format(orgue.commune))
        return
