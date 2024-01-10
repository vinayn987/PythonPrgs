from typing import List

class ShoppingCart:
    def __init__(self) -> None:
        self.items: List[str] = []

    def add(self, item: str ):
        self.items.append(item)
    
    def size(self) -> int:
        return len(self.items)
    
    def get_items(self) -> List[str]:
        return self.items
    
    def get_total_price(self, price):
        pass



def test_add_item():
    cart = ShoppingCart()
    cart.add('apple')
    assert cart.size() == 1

def test_cart_contain_item():
    cart = ShoppingCart()
    cart.add('apple')
    assert 'apple' in cart.get_items()
