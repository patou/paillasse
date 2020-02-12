# Inventaire national des orgues
Gwilherm Poullennec

(contact@inventaire-des-orgues.org)

## Présentation générale

Ces scripts Python permettent la gestion de l'index principal, base de l'inventaire national des orgues.

Cet index est une table en format texte:
- format CSV séparateur point-virgule
- encodée en UTF-8
- fins de lignes au format Windows CR+LF (\r\n)

L'index accueille les informations permettant la correspondance avec d'autres bases de données,
ainsi que quelques informations résumées de ces autres bases de données.

Les bases de données mises en correspondance (jointure) avec l'index sont, à ce jour, les suivantes :
- livres d'inventaires scannés
- base Palissy du ministère de la culture, répertoriant les objets classés ou inscrits
- site Internet orgbase.nl
- site Internet MessesInfo, répertoriant les édifices religieux de culte catholique

L'index a vocation à être mis en correspondance, à l'avenir, avec les principaux sites Internet francophones inventoriant des orgues.

## Structure de l'index

### Enregistrements (lignes)
L'index comprend un enregistrement par orgue. Un orgue correspond à un emplacement géoographique unique. Sont concernés par l'inventaire national :
- tous les orgues du territoire français, métropole et outres-mers;
- d'accès public, c'est-à-dire hébergés dans un lieu privé ou public, mais à l'exclusion des domiciles de particuliers;
- à tuyaux et alimentés mécaniquement en vent, à l'exclusion donc des instruments électroniques ou encore des harmoniums;
- existants à ce jour, à l'exclusion donc des instruments complètement disparus;
- quelque soit leur état ou leur utilisation : en fonctionnement, dégradé, partiel. Notamment, les buffets vides sont concernés;

### Champs (colonnes)
L'index comprend :
1. des champs principaux, décrivant exactement et de façon unique un emplacement géographique. Lorsque l'inventaire sera mis en ligne, ces champs ne seront modifiables que par les administrateurs.
2. des champs secondaires, décrivant les caractéristiques de l'orgue et permettant la correspondance vers d'autres bases de données. Ils seront ouverts à la modification.

