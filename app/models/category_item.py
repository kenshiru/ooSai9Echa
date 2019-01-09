import re


class CategoryItem:
    REPLACE_REGEX = re.compile('[^a-zA-Zа-яА-Я ]')

    def __init__(self, name):
        self.name = name
        self.name_words = self.get_name_words(name)

    @classmethod
    def get_name_words(cls, name):
        prepared_name = cls.REPLACE_REGEX.sub('', name)
        return set(prepared_name.lower().split(' '))

    def check(self, name):
        given_name_words = self.get_name_words(name)
        return len(self.name_words.difference(given_name_words)) == 0
