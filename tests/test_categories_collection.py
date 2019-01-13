import unittest
from app.models.category import Category
from app.models.category_item import CategoryItem
from app.models.categories_collection import CategoriesCollection


class TestCategoriesCollection(unittest.TestCase):
    CATEGORIES = {
        "новости": [
            "Деревья на садовом кольце",
            "добрый автобус",
            "выставка IT-технологий"
        ],
        "кухня": [
            "рецепт борща",
            "яблочный пирог",
            "тайская кухня"
        ],
        "товары": [
            "Дети капитана Гранта",
            "зимние шины",
            "тайская кухня"
        ]
    }

    def setUp(self):
        self.collection = CategoriesCollection()
        for category_name, category_items in self.CATEGORIES.items():
            category = Category(category_name)
            for raw_item in category_items:
                category.add_item(CategoryItem(raw_item))
            self.collection.add_category(category)

    def test_add_category(self):
        new_category = Category('testName')
        self.collection.add_category(new_category)
        self.assertEqual(self.collection.get_category('testName'), new_category)

    def test_get_category(self):
        category_name = 'кухня'
        category = self.collection.get_category(category_name)
        self.assertEqual(category_name, category.name)

    def test_get_category_by_phrase(self):
        phrase = "тайская кухня"
        expect_categories_names = ["кухня", "товары"]
        found_categories = self.collection.get_categories_by_phrase(phrase)
        self.assertEqual(len(found_categories), 2)
        for category in found_categories:
            self.assertTrue(category.name in expect_categories_names)
