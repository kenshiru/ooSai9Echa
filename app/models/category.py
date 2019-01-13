from app.models.category_item import CategoryItem


class Category:
    """
    Category model
    """
    def __init__(self, name: str):
        """
        Set name and declate items attributes
        :param name: category name
        :type name: string
        """
        self.name = name
        self.items = []

    def add_item(self, item: CategoryItem) -> None:
        """
        Append category item into items
        :param item: some category item
        :type item: CategoryItem
        :return: nothing
        :rtype: None
        """
        self.items.append(item)

    def search_items(self, name: str) -> list:
        """
        Search items in category
        :param name: search query
        :type name: str
        :return: list of similar items
        :rtype: list
        """
        return [item for item in self.items if item.check(name)]

    def has_items(self, name: str) -> bool:
        """
        Check similar item exist in category
        :param name: name for check
        :type name: str
        :return: item exist?
        :rtype: bool
        """
        for item in self.items:
            if item.check(name):
                return True
        return False
