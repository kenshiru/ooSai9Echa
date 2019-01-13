import re


class CategoryItem:
    """
    Category item model
    """

    REPLACE_REGEX = re.compile('[^a-zA-Zа-яА-Я ]')

    def __init__(self, name: str):
        """
        Set and parse name
        :param name: item name
        :type name: str
        """
        self.name = name
        self.name_words = self.get_name_words(name)

    @classmethod
    def get_name_words(cls, name: str) -> set:
        """
        Returns words from name in lower case and without alphabetic symbols
        (only a-Zа-Я)
        :param name: item name
        :type name: str
        :return: name words set
        :rtype set
        """
        prepared_name = cls.REPLACE_REGEX.sub('', name)
        return set(prepared_name.lower().split(' '))

    def check(self, phrase: str) -> bool:
        """
        Check phrase similar item
        :param phrase: phrase for checking
        :return: is similar item phrase
        :rtype bool
        """
        given_name_words = self.get_name_words(phrase)
        return len(self.name_words.difference(given_name_words)) == 0
