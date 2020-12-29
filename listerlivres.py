"""
Parcourt le dossier des livres scannés.
Affiche les fichiers .pdf
"""

import os

REP_LIVRES = 'E:\\02-scans'
l = os.walk(REP_LIVRES)
for root, dirs, files in l:
    for file in files:
        terminaison = '--vectorise.pdf'
        if file[-len(terminaison):] == terminaison:
            print("{}\\{}".format(root, file))

f = open("..\\98-indexes\\liste-sources.txt", 'r')
sources = f.readlines()
for s in set(sources):
    print(s)
f.close()