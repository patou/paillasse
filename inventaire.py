"""
Classes représentant le modèle de données de l'index des orgues de France.
"""

import logging
import json
import palissy
import utilsorgues
import gpsmessesinfo
import orgbase
import re


loggerInventaire = logging.getLogger('inventaire')
loggerInventaire.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('./inventaire.log', mode='w', encoding='utf-8')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
loggerInventaire.addHandler(fh)
loggerInventaire.addHandler(ch)

logger_palissy = logging.getLogger('inventaire.Palissy')
logger_palissy.setLevel(logging.WARNING)
# create file handler which logs even debug messages
fhp = logging.FileHandler('./inventaire--palissy.log', mode='w', encoding='utf-8')
fhp.setLevel(logging.DEBUG)
# create console handler with a higher log level
shp = logging.StreamHandler()
shp.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatterp = logging.Formatter('lp - %(levelname)s - %(message)s')
fhp.setFormatter(formatterp)
shp.setFormatter(formatterp)
# add the handlers to the logger
logger_palissy.addHandler(fhp)
logger_palissy.addHandler(shp)


loggerGps = logging.getLogger('inventaire.GPS')

loggerInsee = logging.getLogger('inventaire.Insee')

class Accessoires(list):
    """
    Liste d'accessoires
    Un accessoire est décrit par une chaîne, qui normalement doit respecter le config.json de portail.
    """
    pass

