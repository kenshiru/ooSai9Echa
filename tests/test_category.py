import unittest
from app.models.category import Category
from app.models.category_item import CategoryItem


class TestCategory(unittest.TestCase):
    CATEGORY_ITEMS = [
        "рецепт борща",
        "яблочный пирог",
        "пирог яблочный",
        "тайская кухня"
    ]

    CATEGORY_NAME = "кухня"

    def setUp(self):
        self.category = Category(self.CATEGORY_NAME)
        self.items = {item_name: CategoryItem(item_name) for item_name in self.CATEGORY_ITEMS}

        for category_item in self.items.values():
            self.category.add_item(category_item)

    def testSearchItems(self):
        cases = [
            {
                "queries": [
                    "рецепт борща",
                    "точный рецепт борща",
                    "рецепт вкусного борща",
                    "срочно! где найти рецепт борща?"
                ],
                "expect": [self.items["рецепт борща"]]
            }
        ]

        for test_case in cases:
            for query in test_case['queries']:
                self.assertListEqual(self.category.search_items(query), test_case['expect'])

    def testSearchItemsMany(self):
        cases = [
            {
                "queries": [
                    "яблочный пирог",
                    "пирог яблочный",
                    "большой яблочный пирог"
                ],
                "expect": {
                    "пирог яблочный": self.items["пирог яблочный"],
                    "яблочный пирог": self.items["яблочный пирог"]
                }
            }
        ]

        for test_case in cases:
            for query in test_case['queries']:
                self.assertDictEqual(
                    {item.name: item for item in self.category.search_items(query)},
                    test_case['expect']
                )


