
class Inventory:
    def __init__(self):
        self._items: list = []   # _ is used in the variable is used to mention or give the sign that it is a protected variable

    def add(self, item):
        self._items.append(item)
    
    def use(self, index: int, target) -> str:
        item = self._items.pop(index)
        return item.apply(target)

    def list_items(self) -> list[str]:
        return [type(i).__name__ for i in self._items]    # this returns the list with the name of the items
    
