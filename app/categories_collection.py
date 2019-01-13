"""
Filled from categories-collection.json storage
Import categories_collection from here
"""
import json
from app.models import Category, CategoryItem, CategoriesCollection

CATEGORIES = json.load(open('./categories-collection.json'))

categories_collection = CategoriesCollection()

for category_name in CATEGORIES:
    category_items = CATEGORIES[category_name]
    category = Category(category_name)

    for raw_item in category_items:
        category.add_item(CategoryItem(raw_item))

    categories_collection.add_category(category)
