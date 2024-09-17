class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории"""

    category_count = 0
    product_count = 0
    name: str
    description: str
    products: list[Product]

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product):
        """Добавление продукта в категорию"""
        self.products.append(product)
        Category.product_count += 1
