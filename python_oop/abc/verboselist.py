#!/usr/bin/env python3
"""Defines the VerboseList class."""


class VerboseList(list):
    """A list that prints messages when modified."""

    def append(self, item):
        """Add an item to the list and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print the number of items added."""
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Remove an item from the list and print a message."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item, then print a message."""
        item = self[index]
        result = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return result
