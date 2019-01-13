from .category import Category


class CategoriesCollection:
    """
    Store categories here
    """
    def __init__(self):
        """
        Set categories dictionary to self
        """
        self.categories = {}

    def add_category(self, category: Category):
        """
        Add category to collection
        :param category: category instance
        :type category: Category
        :return: None
        """
        self.categories[category.name] = category

    def get_category(self, name: str) -> Category:
        """
        Search category by full name
        :param name: category name
        :type name: str
        :return: category or None
        :rtype Category
        :rtype None
        """
        return self.categories.get(name)

    def get_categories_by_phrase(self, phrase: str) -> list:
        """
        Search categories by phrase
        :param phrase:
        :return: list of found categories
        :rtype list
        """
        return [category for category in self.categories.values() if category.has_items(phrase)]