class OrgueInventaire(object):
    """
    Orgue de l'inventaire national.
    """
    entete = ['Codification',
              'Commune',
              'Edifice',
              'Edifice_standard',
              'Info_edifice',
              'Codification_edifice',
              'Nom_departement',
              'Code_depertament',
              'Nom_region',
              'Code_insee',
              'Commune_insee',
              'Ancienne_commune',
              'Adresse',
              'Désignation',
              'Livre',
              'Pages_pdf',
              'Pages_livre',
              'Pages_livre_complement',
              'Commentaire',
              'Log',
              'Site_ref',
              'Latitude',
              'Longitude',
              'OSM_type',
              'OSM_id',
              'OSM_latitude',
              'OSM_longitude',
              'Orgbase_manu',
              'Orgbase_commune',
              'Orgbase_auto',
              'Orgbase_desc',
              'Orgbase_edifice',
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
              ]

    def __init__(self, _liste):
        self.codification = _liste[0]
        self.commune = _liste[1]
        self.edifice = _liste[2]
        self.edifice_standard = _liste[3]
        self.is_edificestandard = _liste[4]
        self.codification_edifice = _liste[5]
        self.nomdepartement = _liste[6]
        self.code_departement = _liste[7]
        self.nomregion = _liste[8]
        self.code_insee = _liste[9]
        self.commune_insee = _liste[10]
        self.ancienne_commune = _liste[11]
        self.adresse = _liste[12]
        self.designation = _liste[13]
        self.livre = _liste[14]
        self.pages_pdf = _liste[15]
        self.pages_livre = _liste[16]
        self.pages_livre_complement = _liste[17]
        self.commentaire = _liste[18]
        self.log = _liste[19]
        self.site_ref = _liste[20]
        self.latitude = _liste[21]
        self.longitude = _liste[22]
        self.osm_type = _liste[23]
        self.osm_id = _liste[24]
        self.osm_lat = _liste[25]
        self.osm_lon = _liste[26]
        self.orgbase_manu = _liste[27]
        self.orgbase_commune = _liste[28]
        self.orgbase_auto = _liste[29]
        self.orgbase_desc = _liste[30]
        self.orgbase_edifice = _liste[31]
        self.orgbase_facteurs = _liste[32]
        self.orgbase_minicomposition = _liste[33]
        self.orgbase_edifice_standard = _liste[34]
        self.orgbase_edifice_log = _liste[35]
        self.orgbase_commune_insee = _liste[36]
        self.reference_palissy = _liste[37].split(',')
        self.denomination_palissy = _liste[38]
        self.edifice_palissy = _liste[39]
        self.protection_palissy = _liste[40]
        self.resume = _liste[41]
        self.proprietaire = _liste[42]
        self.organisme = _liste[43]
        self.lien_reference = _liste[44]
        self.is_polyphone = _liste[45]
        self.etat = _liste[46]
        self.elevation = _liste[47]
        self.buffet = _liste[48]
        self.console = _liste[49]
        self.commentaire_admin = _liste[50]
        self.diapason = _liste[51]
        self.sommiers = _liste[52]
        self.soufflerie = _liste[53]
        self.transmission_notes = _liste[54]
        self.transmission_commentaire = _liste[55]
        self.tirage_jeux = _liste[56]
        self.tirage_commentaire = _liste[57]
        self.commentaire_tuyauterie = _liste[58]
        self.evenements = _liste[59]
        self.accessoires = Accessoires(_liste[60])
        if _liste[60] != '':
            self.accessoires = _liste[60].split(',')
        else:
            self.accessoires = None
        self.claviers = _liste[61]
        self.images = _liste[62]
        return

    def __repr__(self):
        return '{} {}'.format(self.commune, self.edifice)

    def to_record(self):
        champs = [self.codification,
                  self.commune,
                  self.edifice,
                  self.edifice_standard,
                  self.is_edificestandard,
                  self.codification_edifice,
                  self.nomdepartement,
                  self.code_departement,
                  self.nomregion,
                  self.code_insee,
                  self.commune_insee,
                  self.ancienne_commune,
                  self.adresse,
                  self.designation,
                  self.livre,
                  self.pages_pdf,
                  self.pages_livre,
                  self.pages_livre_complement,
                  self.commentaire,
                  self.log,
                  self.site_ref,
                  self.latitude,
                  self.longitude,
                  self.osm_type,
                  self.osm_id,
                  self.osm_lat,
                  self.osm_lon,
                  self.orgbase_manu,
                  self.orgbase_commune,
                  self.orgbase_auto,
                  self.orgbase_desc,
                  self.orgbase_edifice,
                  self.orgbase_facteurs,
                  self.orgbase_minicomposition,
                  self.orgbase_edifice_standard,
                  self.orgbase_edifice_log,
                  self.orgbase_commune_insee,
                  ",".join(self.reference_palissy),
                  self.denomination_palissy,
                  self.edifice_palissy,
                  self.protection_palissy,
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
                  self.evenements,
                  ",".join(self.accessoires),
                  self.claviers,
                  self.images,
                  ]
        record = ';'.join(champs)
        return record

    def to_dict(self):
        """
        TODO: Ecraser lien_reference par site_ref
        TODO: l'API sort id
        TODO: l'API sort updated_by_user
        TODO: l'API sort url
        TODO : diapason sort null (à modifier dans portail ?)
        TODO : ancienne_commune sort null (à modifier dans portail ?)
        TODO : elevation sort null
        TODO : etat sort null
        TODO : latitude, longitude sort null
        TODO : organisme null
        TODO : osm_id, osm_type null
        TODO : references_palissy null
        TODO : tirages et transmissions null
        TODO: Champs non exportés en JSON :

            self.adresse
            self.commune_insee,
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
            self.orgbase_edifice,
            self.orgbase_facteurs,
            self.orgbase_minicomposition,
            self.orgbase_edifice_standard,
            self.orgbase_edifice_log,
            self.orgbase_commune_insee,

            self.site_ref (a supprimer)

            self.log


            self.denomination_palissy,
            self.edifice_palissy,
            self.protection_palissy,
            self.accessoires,

        """
        dict_orgue = dict()
        dict_orgue = {
            "codification": self.codification,
            "designation": self.designation,
            "is_polyphone": self.is_polyphone,
            "elevation": self.elevation,
            "etat": self.etat,
            "proprietaire": self.proprietaire,
            "commune": self.commune,
            "ancienne_commune": self.ancienne_commune,
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
            "references_palissy": ",".join(self.reference_palissy),
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
            "evenements": [],
            "images": [],
            "fichiers": [],
            }
        if self.accessoires is not None:
            dict_orgue["accessoires"] = self.accessoires
        else:
            dict_orgue["accessoires"] = []
        return dict_orgue

    def standardiser_edifice(self):
        """
        standardiser_edifice = detecter_type_edifice + corriger_nom_edifice
        :return:
        """
        if self.edifice != '':
            edifice_denomination_corrigee = utilsorgues.detecter_type_edifice(self.edifice)
            self.edifice_standard, self.is_edificestandard =\
                utilsorgues.corriger_nom_edifice(edifice_denomination_corrigee, self.commune)
        return

    def codifier_edifice(self):
        """
        codifier_edifice = detecter_type_edifice + corriger_nom_edifice + codifier_edifice
        :return:
        """
        if self.edifice_standard != '':
            self.codification_edifice = utilsorgues.codification.codifie_edifice(self.edifice_standard)
        return

    def codifier_orgue(self):
        self.codification = utilsorgues.codifier_instrument(self)

    def verifier_existence_insee(self, communes_francaises, regions_francaises):
        communes_possibles = None
        #
        # Recherche exacte de la commune
        try:
            communes_possibles = communes_francaises[self.commune]
        except KeyError:
            pass
        #
        # Choix de la commune en fixant le département
        if communes_possibles is not None:
            commune_trouvee = None
            for commune in communes_possibles:
                if commune.nomdepartement == self.nomdepartement:
                    commune_trouvee = commune
            #
            if commune_trouvee is not None:
                # Si la commune est de pleins droits :
                if commune_trouvee.statut == 'ACTUELLE':
                    self.code_insee = commune_trouvee.code_insee
                    self.commune_insee = commune_trouvee.nom
                # S'il s'agit d'une commune associée ou déléguée, on renvoie le nom de la commune chef-lieu.
                elif commune_trouvee.statut == 'ASSOCIEE' or commune_trouvee.statut == 'DELEGUEE':
                    # Mise à jour de l'ancienne commune
                    self.code_insee = commune_trouvee.rattachement
                    self.commune_insee = communes_francaises[commune_trouvee.rattachement].nom
                    if self.ancienne_commune == '':
                        self.ancienne_commune = self.commune
                        loggerInsee.info("COMMUNE_TROUVEE ASSOCIEE OU DELEGUEE : {} {} -> {}"
                                         .format(self.nomdepartement,
                                                 self.commune,
                                                 self.commune_insee))
                    else:
                        loggerInsee.error("ANCIENNE COMMUNE DEJA RENSEIGNEE : {}".format(self.ancienne_commune))
                        if self.ancienne_commune != self.commune:
                            loggerInsee.critical("Conflit ancienne commune <{}> et nom de commune associée ou déléguée <{}>"
                                                 .format(self.ancienne_commune, self.commune))
                # S'il s'agit d'une commune périmée.
                elif commune_trouvee.statut == 'PERIMEE':
                    loggerInsee.error("COMMUNE_TROUVEE MAIS PERIMEE : {} {}".format(self.nomdepartement, self.commune))
                #
                # Ajout de la région:
                self.nomregion = regions_francaises[commune_trouvee.coderegion].nomenclair
            else:
                loggerInsee.critical("MAIS COMMUNE DANS UN AUTRE DEPARTEMENT : {} {} {}".format(self.nomdepartement,
                                                                                                self.commune,
                                                                                                communes_possibles))
        else:
            loggerInsee.fatal("COMMUNE_NON_TROUVEE : {} {}".format(self.nomdepartement, self.commune))
        return


