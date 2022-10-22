from __future__ import annotations
from typing import List

from singleton import Singleton

@Singleton
class HelloWorldBuilder: 
    """
    A class that follows the builder pattern, designed to assemble a hello world string
    """

    def __init__(self):
        """
        Instantiates the builder class, creating an empty list for characters
        """
        self._chars: List[str] = []

    def add_char(self, c: str) -> HelloWorldBuilder:
        """
        Will append a new character to the builder's internal list of characters
        :rtype: HelloWorldBuilder
        :param c: The character to add
        :type c: str
        :return: Returns the builder
        """
        if type(c) != str:
            raise TypeError("Character provided must be of type <class='str'>")
        char = c[0]
        self._chars.append(char)
        return self

    def build(self) -> str:
        """
        Builds the internal list of characters into a readable string
        :rtype: str
        :return: Returns the built string
        """
        built_string = ''.join(self._chars)
        return built_string