- commune_insee : commune de plein droit, selon code national géographique (à l'exclusion donc des communes déléguées et associées)
- edifice : nom usuel de l'édifice
- edifice_standard : nom de l'édifice standardisé (discrimintation entre nom propre et type d'édifice)
- info_edifice : traces de traitement du nom de l'édifice
- codification_edifice : codification de l'édifice
- nomdepartement : nom du département, selon code géographique national
- code_departemnet : code du département, selon code géographique national
- nomregion : nom de la région, selon le code géographique national
- code_insee : code INSEE de la commune, selon le code géographique national
- adresse : complément d'adresse permettant l'identification de l'édifice, généralement la commune associée ou déléguée, ou l'ancien nom de commune, en cas de fusion, parfois le lieu-dit
- denomination : dénomniation de l'orgue, par exemple : "O.C." pour orgue de choeur, "G.O." pour grand-orgue, "Polyphone" pour un polyphone Debierre, ou un numéro d'ordre
- livre : livre d'inventaire dans lequel est répertorié l'orgue
- pages_pdf : pages concernant l'orgue dans le fichier scannés du livre d'inventaire. Les intervalles, inclusifs, de pages sont séparés par des virgules et notés avec un trait d'union, sauf si une page est seule. Exemple : "12, 14-18".
- pages_livre : pages concernant l'orgue telles que définies dans le livre d'inventaire. Ce ne sont pas nécessairemnt les même que celles du fichier de scan (présence de couverture, planches non numérotées dans les livres, etc.)
- pages_livre_complement : autre notation permettant l'identification des pages dans le livre d'inventaire, par exemple dans le cas de classeurs rassemblant des fiches.
- commentaire : champ libre
- log : champ libre utilisé pour des remarques sur des traitements (erreurs, alertes, etc.)
- site_ref : lien Internet du site de référencec dédiée à l'instrument, à savoir le site de l'association oeuvrant pour l'instrument.
- latitude : latitude, en format GPS, de l'emplacement.
- longitude : longitude, en format GPS, de l'emplacement.
- orgbase_manu : lien Internet sur la fiche de l'orgue sur le site Orgbase.nl, renseigné à la main.
- orgbase_commune : commune de l'orgue telle qu'écrite sur le site Orgbase.nl
- orgbase_auto : lien Internet sur la fiche de l'orgue sur le site Orgbase.nl, renseigné automatiquement par les scripts.
- orgbase_desc : description de l'orgue sur le site Orgbase.nl.
- orgbase_edifice : nom de l'édifice hébergeant l'orgue sur le site Orgbase.nl
- orgbase_facteurs : champ décrivant les facteurs étant intervenus sur l'orgue, tels que décrits sur le site Orgbase.nl
- orgbase_minicomposition : composition abrégée de l'orgue sur le site Orgbase.nl
- orgbase_edifice_standard : nom de l'édifice hébergeant l'orgue sur le site Orgbase.nl standardisé (discrimintation entre nom propre et type d'édifice)
- orgbase_edifice_log : traces de traitement du nom d'édifice en provenance de Orgbase.nl.
- orgbase_commune_insee : commune de l'orgue trouvée dans le code géographique national, transcrite depuis le site Orgbase.nl
- reference_palissy : codes Palissy de référence sur l'orgue (champ REF de Palissy). Plusieurs codes pouvant exister pour un même instrument, ils sont séparés de traits-union.
- denomination_palissy : dénomination de l'instrument dans Palissy (champ DENO de Palissy).
- edifice_palissy : nom de l'édifice dans Palissy (champ EDIF de Palissy).
- protection_palissy : protection (inscription ou classement) telle que présente dans Palissy (champ PROT).

## Scripts Python

### Scripts de gestion des bases de données d'orgue
- inventaire.py : script principal de lecture / écriture CSV de l'index général de l'inventaire

- palissy.py : lecture d'un export CSV de la base Palissy et modélisation objet
- orgbase.py : lecture d'un export CSV de la base orgbase.nl et modélisation objet
- gpsmessesinfo.py : lecture d'un export CSV de la base MessesInfo et modélisation objet

Ces scripts mettent généralement en oeuvre deux classes principales :
1. Une classe décrivant toute la base de données, et héritant des objets Python 'dict' ou 'list'.
2. une classe décrivant un orgue dans la base de données, portant les attributs permettant la description de l'instrument.
Ces classes comportent des méthodes heuristiques pour mettre en correspondance des bases de données diverses avec l'inventaire. Elles comportent des tests de comparaison de noms de commune et de nom d'édifice, non génériques.
Généralement, ces tests sont facilités par une dégénérescence (simplification de légère à drastique) du nom de l'édifice.
Ils ne permettent pas de mettre en correspondance la totalité des instruments, mais produisent des traces en cas d'échec, permettant la mise en correspondance manuelle, et/ou, le cas échéant, la correction d'erreur de données de part et d'autre.

### Scripts utilitaires
- /utilsorgues/codegeographique.py : lectures des CSV de l'INSEE et modélisation objet du code national géographique de l'INSEE
- /utilsorgues/codification.py : outils de codification des noms d'édifice et de commune
- /utilsorgues/correcteurorgues.py : outils de corrections des dénominations d'édifice
- /utilsorgues/generiques/generiques.py : outils de modification des chaînes de caractères

Les fonctions de codification ou de correction des dénominations d'édifice sont des heuristiques non génériques.
Elles comportent de nombreux tests permettant par exemple la détection du type d'édifice et l'homogénisation des noms religieux, principalement les noms de saints et saintes, ainsi que les multiples appellations de la Vierge Marie.