class OrguesInventaire(list):
    """
    Index orgelbase.nl
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
                    # Les champs manquants sont fixés à une chaîne vide :
                    if len(champs) == 24:
                        orgue = OrgueInventaire(champs + (13*['']))
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

    def print_resume(self):
        self._ensemble_communes = set([orgue.commune for orgue in self])
        loggerInventaire.info("L'inventaire contient {} orgues, dans {} communes."
                              .format(len(self), len(self._ensemble_communes)))

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
        departements = utilsorgues.codegeographique.Departements()
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
        for orgue in self:
            orgue.codifier_orgue()

    def verifier_existences_insee(self):
        communes_francaises = utilsorgues.codegeographique.Communes()
        regions_francaises = utilsorgues.codegeographique.Regions()
        for orgue in self:
            orgue.verifier_existence_insee(communes_francaises, regions_francaises)

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
            # Créer un dico comme celui des communes et taper dedans.
            print(orgue)
            pass

    def mapper_palissypop_sur_inventaire(self, fic_palissy):
        """
        Cherche à associer à un orgue de l'inventaire sa référence Palissy.
        :param fic_palissy: fichier CSV exporté de Palissy
        :return:
        # FIXME: Gestion des accents é sur majuscule.
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
        #
        # On calcule les codes d'édifice pour Palissy:
        for objet_palissy in base_palissy:
            edifice_palissy_denomination_corrigee = utilsorgues.detecter_type_edifice(objet_palissy.EDIF)
            edifice_palissy_standard, info_edifice_palissy =\
                utilsorgues.corriger_nom_edifice(edifice_palissy_denomination_corrigee, objet_palissy.COM)
            objet_palissy.code_edifice = utilsorgues.codification.codifie_edifice(edifice_palissy_standard)
            logger_palissy.info("Codification de l'édifice de l'orgue Palissy {} {}"
                                .format(objet_palissy.code_edifice, objet_palissy))
        #
        # Filtrage de la base Palissy pour ne pas chercher les références déjà présentes.
        ref_palissy_deja_presentes = sum([orgue_i.reference_palissy for orgue_i in self],[])
        base_palissy_filtree = [orgue_pal for orgue_pal in base_palissy if orgue_pal.REF not in ref_palissy_deja_presentes]
        #
        # Début de la recherche pour chaque orgue Palissy filtrée:
        for objet_palissy in base_palissy_filtree:
            # FIXME : garder les accents dans Palissy.
            logger_palissy.info("")
            logger_palissy.info("Recherche de l'orgue Palissy {} dans l'inventaire".format(objet_palissy))
            # Réduction du nom de l'édifice Palissy
            orgue_palissy_edifice_standard = utilsorgues.reduire_edifice(objet_palissy.EDIF)
            # Début recherche
            orgues_trouves_dans_edifice = []
            # Buffer pour les traces débug à n'afficher qu'en cas d'échec de recherche :
            traces = []
            for orgue_inventaire in self:
                # Initialisation de l'attribut références Palissy
                orgue_inventaire_edifice_standard = utilsorgues.simplifier_nom_edifice(
                    orgue_inventaire.edifice_standard)
                # Si la commune est Paris,  on tente de trouver l'édifice :
                if objet_palissy.COM[:6] == 'Paris ' and orgue_inventaire.code_insee == '75056':
                    logger_palissy.info("Paris")
                    traces.append("Palissy    : {}".format(
                        orgue_palissy_edifice_standard.replace('catholique-','')))
                    traces.append("Inventaire : {}, {}".format(
                        orgue_inventaire_edifice_standard.replace('é','e').replace('è','e'), orgue_inventaire.designation))
                    # Si l'édifice est le même
                    if orgue_inventaire_edifice_standard.replace('é','e').replace('è','e') == orgue_palissy_edifice_standard.replace('catholique-','').replace('é','e').replace('è','e'):
                        orgues_trouves_dans_edifice.append(orgue_inventaire)
                # Si la commune correspond, on tente de trouver l'édifice :
                elif objet_palissy.INSEE == orgue_inventaire.code_insee:
                    logger_palissy.info("Code INSEE Palissy trouvé dans l'inventaire.")
                    traces.append("Palissy    : {}".format(
                        orgue_palissy_edifice_standard.replace('catholique-','')))
                    traces.append("Inventaire : {}, {}".format(
                        orgue_inventaire_edifice_standard.replace('é','e').replace('è','e'), orgue_inventaire.designation))
                    # Si l'édifice est le même
                    if orgue_inventaire_edifice_standard.replace('é','e').replace('è','e') == orgue_palissy_edifice_standard.replace('catholique-','').replace('é','e').replace('è','e'):
                        orgues_trouves_dans_edifice.append(orgue_inventaire)
                # Sinon on cherche dans la commune associée/déléguée (fusion de communes, etc.)
                # FIXME : a minima ajouter vérification du département et sortir un WARN !
                elif objet_palissy.COM in orgue_inventaire.ancienne_commune:
                    logger_palissy.warning("Code INSEE Palissy non trouvé dans l'inventaire mais ancienne commune si. : {}.".format(objet_palissy.INSEE))
                    traces.append("Palissy    : {}".format(
                        orgue_palissy_edifice_standard.replace('catholique-','')))
                    traces.append("Inventaire : {}, {}".format(
                        orgue_inventaire_edifice_standard.replace('é','e').replace('è','e'), orgue_inventaire.designation))
                    # Si l'édifice est le même
                    if orgue_inventaire_edifice_standard.replace('é','e').replace('è','e') == orgue_palissy_edifice_standard.replace('catholique-','').replace('é','e').replace('è','e'):
                        orgues_trouves_dans_edifice.append(orgue_inventaire)
                else:
                    #logger_palissy.error("Code INSEE Palissy non trouvé dans l'inventaire, commune dans le champ autre_commune non plus !")
                    pass
                # En dernier recours, on ne compare que les codifications
                # elif objet_palissy.code_edifice == utilsorgues.codification.codifie_edifice(orgue_inventaire.edifice_standard):
                #     traces.append("Palissy    : {}".format(
                #         objet_palissy.code_edifice))
                #     traces.append("Inventaire : {}".format(
                #         orgue_inventaire.codification))
            #
            # Fin de boucle
            # - Si recherche fructueuse :
            if len(orgues_trouves_dans_edifice) == 1:
                nombre_orgues_mappes += 1
                logger_palissy.info("Cet objet Palissy {} a été trouvé dans l'inventaire ! Correspondance possible !"
                                   .format(objet_palissy))
                # Recopie de la référence Palissy dans l'inventaire, si elle n'est pas déjà présente.
                if objet_palissy.REF not in orgues_trouves_dans_edifice[0].reference_palissy:
                    orgues_trouves_dans_edifice[0].reference_palissy.append(objet_palissy.REF)
            # - Si plusieurs orgues dans un même édifice, il faut descendre jusqu'à la dénomination :
            elif len(orgues_trouves_dans_edifice) > 1:
                logger_palissy.warning("Plus d'un édifice de l'inventaire correspondant à l'objet dans Palissy {} !"
                                     .format(objet_palissy))
                for orgue in orgues_trouves_dans_edifice:
                    logger_palissy.debug("Orgue trouvé dans l'édifice".format(orgue))
                    if orgue.designation == 'G.O.'\
                            and nettoyer_titre_courant_palissy(objet_palissy.TICO) in ['orgue de tribune', "tribune d'orgue"]:
                        nombre_orgues_mappes += 1
                        logger_palissy.info("L'orgue Palissy {} a été trouvé dans l'inventaire !"
                                            .format(objet_palissy))
                        # Ajout de la référence si elle n'est pas déjà présente
                        if objet_palissy.REF not in orgue.reference_palissy:
                            orgue.reference_palissy.append(objet_palissy.REF)
                    if orgue.designation == 'O.C.'\
                            and nettoyer_titre_courant_palissy(objet_palissy.TICO) in ['orgue de choeur']:
                        nombre_orgues_mappes += 1
                        logger_palissy.info("L'orgue Palissy {} a été trouvé dans l'inventaire !"
                                            .format(objet_palissy))
                        # Ajout de la référence si elle n'est pas déjà présente
                        if objet_palissy.REF not in orgue.reference_palissy:
                            orgue.reference_palissy.append(objet_palissy.REF)
            else:
                logger_palissy.error("")
                logger_palissy.error("Orgue Palissy non trouvé dans l'inventaire: {}"
                                     .format(objet_palissy))
                pm_possibles = ",".join(edifices_refs[objet_palissy.INSEE + '---' + objet_palissy.EDIF])
                logger_palissy.error("PM possibles : {}".format(pm_possibles))
                for trace in traces:
                    logger_palissy.error("   " + trace)
        logger_palissy.info("Fin de correspondance Inventaire vs. Palissy, {}/{} orgues mappés."
                           .format(nombre_orgues_mappes, len(base_palissy)))

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
                if orgue.commune_insee == orgue_picard[1]:
                    # Si pas d'édifice, on ne raffine pas.
                    if orgue_picard[2] is None:
                        # On n'écrase pas les données déjà présentes.
                        if (orgue.longitude, orgue.latitude) == ('',''):
                            orgue.longitude = orgue_picard[3]
                            orgue.latitude = orgue_picard[4]
                            loggerInventaire.info('Orgue picard mappé : {}'
                                                  .format(str(orgue_picard)))
                    # Si un édifice est présent, et trouvé dans l'inventaire :
                    elif orgue_picard[2] == orgue.edifice:
                        # On n'écrase pas les données déjà présentes.
                        if (orgue.longitude, orgue.latitude) == ('',''):
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
                #way;23100587;Église Saint-Louis;45.18977948571429;5.725901744642857;Grenoble;38185;
                objet_osm = ligne.rstrip('\r\n').split(';')
                data_osm.append(objet_osm)
        # Boucle sur les orgues
        compteur = 0
        for orgue in self:
            # Boucle de recherche dans les objets OSM (qui représentent un édifice)
            for edifice_osm in data_osm:
                # La recherche se fait sur les codes INSEE ET nom d'édifice complet
                if orgue.code_insee == edifice_osm[6] and\
                    orgue.edifice == edifice_osm[2].replace('Église','église'):
                    compteur += 1
                    loggerInventaire.info("Edifice OSM trouvé {} {} {}".format(orgue.commune_insee, orgue.edifice, str(compteur)))
                    orgue.osm_type = edifice_osm[0]
                    orgue.osm_id = edifice_osm[1]
                    orgue.osm_lat = edifice_osm[3]
                    orgue.osm_lon = edifice_osm[4]

    def rechercher_gps_osm_depuis_id(self):
        for orgue in self:
            if orgue.osm_type and orgue.osm_id:
                pass
                #TODO : Aller chercher XML sur OSM, le lire, calculer barycentre si way ou relation.

    def ecraser_gps_par_osm(self):
        for orgue in self:
            if orgue.osm_type and orgue.osm_id:
                orgue.latitude = orgue.osm_lat
                orgue.longitude = orgue.osm_lon

    def correction_directe_nom_edifice(self):
        for orgue in self:
            # Correction des édifices Saint ou Sainte sans dénomination : on écrit 'église' par défaut.
            if orgue.edifice[:6] == 'Saint-' or orgue.edifice[:7] == 'Sainte-':
                loggerInventaire.info('Correction directe édifice : Saint ou Sainte sans préfixe église {}'.format(orgue))
                orgue.edifice = 'église {}'.format(orgue.edifice)
            # Correction de la dénomination 'église paroissiale' en 'église'.
            if orgue.edifice.lower() == 'église paroissiale':
                loggerInventaire.info('Correction directe édifice : église paroissiale devient église {}'.format(orgue))
                orgue.edifice = 'église'
            # Correction de la casse MIXTE:
            if 'MIXTE' in orgue.edifice:
                loggerInventaire.info('Correction directe édifice : église MIXTE devient église mixte {}'.format(orgue))
                orgue.edifice = orgue.edifice.replace('MIXTE', 'mixte')

    def detecter_noms_edifice_majuscules(self):
        for orgue in self:
            if re.search(".*[A-Z][A-Z].*", orgue.edifice):
                loggerInventaire.warning("Pour cet orgue l'édifice est en majuscules : {}".format(orgue))

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
                utilsorgues.generiques.supprimer_accents(
                    utilsorgues.correcteurorgues.simplifier_nom_edifice(orgue.edifice_standard))
            edifices_possibles = edifices_par_commune.get(orgue.code_insee, None)
            # Si la commune est répertoriée dans MessesInfo :
            if edifices_possibles is not None:
                # Recherche par nom d'édifice :
                edifice_trouve = None
                for edifice in edifices_possibles:
                    # Dégénérescence du nom de l'édifice :
                    edifice_simplifie = utilsorgues.generiques.supprimer_accents(
                        utilsorgues.correcteurorgues.simplifier_nom_edifice(edifice.edifice_standard))
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


