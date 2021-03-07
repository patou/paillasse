"""
Script de manipulation des données de l'index des orgues.
"""
import time
import sys

import inventaire


if __name__ == '__main__':

    inventaire.loggerInventaire.info('{} Démarrage du script'.format(time.asctime(time.localtime())))

    if len(sys.argv) == 2:
        PARAM_DEBUG = sys.argv[1]
    else:
        PARAM_DEBUG = None

    if PARAM_DEBUG == 'MAIN_DEBUG':
        pass
        #mon_inventaire = inventaire.OrguesInventaire('../98-indexes/indexFrance.debug.csv', True)
    else:
        mon_inventaire = inventaire.OrguesInventaire('../98-indexes/index.csv', True)
    print(mon_inventaire)
    # print(mon_inventaire.denombrer_par_commune()["La Flèche, Sarthe"])
    # mon_inventaire.to_console()

    # mon_inventaire.liste_edifices_absents()

    # mon_inventaire.codifier_departements()
    # mon_inventaire.verifier_existences_insee()

    # mon_inventaire.detecter_noms_edifice_majuscules()

    #mon_inventaire.standardiser_edifices()  # dont corrections casse, etc.
    # mon_inventaire.correction_directe_nom_edifice()
    # mon_inventaire.fixer_noms_edifices()

    #mon_inventaire.codifier_edifices()
    #mon_inventaire.codifier_orgues()
    #mon_inventaire.fixer_polyphones()
    #mon_inventaire.detecter_doublons_codifsorgues()

    #mon_inventaire.fixer_fichiers()
    mon_inventaire.fixer_sources(reset=True)

    """
    if PARAM_DEBUG == 'PALISSY_DEBUG':
        mon_inventaire.mapper_palissypop_sur_inventaire('../97-data/debugPalissy.csv')
    else:
        mon_inventaire.mapper_palissypop_sur_inventaire('../97-data/palissy_20200414_14h14m05s.csv')
    """

    # mon_inventaire.rechercher_donnees_osm('../97-data/simple-FranceMetropole.csv')
    # mon_inventaire.rechercher_gps_osm_depuis_id()
    # mon_inventaire.rechercher_coordonnees_gps()
    # mon_inventaire.mapper_coordonnees_gps_picardie('../97-data/', ['aisne', 'somme', 'oise'])

    # mon_inventaire.ecraser_gps_par_osm()
    # mon_inventaire.fixer_polyphones()
    # mon_inventaire.fixer_monumentshistoriques('../97-data/palissy_20200414_14h14m05s.csv', reset=True)
    # mon_inventaire.fixer_liendereference()

    mon_inventaire.split_pdfs(ecrase=False, tar_pdf=True)


    if PARAM_DEBUG == 'MAIN_DEBUG':
        pass
        #mon_inventaire.to_csv('../98-indexes/index_debug.csv')
        #mon_inventaire.to_json('../98-indexes/Ardennes_out.json', limit=1)
    else:
        pass
        #mon_inventaire.to_csv('../98-indexes/index.csv')
        #mon_inventaire.to_json('../98-indexes/Ardennes_out.json')

    inventaire.loggerInventaire.info('Fin du script'.format(time.asctime(time.localtime())))
