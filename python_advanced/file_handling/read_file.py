#!/usr/bin/env python3
"""
Ce module fournit la fonction read_file.
"""


def read_file(filename=""):
    """Lit un fichier texte codé en UTF-8 et l'affiche sur stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
