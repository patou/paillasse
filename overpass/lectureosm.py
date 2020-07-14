# Petit parser OSM
# imposm n'est compatible que Python 2, et Pyosmium un peu compliqué, d'où ce module ad hoc.
#

import requests
import xml.etree.ElementTree as et
import json

REGIONS_METROPOLE = ['Île-de-France', 'Centre-Val de Loire', 'Bourgogne-Franche-Comté', 'Normandie', 'Hauts-de-France', 'Grand Est', 'Pays de la Loire', 'Bretagne', 'Nouvelle-Aquitaine', 'Occitanie', 'Auvergne-Rhône-Alpes', "Provence-Alpes-Côte d'Azur", 'Corse']
REP_TRAVAIL = 'D:\\Users\\poullennecgwi\\Downloads\\OSM\\overpass\\'
FIC_COMMUNES = 'D:\\Users\\poullennecgwi\\Downloads\\OSM\\communes-20190101\\communes-20190101.json'

# FIC_OSM = 'D:\\Users\\poullennecgwi\\Downloads\\OSM\\overpass\\exportNormandie.osm'
# FIC_CSV = 'D:\\Users\\poullennecgwi\\Downloads\\OSM\\overpass\\simpleNormandie2.csv'

REGIONS_TO_DEPARTEMENTS = {
    'IDF_11': ['75', '77', '78', '91', '92', '93', '94', '95'],
    'CVL_24': ['18', '28', '36', '37', '41', '45'],
    'BFC_27': ['21', '25', '39', '58', '70', '71', '89', '90'],
    'NOR_28': ['14', '27', '50', '61', '76'],
    'HDF_32': ['02', '59', '60', '62', '80'],
    'GDE_44': ['08', '10', '51', '52', '54', '55', '57', '67', '68', '88'],
    'PDL_52': ['44', '49', '53', '72', '85'],
    'BZH_53': ['22', '29', '35', '56'],
    'NAQ_75': ['16', '17', '19', '23', '24', '33', '40', '47', '64', '79', '86', '87'],
    'OCC_76': ['09', '11', '12', '30', '31', '32', '34', '46', '48', '65', '66', '81', '82'],
    'ARA_84': ['01', '03', '07', '15', '26', '38', '42', '43', '63', '69', '73', '74'],
    'PAC_93': ['04', '05', '06', '13', '83', '84'],
    'COR_94': ['2A', '2B']}


def point_inside_polygon(x, y, poly):
    """
    pi = point_inside_polygon(-0.4469913, 49.06458854,[[-0.45787379999999994,49.063878499676505],[-0.45120179999999993,49.06545309967611],[-0.4490515999999999,49.06581489967605],[-0.4465841999999999,49.06511829967619],[-0.4447340999999999,49.06226299967692],[-0.4434336999999999,49.05990669967749],[-0.4433420999999999,49.05818069967792],[-0.4408370999999998,49.05698349967822],[-0.43827619999999984,49.05434349967888],[-0.43331149999999985,49.05220449967939],[-0.4315589999999999,49.049395399680094],[-0.42769279999999993,49.0485695996803],[-0.4233090999999998,49.04935709968009],[-0.42333359999999987,49.048492699680324],[-0.42038369999999986,49.04623629968087],[-0.4189124999999999,49.04407639968142],[-0.4187658999999999,49.041491399682045],[-0.42316739999999997,49.04163209968202],[-0.4226608999999999,49.040575899682274],[-0.4189809999999999,49.040362699682326],[-0.41843389999999997,49.038031799682905],[-0.4192943999999999,49.03497019968365],[-0.4209701999999999,49.03203359968438],[-0.4240864999999998,49.033158299684104],[-0.4249922999999998,49.03427409968383],[-0.4276364999999998,49.03257909968425],[-0.4292303999999999,49.03293499968415],[-0.4296871999999999,49.03054189968476],[-0.4334565999999999,49.03171699968447],[-0.4375177999999999,49.03209819968437],[-0.4437569999999999,49.03175409968446],[-0.44813159999999985,49.03103119968465],[-0.4515078999999999,49.0311816996846],[-0.4551178999999998,49.032424699684285],[-0.4581422999999998,49.03203539968438],[-0.46013319999999985,49.03254019968425],[-0.46557539999999986,49.03316259968411],[-0.4662986999999999,49.03251009968428],[-0.4666053999999999,49.03484209968368],[-0.46549669999999993,49.03759469968303],[-0.46506099999999984,49.04130789968208],[-0.4632872999999998,49.04460889968127],[-0.4605772999999999,49.047437299680595],[-0.4586226999999998,49.0488584996802],[-0.4592217999999999,49.05379739967902],[-0.46079659999999983,49.05928549967764],[-0.4604008999999999,49.06062159967731],[-0.45787379999999994,49.063878499676505]])
    print(pi)
    :param x: long
    :param y: lat
    :param poly: liste de listes[lon, lat]
    :return: bool
    """
    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y
    return inside


