#!/usr/bin/env python3
"""
Ce module fournit la fonction read_file.
"""


def write_file(filename="", text=""):
    """Lit un fichier texte codé en UTF-8 et l'affiche sur stdout."""
    with open(filename, 'w', encoding="utf-8") as f:
        data = f.filename
        print(f.read(), end="")
    return data
