import unittest
from app.models.category_item import CategoryItem


class TestCategoryItem(unittest.TestCase):

    def test_init(self):
        self.assertEqual(
            CategoryItem('Деревья на садовом кольце').name_words,
            set(['деревья', 'на', 'садовом', 'кольце'])
        )

        self.assertEqual(
            CategoryItem('Деревья на ,садовом кольце').name_words,
            set(['деревья', 'на', 'садовом', 'кольце'])
        )
        self.assertEqual(
            CategoryItem('ДеРеВьЯ на ,саДоВОМ кольце').name_words,
            set(['деревья', 'на', 'садовом', 'кольце'])
        )

    def test_check(self):
        self.assertTrue(CategoryItem('рецепт борща').check('Борща любимого рецепт'))
        self.assertTrue(CategoryItem('рецепт борща').check('Борща рецепт'))
        self.assertTrue(CategoryItem('рецепт борща').check('Борща ,рецепт'))
        self.assertFalse(CategoryItem('рецепт борща корейского').check('Борща любимого рецепт'))
