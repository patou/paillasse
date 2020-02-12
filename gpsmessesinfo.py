"""
Classes pour gestions des édifices décrits dans MessesInfo.
"""
import logging
import utilsorgues


loggerGpsmessesinfo = logging.getLogger('gpsmessesinfo')
loggerGpsmessesinfo.setLevel(logging.DEBUG)
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
loggerGpsmessesinfo.addHandler(fh)
loggerGpsmessesinfo.addHandler(ch)


class EdificeMessesInfo(object):
    """
    Edifice tel que pris dans MessesInfo
    """
    def __init__(self, _liste, _num):
        self.departement = _liste[0]
        self.commune = _liste[1][2:-2]
        self.communaute = _liste[2][2:-2]
        self.edifice = _liste[3][2:-2]
        self.latitude = _liste[4]
        self.longitude = _liste[5]
        self.nomdepartement = ''
        self.nomregion = ''
        self.adresse = ''
        self.index = _num
        self.edifice_standard = ''
        self.info_edifice = ''
        self.commune_insee = ''
        self.code_insee = ''
        return

    def __repr__(self):
        return '<Edifice MessesInfo : {}, {}>'.format(self.commune, self.edifice)

    def standardiser_edifice(self):
        edifice_denomination_corrigee = utilsorgues.corriger_denomination_edifice(self.edifice)
        self.edifice_standard, self.info_edifice = \
            utilsorgues.corriger_nom_edifice(edifice_denomination_corrigee, self.commune)
        # print('{} -> {}'.format(self.edifice, self.edifice_standard))
        return

    def verifier_coordonnees_edifice(self):
        if self.longitude == '0.00000000' or self.latitude == '0.00000000':
            loggerGpsmessesinfo.error('COORDONNEE FAUSSE 0.00000000 : {} {}'.format(self.commune, self.edifice))

    def verifier_existence_insee(self, communes_francaises, regions_francaises):
        commune_trouvee = False
        # print("\nDEBUT RECHERCHE COMMUNE : {} {}".format(self.departement, self.commune))
        #
        # Recherche exacte de la commune
        try:
            communes_possibles = communes_francaises[utilsorgues.generiques.upper_sans_accent(self.commune)]
            # print('DEBUG : Accès au dictionnaire du nom de commune : orthographe exacte.')
        # A défaut, recherche approchée de la commune
        except KeyError:
            communes_possibles = communes_francaises.get(
                utilsorgues.generiques.upper_sans_accent(self.commune.replace(' ', '-')))
            if communes_possibles is not None:
                # print('DEBUG : Accès au dictionnaire du nom de commune : orthographe modifiée.')
                pass
            else:
                communes_possibles = communes_francaises.get(
                    utilsorgues.generiques.upper_sans_accent(self.commune.replace(' ', '-')))
                if communes_possibles is not None:
                    # print('DEBUG : Accès au dictionnaire du nom de commune : orthographe modifiée 2.')
                    pass
                else:
                    # print('DEBUG : Accès au dictionnaire du nom de commune : abandon.')
                    pass
        #
        # Choix de la commune en fixant le département
        if communes_possibles is not None:
            commune_trouvee = None
            for commune in communes_possibles:
                if commune.codedepartement == self.departement:
                    commune_trouvee = commune
            #
            if commune_trouvee is not None:
                # Si la commune est de pleins droits :
                if commune_trouvee.statut == 'ACTUELLE':
                    loggerGpsmessesinfo.info("COMMUNE_TROUVEE : {} {}".format(self.nomdepartement, self.commune))
                    self.code_insee = commune_trouvee.code_insee
                    self.commune_insee = commune_trouvee.nom
                # S'il s'agit d'une commune associée ou déléguée, on renvoie le nom de la commune chef-lieu.
                elif commune_trouvee.statut == 'ASSOCIEE' or commune_trouvee.statut == 'DELEGUEE':
                    # Mise à jour de l'adresse
                    self.code_insee = commune_trouvee.rattachement
                    self.commune_insee = communes_francaises[commune_trouvee.rattachement].nom
                    if self.adresse == '':
                        self.adresse = self.commune
                        loggerGpsmessesinfo.info("COMMUNE_TROUVEE ASSOCIEE OU DELEGUEE : {} {} -> {}".format(self.nomdepartement,
                                                                                                 self.commune,
                                                                                                 self.commune_insee))
                    else:
                        loggerGpsmessesinfo.error("ADRESSE DEJA RENSEIGNEE : {}".format(self.adresse))
                # S'il s'agit d'une commune périmée.
                elif commune_trouvee.statut == 'PERIMEE':
                    loggerGpsmessesinfo.error("COMMUNE_TROUVEE MAIS PERIMEE : {} {}".format(self.nomdepartement, self.commune))
                #
                # Ajout de la région:
                self.nomregion = regions_francaises[commune_trouvee.coderegion].nomenclair
            else:
                loggerGpsmessesinfo.error("MAIS COMMUNE DANS UN AUTRE DEPARTEMENT : {} {} {}".format(self.nomdepartement,
                                                                                         self.commune,
                                                                                         communes_possibles))
        else:
            loggerGpsmessesinfo.error("COMMUNE_NON_TROUVEE : {} {}".format(self.nomdepartement, self.commune))
        return

    def to_record(self):
        champs = [str(self.index),
                  self.departement,
                  self.commune,
                  self.communaute,
                  self.edifice,
                  self.latitude,
                  self.longitude,
                  self.nomdepartement,
                  self.nomregion,
                  self.adresse,
                  self.edifice_standard,
                  self.info_edifice,
                  self.commune_insee,
                  self.code_insee]
        record = ';'.join(champs)
        return record


