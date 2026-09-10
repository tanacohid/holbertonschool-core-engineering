#!/usr/bin/env python3
"""Module définissant la classe abstraite Animal et ses sous-classes."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe de base abstraite représentant un animal."""

    @abstractmethod
    def sound(self):
        """Méthode abstraite devant retourner le cri de l'animal."""
        pass


class Dog(Animal):
    """Sous-classe représentant un chien."""

    def sound(self):
        """Retourne le cri du chien."""
        return "Bark"


class Cat(Animal):
    """Sous-classe représentant un chat."""

    def sound(self):
        """Retourne le cri du chat."""
        return "Meow"