if __name__ == '__main__':
    loggerInventaire.info('Démarrage du script')
    mon_inventaire = OrguesInventaire('../../98-indexes/indexFrance-inventairedesorgues.csv', True)
    mon_inventaire.print_resume()
    mon_inventaire.liste_edifices_absents()
    #
    # print(mon_inventaire.denombrer_par_commune()["La Flèche, Sarthe"])
    # mon_inventaire.to_console()
    #
    ##mon_inventaire.verifier_existences_insee()
    ##mon_inventaire.codifier_departements()
    #
    #mon_inventaire.standardiser_edifices()#dont corrections casse, etc.
    ##mon_inventaire.rechercher_coordonnees_gps()
    #
    ##mon_inventaire.mapper_coordonnees_gps_picardie('../97-data/', ['aisne', 'somme', 'oise'])
    # print(mon_inventaire[4].reference_palissy)
    ##mon_inventaire.mapper_palissypop_sur_inventaire('../97-data/export-pop-palissy.csv')
    #
    ##mon_inventaire.codifier_orgues()
    #
    ####mon_inventaire.rechercher_donnees_osm('../97-data/simple-FranceMetropole.csv')
    #mon_inventaire.rechercher_gps_osm_depuis_id()

    #mon_inventaire.ecraser_gps_par_osm()

    #mon_inventaire.correction_directe_nom_edifice()
    #mon_inventaire.codifier_edifices()

    #mon_inventaire.detecter_noms_edifice_majuscules()

    #mon_inventaire.to_csv('../../98-indexes/indexFrance-inventairedesorgues.csv')
    mon_inventaire.to_json('../../98-indexes/indexFrance-inventairedesorgues.json', limit=1)
    loggerInventaire.info('Fin du script')
