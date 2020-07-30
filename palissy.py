"""
Gestion des objets contenus dans des extractions CSV de Palissy.
Plusieurs formats d'export sont gérés suivant l'application source de l'export.

data.culture.gouv :
https://data.culture.gouv.fr/explore/dataset/liste-des-objets-mobiliers-propriete-publique-classes-au-titre-des-monuments-/api/?dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6Imxpc3RlLWRlcy1vYmpldHMtbW9iaWxpZXJzLXByb3ByaWV0ZS1wdWJsaXF1ZS1jbGFzc2VzLWF1LXRpdHJlLWRlcy1tb251bWVudHMtIiwib3B0aW9ucyI6e319LCJjaGFydHMiOlt7ImFsaWduTW9udGgiOnRydWUsInR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQ09VTlQiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjYzQzYTJmIn1dLCJ4QXhpcyI6InJlZyIsIm1heHBvaW50cyI6NTAsInNvcnQiOiIifV0sInRpbWVzY2FsZSI6IiIsImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9

POP : https://pop.culture.gouv.fr/search/list?mainSearch=%22orgue%20landivisiau%22
POP : https://pop.culture.gouv.fr/notice/palissy/PM29002961

URI Palissy : 'http://www2.culture.gouv.fr/public/mistral/palissy_fr?ACTION=CHERCHER&FIELD_1=REF&VALUE_1={}'.format(PM74000046)
URI Mérimée : 'http://www2.culture.gouv.fr/public/mistral/merimee_fr?ACTION=CHERCHER&FIELD_8=REF&VALUE_8={}'.format(PA00094810)

<N> <A HREF="javascript:merimee('PA00094808')"><IMG SRC="/documentation/icones/pcmer.gif" border="0" title="édifice"></A></N></FONT>
"""

import csv


class OrguePalissyOpenData(object):
    """
    Orgue dans Palissy POP open data.
    REG;DPT;COM;Titre courant;Type d'objet;AUTR;MATR;EDIF;SCLE;DPRO;INSEE;STAT;REF
    """
    def __init__(self, _liste):
        [self.REG,
         self.DPT,
         self.COM,
         self.titre_courant,
         self.TypeObjet,
         self.AUTR,
         self.MATR,
         self.EDIF,
         self.SCLE,
         self.DPRO,
         self.INSEE,
         self.STAT,
         self.REF] = _liste
        return

    def __repr__(self):
        return '<object OrguePalissyOpenData {} {} {} {} {} {}>'\
            .format(self.REF, self.DPT, self.COM, self.INSEE, self.EDIF, self.titre_courant)


class OrguesPalissyOpenData(list):
    """
    Base Palissy POP open data(data.culture.gouv.fr)
    """
    def __init__(self, fic_csv):
        """
        Importe un fichier CSV extrait de la base Palissy.
        :argument: fic_csv : fichier CSV extrait de Palissy open data
        :return:
        """
        super().__init__()
        with open('./{}'.format(fic_csv), 'r', encoding='utf-8') as fic_totale:
            palissy_reader = csv.reader(fic_totale, delimiter=';', quotechar='"')
            for i, ligne in enumerate(palissy_reader):
                if i != 0:
                    orgue = OrguePalissyOpenData(ligne)
                    self.append(orgue)
        return

    def to_console(self):
        for item in self:
            print(item)
        return None

    def to_dict_edifices_refs(self):
        edifices_pm = dict()
        for item_palissy in self:
            insee_edif = item_palissy.INSEE + '---' + item_palissy.EDIF
            if insee_edif not in edifices_pm.keys():
                edifices_pm[insee_edif] = [item_palissy.REF]
            else:
                valeur = edifices_pm[insee_edif]
                valeur = valeur + [item_palissy.REF]
                edifices_pm[insee_edif] = valeur
        return edifices_pm

    def corriger_insee(self):
        # FIXME dans l'export Palissy OpenData
        for objet_palissy in self:
            # Correction des références INSEE à quatre chiffres seulement.
            if len(objet_palissy.INSEE) == 4:
                objet_palissy.INSEE = '0' + objet_palissy.INSEE


