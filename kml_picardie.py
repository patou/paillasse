"""
Parseur des kml extraits des cartes du site Orgues de Picardie.
Le parseur extrait : le département, la commune, l'édifice (si plusieurs dans la commune),
ainsi que les coordonnées GPS.

#FIXME : il faut supprimer à la main la ligne déclaration d'encoding (première ligne) du kml.
"""
from fastkml import kml


def lecture_picardie(repertoire_picardie, departements_picardie):
    """
    :param repertoire_picardie:
    :param departements_picardie:
    :return: orgues_picardie: liste [[departement, commune, edifice, x_gps, y_gps],...]
    """
    orgues_picardie = list()
    # Parcours des fichiers KML.
    for departement_picardie in departements_picardie:
        with open(repertoire_picardie + departement_picardie + '.kml',encoding='utf-8') as f_kml:
            doc = f_kml.read()
            k = kml.KML()
            k.from_string(doc)
            features = list(k.features())
            for f in features[0].features():
                for placemark in f.features():
                    name = placemark.name.rstrip('\n')
                    # Si l'édifice est présent :
                    if ' - ' in name:
                        commune, edifice = name.split(' - ')
                    # Si l'édifice est absent :
                    else:
                        commune, edifice = name, None
                    orgues_picardie.append([departement_picardie,
                                            commune,
                                            edifice,
                                            str(placemark.geometry.x),
                                            str(placemark.geometry.y)])
    return orgues_picardie


if __name__ == '__main__':
    orgues_picards = lecture_picardie('../97-data/', ['aisne', 'somme', 'oise'])
    print(orgues_picards)