from app.models.category import Category
from app.models.category_item import CategoryItem
from app.models.categories_collection import CategoriesCollection

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

categories_collection = CategoriesCollection()

for category_name in CATEGORIES:
    category_items = CATEGORIES[category_name]
    category = Category(category_name)

    for raw_item in category_items:
        category.add_item(CategoryItem(raw_item))

    categories_collection.add_category(category)
