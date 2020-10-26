#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
from os.path import getsize
# TODO: Définissez vos fonction ici

def compare_files(fname1, fname2):
    with open(fname1, 'r') as f, open(fname2, 'r') as p:
        if f.getsize() != p.getsize():
            print('Les fichiers ne sont pas de la même taille')
        else:
            c, k = f.read(1), p.read(1)
            while c != '' and k != '':
                if c != k:
                    position = f.tell()
                    print(f"la différence à la position {position} est {c} et {k}")
                    break
                c, k = f.read(1), p.read(1)

def trouver_nombre_ordre_croissant(fname):
    with open(fname, 'r') as f:
        données = f.read()

    listeNombres = sorted([int(mot) for mot in données.split() if mot.isdigit()])

    #mots = données.split()
    #for mot in mots:
     #   if mot.isdigit():
     #       listeNombres.append(int(mot))
   # listeNombres.sort()
    print(listeNombres)


if __name__ == '__main__':
    compare_files('exemple.txt', 'exemple2.txt')
    trouver_nombre_ordre_croissant('exemple.txt')

    pass