def test_gps_to_commune_pointinterieur():
    with open('D:\\Users\\poullennecgwi\\Downloads\\OSM\\communes-20190101\\LeConquet.json', encoding='utf-8') as fjson:
        print('Chargement GeoJson des communes françaises...')
        j = json.load(fjson)
        print('Fin chargement GeoJson des communes françaises.')
    res = gps_to_commune_pointinterieur(48.3590054, -4.7728487, j, REGIONS_TO_DEPARTEMENTS['BZH_53'])
    print(res)


def gps_to_commune_pointinterieur(_lat, _lon, j, deps):
    # FIXME : Le Conquet, Hyères, Guérande...
    communes = j['features']
    (nom, insee) = (None, None)
    for commune in communes:
        insee = commune['properties']['insee']
        # Accélération : on ne recheche que dans les bons départements:
        if insee[:2] in deps:
            nom = commune['properties']['nom']
            # Détection du nombre de polygones :
            typec = commune['geometry']['type']
            # Si la commune n'est qu'un seul polygone
            if typec == 'Polygon':
                poly = commune['geometry']['coordinates'][0]
                if point_inside_polygon(_lon, _lat, poly):
                    return nom, insee
            # Si la commune est plusieurs polygones (non connexité)
            elif typec == 'MultiPolygon':
                poly = commune['geometry']['coordinates']
                for sous_poly in poly:
                    if point_inside_polygon(_lon, _lat, sous_poly[0]):
                        return nom, insee
    print("Echec du point intérieur.".format(_lat, _lon))
    return None, None


def gps_to_commune_api(_lat, _lon):
    _proxies = {'https': 'https://NNI:MDP@proxy-surf.rte-france.com:3128',
                'http': 'http://NNI:MDP@proxy-surf.rte-france.com:3128'}
    url = 'https://geo.api.gouv.fr/communes'
    param = {'lat': _lat, 'lon': _lon, 'fields': 'nom,code,codesPostaux,codeDepartement,codeRegion,population',
             'format': 'json', 'geometry': 'centre'}
    r = requests.get(url, params=param, proxies=_proxies)
    print(r.text)
    j = eval(r.text)
    return j[0]['nom'], j[0]['code']