class EdificesMessesInfo(list):
    """
    Edifices tels que pris dans MessesInfo
    """
    def __init__(self, fic_csv):
        super().__init__()
        with open('./{}'.format(fic_csv), 'r', encoding='utf-8') as fic_totale:
            for i, ligne in enumerate(fic_totale):
                if i != 0:  # On ignore l'entête
                    orgue = EdificeMessesInfo(ligne.rstrip('\r\n').split(','), i)
                    self.append(orgue)
        return

    def to_console(self):
        for item in self:
            print(item)
        return None

    def standardiser_edifices(self):
        for orgue in self:
            orgue.standardiser_edifice()

    def verifier_coordonnees(self):
        for orgue in self:
            orgue.verifier_coordonnees_edifice()

    def verifier_existences_insee(self):
        communes_francaises = utilsorgues.codegeographique.Communes(utilsorgues.generiques.upper_sans_accent)
        regions_francaises = utilsorgues.codegeographique.Regions()
        for orgue in self:
            orgue.verifier_existence_insee(communes_francaises, regions_francaises)

    def to_list(self):
        enregistrements = [item.to_record() for item in self]
        return enregistrements

    def to_dict(self):
        """
        Construit un dictionnaire clés: code_INSEE, valeurs: [liste des édifices de cette commune].
        :return:
        """
        edifices_par_code_insee = {}
        for edifice in self:
            if edifice.code_insee not in edifices_par_code_insee.keys():
                edifices_par_code_insee[edifice.code_insee] = [edifice]
            else:
                edifices_par_code_insee[edifice.code_insee].append(edifice)
        return edifices_par_code_insee

    def to_csv(self, nom_fic_out):
        with open('./{}'.format(nom_fic_out), 'w', encoding='utf-8') as fic_out:
            for item in self.to_list():
                fic_out.write(item + '\n')
        return None


if __name__ == '__main__':
    index = EdificesMessesInfo('20181219-Lieux de culte MessesInfo.csv')
    # index.to_console()
    index.standardiser_edifices()
    index.verifier_coordonnees()
    index.verifier_existences_insee()
    print(index.to_dict()['01005'])
    index.to_csv('EdificesMessesInfo.csv')
