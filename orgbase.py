"""
Classes pour manipulation des orgues de orgbase.nl
"""
import utilsorgues
import logging


logger_orgbase = logging.getLogger('orgbase')
logger_orgbase.setLevel(logging.DEBUG)
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
logger_orgbase.addHandler(fh)
logger_orgbase.addHandler(ch)


class OrgueOrgbase(object):
    """
    Orgue tel que vu dans les index de orgbase.nl
    """
    def __init__(self, _liste):
        self.nomdepartement = _liste[0]
        self.lien = _liste[1]
        self.desc = _liste[2]
        self.commune = _liste[3]
        self.edifice = _liste[4]
        self.facteurs = _liste[5]
        self.minicomposition = _liste[6]
        self.edifice_standard = ''
        self.info_edifice = ''
        self.commune_insee = ''
        self.code_insee = ''
        self.adresse = ''
        return

    def __repr__(self):
        return '{} {}'.format(self.commune, self.edifice)

    def to_record(self):
        """
        Sérialisation.
        :return: enregistrement (str)
        """
        champs = [self.nomdepartement,
                  self.lien,
                  self.desc,
                  self.commune,
                  self.edifice,
                  self.facteurs,
                  self.minicomposition,
                  self.edifice_standard,
                  self.info_edifice,
                  self.commune_insee,
                  self.code_insee,
                  self.adresse]
        record = ';'.join(champs)
        return record

    def standardiser_edifice(self):
        """
        Dégénérescence du nom de l'édifice.
        :return:
        """
        edifice_denomination_corrigee = utilsorgues.corriger_denomination_edifice(self.edifice)
        self.edifice_standard, self.info_edifice =\
            utilsorgues.corriger_nom_edifice(edifice_denomination_corrigee, self.commune)
        # print('{} -> {}'.format(self.edifice, self.edifice_standard))
        return

    def verifier_existence_insee(self, communes_francaises):
        communes_possibles = []
        #
        # print("\nDEBUT RECHERCHE COMMUNE : {} {}".format(self.nomdepartement, self.commune))
        #
        # Recherche exacte de la commune
        try:
            communes_possibles = communes_francaises[utilsorgues.supprimer_accents(self.commune)]
            # print('Accès au dictionnaire du nom de commune : orthographe exacte.')
        # A défaut, recherche approchée de la commune
        except KeyError:
            communes_possibles = communes_francaises.get(utilsorgues.supprimer_accents(self.commune).replace(' ', '-'))
            if communes_possibles is not []:
                pass
                # logger_orgbase.debug('Accès au dictionnaire du nom de commune : orthographe modifiée. {}, {}'
                # .format(self.commune,self.nomdepartement))
            else:
                logger_orgbase.error('Accès au dictionnaire du nom de commune : abandon. {}, {}'
                      .format(self.commune, self.nomdepartement))
                """
                communes_possibles = communes_francaises.get(
                    utilsorgues.upper_sans_accent(utilsorgues.supprimer_accents(self.commune).replace(' ', '-')))
                if communes_possibles is None:
                    logger_orgbase.debug('Accès au dictionnaire du nom de commune : abandon.')
                else:
                    logger_orgbase.debug('Accès au dictionnaire du nom de commune : orthographe modifiée 2.')
                """
        #
        # Choix de la commune en fixant le département
        if communes_possibles is not []:
            commune_trouvee = None
            for commune in communes_possibles:
                if commune.nomdepartement == self.nomdepartement:
                    commune_trouvee = commune
                #
                if commune_trouvee is not None:
                    # Si la commune est de pleins droits :
                    if commune_trouvee.statut == 'ACTUELLE':
                        # print("INFO : COMMUNE_TROUVEE : {} {}".format(self.nomdepartement, self.commune))
                        self.code_insee = commune_trouvee.code_insee
                        self.commune_insee = commune_trouvee.nom
                    # S'il s'agit d'une commune associée ou déléguée, on renvoie le nom de la commune chef-lieu.
                    elif commune_trouvee.statut == 'ASSOCIEE' or commune_trouvee.statut == 'DELEGUEE':
                        # Mise à jour de l'adresse
                        self.code_insee = commune_trouvee.rattachement
                        self.commune_insee = communes_francaises[commune_trouvee.rattachement].nom
                        if self.adresse == '':
                            self.adresse = self.commune
                            logger_orgbase.info(
                                "COMMUNE_TROUVEE ASSOCIEE OU DELEGUEE : {} {} -> {}".format(self.nomdepartement,
                                                                                                   self.commune,
                                                                                                   self.commune_insee))
                        else:
                            logger_orgbase.error("ADRESSE DEJA RENSEIGNEE : {}".format(self.adresse))
                    # S'il s'agit d'une commune périmée.
                    elif commune_trouvee.statut == 'PERIMEE':
                        logger_orgbase.error("COMMUNE_TROUVEE MAIS PERIMEE : {} {}".format(self.nomdepartement, self.commune))
                else:
                    logger_orgbase.error("MAIS COMMUNE DANS UN AUTRE DEPARTEMENT : {} {} {}".format(self.nomdepartement,
                                                                                             self.commune,
                                                                                             communes_possibles))
        else:
            logger_orgbase.error("COMMUNE_NON_TROUVEE : {} {}".format(self.nomdepartement, self.commune))
        return


class OrguesOrgelbase(list):
    """
    Index orgelbase.nl
    """
    def __init__(self, fic_csv):
        super().__init__()
        with open('./{}'.format(fic_csv), 'r', encoding='iso-8859-1') as fic_totale:
            for ligne in fic_totale:
                orgue = OrgueOrgbase(ligne.rstrip('\r\n').split(';'))
                self.append(orgue)
        return

    def to_console(self):
        for item in self:
            print(item)
        return None

    def to_list(self):
        enregistrements = [item.to_record() for item in self]
        return enregistrements

    def to_csv(self, nom_fic_out):
        with open('./{}'.format(nom_fic_out), 'w', encoding='iso-8859-1') as fic_out:
            for item in self.to_list():
                fic_out.write(item + '\n')
        return None

    def standardiser_edifices(self):
        for orgue in self:
            orgue.standardiser_edifice()

    def verifier_existences_insee(self):
        communes_francaises = utilsorgues.codegeographique.Communes(utilsorgues.supprimer_accents)
        for orgue in self:
            orgue.verifier_existence_insee(communes_francaises)

    def to_dict(self):
        """
        Construit un dictionnaire clés: code_INSEE, valeurs: [liste des édifices de cette commune].
        :return:
        """
        orgues_par_code_insee = {}
        for orgue in self:
            if orgue.code_insee not in orgues_par_code_insee.keys():
                orgues_par_code_insee[orgue.code_insee] = [orgue]
            else:
                orgues_par_code_insee[orgue.code_insee].append(orgue)
        return orgues_par_code_insee


if __name__ == '__main__':
    index = OrguesOrgelbase('orgbase - correction2.csv')
    # index.to_console()
    index.standardiser_edifices()
    index.verifier_existences_insee()
    index.to_csv('orgbase3-vrai-insee.csv')