class OrguePalissyPop2020(object):
    """
    Orgue dans Palissy exporté via POP back-office, version 2020.
    Spécificité : Tous les champs et non que les champs open data.
    """
    # TODO : Typage ?
    def __init__(self, _liste):
        [self.REF,
         self.POP_ARRETE_PROTECTION,
         self.POP_COMMENTAIRES,
         self.POP_CONTIENT_GEOLOCALISATION,
         self.POP_COORDINATES_POLYGON,
         self.POP_COORDONNEES,
         self.POP_DOSSIER_PROTECTION,
         self.POP_DOSSIER_VERT,
         self.POP_FLAGS,
         self.POP_IMPORT,
         self.ACQU,
         self.ADRS,
         self.ADRS2,
         self.AFIG,
         self.AIRE,
         self.APPL,
         self.ATEL,
         self.AUTP,
         self.AUTR,
         self.BASE,
         self.BIBL,
         self.CANT,
         self.CATE,
         self.COM,
         self.COM2,
         self.CONTACT,
         self.CONTIENT_IMAGE,
         self.COOR,
         self.COORM,
         self.COPY,
         self.DATE,
         self.DBOR,
         self.DENO,
         self.DENQ,
         self.DEPL,
         self.DESC,
         self.DIMS,
         self.DMAJ,
         self.DMIS,
         self.DOMN,
         self.DOSADRS,
         self.DOSS,
         self.DOSURL,
         self.DOSURLP,
         self.DOSURLPDF,
         self.DPRO,
         self.DPT,
         self.DPT_LETTRE,
         self.EDIF,
         self.EDIF2,
         self.EMPL,
         self.EMPL2,
         self.ETAT,
         self.ETUD,
         self.EXEC,
         self.EXPO,
         self.HIST,
         self.IDAGR,
         self.IMAGE,
         self.IMG,
         self.IMPL,
         self.INSC,
         self.INSEE,
         self.INSEE2,
         self.INTE,
         self.JDAT,
         self.LBASE2,
         self.LIENS,
         self.LIEU,
         self.LMDP,
         self.LOCA,
         self.MANQUANT,
         self.MATR,
         self.MEMOIRE,
         self.MFICH,
         self.MICR,
         self.MOSA,
         self.NART,
         self.NINV,
         self.NOMS,
         self.NUMA,
         self.NUMP,
         self.OBS,
         self.ORIG,
         self.PAPP,
         self.PARN,
         self.PART,
         self.PDEN,
         self.PDIM,
         self.PERS,
         self.PETA,
         self.PHOTO,
         self.PINS,
         self.PINT,
         self.PLOC,
         self.PPRO,
         self.PRECISION_JURIDIQUE,
         self.PREP,
         self.PRODUCTEUR,
         self.PROT,
         self.REFA,
         self.REFE,
         self.REFM,
         self.REFP,
         self.REG,
         self.RENP,
         self.RENV,
         self.REPR,
         self.SCLD,
         self.SCLE,
         self.SCLX,
         self.SOUR,
         self.STAD,
         self.STAT,
         self.STRU,
         self.THEM,
         self.TICO,
         self.TITR,
         self.TOUT,
         self.VIDEO,
         self.VOLS,
         self.WADRS,
         self.WCOM,
         self.WEB,
         self.WRENV,
         self.ZONE] = _liste
        # Correction département :
        if len(self.DPT) < 2:
            self.DPT = '0' + self.DPT
        # Correction INSEE :
        if len(self.INSEE) < 5:
            self.INSEE = '0' + self.INSEE
        return

    def __repr__(self):
        return '<object OrguePalissyPop2000 {} {} {} {} {} {}>'\
            .format(self.REF, self.DPT, self.WCOM, self.INSEE, self.EDIF, self.TICO)


class OrguesPalissyPop(list):
    """
    Base Palissy POP back-office (data.culture.gouv.fr)
    """
    def __init__(self, fic_csv):
        """
        Importe un fichier CSV extrait de la base Palissy.
        :argument: fic_csv : fichier CSV extrait de Palissy via POP back office.
        :return:
        """
        super().__init__()
        with open('./{}'.format(fic_csv), 'r', encoding='utf-8') as fic_totale:
            palissy_reader = csv.reader(fic_totale, delimiter=';', quotechar='"')
            for i, ligne in enumerate(palissy_reader):
                # On saute la première ligne (critères de recherche POP) et la seconde (entête des champs).
                # ou
                # Que l'entête pour les fichiers Palissy POP version 2000
                if i > 0:
                    orgue = OrguePalissyPop2020(ligne)
                    self.append(orgue)
        return

    def to_console(self):
        for item in self:
            print(item)
        return None

    def to_dict_pm(self):
        pms = dict()
        for orgue_palissy in self:
            pms[orgue_palissy.REF] = orgue_palissy
        return pms

    def to_dict_edifices_refs(self):
        """
        Retourne un dictionnaire permettant d'accéder à tous les PM d'un édifice Palissy.
        clés : code_commune_INSEE---edifice_Palissy
        valeurs : liste de PM
        :return:
        """
        edifices_pm = dict()
        for item_palissy in self:
            insee_edif = item_palissy.INSEE + '---' + item_palissy.EDIF
            if insee_edif not in edifices_pm.keys():
                edifices_pm[insee_edif] = [item_palissy.REF]
            else:
                valeur = edifices_pm[insee_edif]
                valeur = valeur + [item_palissy.REF]
                edifices_pm[insee_edif] = valeur
        return edifices_pm

    def corriger_insee(self):
        # FIXME dans l'export Palissy OpenData
        for objet_palissy in self:
            # Correction des références INSEE à quatre chiffres seulement.
            if len(objet_palissy.INSEE) == 4:
                objet_palissy.INSEE = '0' + objet_palissy.INSEE


def recherche_fiche_web_palissy(code_pm_palissy='PM74000046'):
    """
    Recherche et parsing d'une fiche Palissy sur Internet.
    :argument: code PM Palissy de l'objet.
    :return: liste de liens <a> BeautifulSoup
    """
    import requests
    from bs4 import BeautifulSoup
    url_palissy = 'http://www2.culture.gouv.fr/public/mistral/palissy_fr?ACTION=CHERCHER&FIELD_1=REF&VALUE_1={}'\
        .format(code_pm_palissy)
    r = requests.get(url_palissy)
    r.encoding = 'iso-8859-1'
    html_palissy = BeautifulSoup(r.text)
    liens = html_palissy.find_all('a')
    print(liens)
    return liens


if __name__ == "__main__":
    # palissy = OrguesPalissyOpenData('../97-data/orgues-Palissy.csv')
    # palissy.to_console()
    # palissy.to_dict_edifices_refs()['6023---église Santa-Maria-in-Albis']
    palissy_pop = OrguesPalissyPop('../97-data/palissy_20200414_14h14m05s.csv')
    palissy_pop.to_console()
    in_ablis = palissy_pop.to_dict_edifices_refs()['06023---église Santa-Maria-in-Albis']
    print(in_ablis)
