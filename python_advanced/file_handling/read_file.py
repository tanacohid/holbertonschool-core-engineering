#!/usr/bin/env python3
"""
    Ce module contient une fonction qui lit un fichier texte
    et affiche son contenu sur la sortie standard.
    """

def read_file(filename=""):

    """
    Lit un fichier texte (UTF-8) et l'affiche dans stdout.
    """
    with open("UTF8.txt", 'r', encoding="utf-8") as f:
        data = f.read()
    print(data)
