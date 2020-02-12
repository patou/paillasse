import re
import sys

fichier = 'D:/Users/gwilpoul/Documents/inventaire/python/inventaire--palissy.log'
fichier_out = 'D:/Users/gwilpoul/Documents/inventaire/python/grep.csv'
ma_re = r'.*ERROR|DEBUG.*'


if __name__ == '__main__':
    with open(fichier_out, "w", encoding='utf-8') as fic_out:
        compteur_lignes = 0
        for line in open(fichier, "r", encoding='ANSI'):
            #texte = ";".join(line.split(';')[3:4])
            if re.search(ma_re, line):
                 compteur_lignes += 1
                 print(line.rstrip('\r\n'))
                 fic_out.write(line)
        print(compteur_lignes)