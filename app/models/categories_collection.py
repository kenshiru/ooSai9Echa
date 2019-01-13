from .category import Category


class CategoriesCollection:
    def __init__(self):
        self.categories = {}

    def add_category(self, category: Category):
        self.categories[category.name] = category

    def get_category(self, name: str) -> Category:
        return self.categories.get(name)

    def get_categories_by_phrase(self, phrase) -> list:
        return [category for category in self.categories.values() if category.has_items(phrase)]
