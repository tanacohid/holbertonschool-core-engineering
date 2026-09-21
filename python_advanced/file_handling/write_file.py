#!/usr/bin/env python3
"""
Ce module fournit la fonction write_file.
"""


def write_file(filename="", text=""):
    """Écrit une chaîne de caractères dans un fichier texte (UTF-8)
    et renvoie le nombre de caractères écrits.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