class OsmData:
    def __init__(self, _fic_osm):
        print('Lecture données OSM depuis le fichier : {}'.format(_fic_osm))
        self.nodes = dict()
        self.ways = list()
        self.ways_centers = dict()
        self.relations = list()
        #
        tree = et.parse(_fic_osm)
        root = tree.getroot()
        #
        for node in root.findall('node'):
            _id = node.get('id')
            lat = float(node.get('lat'))
            lon = float(node.get('lon'))
            # Création du node
            osmnode = Node(_id, lat, lon)
            self.nodes[_id] = osmnode
        #
        for way in root.findall('way'):
            _id = way.get('id')
            nodes = way.findall('nd')
            refs_nodes = list()
            for node in nodes:
                ref = node.get('ref')
                refs_nodes.append(ref)
            tags = way.findall("tag")
            for tag in tags:
                if tag.get('k') == "name":
                    name = tag.get('v')
                if tag.get('k') == 'building':
                    building = tag.get('v')
            # Création du way:
            osmway = Way(_id, refs_nodes, name, building)
            self.ways.append(osmway)
        #
        for relation in root.findall('relation'):
            _id = relation.get('id')
            osmmembers = list()
            members = relation.findall('member')
            for member in members:
                mtype = member.get('type')
                ref = member.get('ref')
                osmmembers.append((ref, mtype))
            tags = relation.findall("tag")
            for tag in tags:
                if tag.get('k') == 'type':
                    _type = tag.get('v')
                if tag.get('k') == "name":
                    name = tag.get('v')
                if tag.get('k') == 'building':
                    building = tag.get('v')
            # Création de la relation:
            osmrelation = Relation(_id, osmmembers, _type, name, building)
            self.relations.append(osmrelation)

    def count(self):
        print('Ce fichier contient : {} nodes, {} ways, {} relations'.format(len(self.nodes), len(self.ways), len(self.relations)))

    def compute_ways_centers(self):
        # Barycentres des ways
        for way in self.ways:
            lat_moy = sum([self.nodes[ref].lat for ref in way.refsnodes]) / len(way.refsnodes)
            lon_moy = sum([self.nodes[ref].lon for ref in way.refsnodes]) / len(way.refsnodes)
            self.ways_centers[way.id] = (lat_moy, lon_moy)

    def find_communes_ways(self, jsoncommunes, _deps):
        for way in self.ways:
            lat = self.ways_centers[way.id][0]
            lon = self.ways_centers[way.id][1]
            if jsoncommunes:
                way.com, way.code = gps_to_commune_pointinterieur(lat, lon, jsoncommunes, _deps)
            else:
                way.com, way.code = gps_to_commune_api(lat, lon)

    def way_to_csv(self, _fic_csv_ways):
        with open(_fic_csv_ways, 'w', encoding='utf-8') as fcsv:
            for way in self.ways:
                lat = self.ways_centers[way.id][0]
                lon = self.ways_centers[way.id][1]
                fcsv.write('{};{};{};{};{};{};\n'.format('way',
                                                         way.id,
                                                         way.name,
                                                         str(lat),
                                                         str(lon),
                                                         way.com,
                                                         way.code))


class OsmElement(object):
    pass


class Node(OsmElement):
    def __init__(self, _id, _lat, _lon):
        self.id = _id
        self.lat = _lat
        self.lon = _lon
        return

    def __repr__(self):
        return '<Node {} {} {}>'.format(self.id,
                                        self.lat,
                                        self.lon)


class Way(OsmElement):
    def __init__(self, _id, _refs_nodes, _name, _building):
        self.id = _id
        self.refsnodes = _refs_nodes
        self.name = _name
        self.building = _building
        self.com = ''
        self.code = ''

    def __repr__(self):
        return '<Way {} {} {} {}>'.format(self.id,
                                          self.name,
                                          self.building,
                                          self.refsnodes)


class Relation(OsmElement):
    def __init__(self, _id, _osmmembers, _type, _name, _building):
        self.id = _id
        self.osmmembers = _osmmembers
        self.type = _type
        self.name = _name
        self.building = _building
        return

    def __repr__(self):
        return '<Relation {} {} {} {}>'.format(self.id,
                                               self.osmmembers,
                                               self.type,
                                               self.name,
                                               self.building)


def trouve_relation_non_polygone(osm):
    # Relations qui ne sont pas des multipolygon
    for relation in osm.relations:
        if relation.type != 'multipolygon':
            print("Relation qui n'est pas de type polygon {}".format(relation))
            # print([mid[0] for mid in relation.osmmembers])


def trouve_ways_ouverts(osm):
    # Ways qui ne sont pas fermés:
    for way in osm.ways:
        if way.refsnodes[0] != way.refsnodes[-1]:
            print('Way non fermé {}'.format(way))


def main():
    with open(FIC_COMMUNES, encoding='utf-8') as fjson:
        print('Chargement GeoJson des communes françaises...')
        j = json.load(fjson)
        print('Fin chargement GeoJson des communes françaises.')
        #
        # Boucle sur les régions
        for region, departements in REGIONS_TO_DEPARTEMENTS.items():
            osm = OsmData(REP_TRAVAIL + 'export-' + region + '.osm')
            osm.count()
            osm.compute_ways_centers()
            osm.find_communes_ways(j, departements)
            osm.way_to_csv(REP_TRAVAIL + 'simple-' + region + '.csv')


if __name__ == '__main__':
    main()
