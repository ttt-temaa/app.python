class Product:
    """Класс для представления продукта"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, data):
        return cls(data["name"],
                   data["description"],
                   data["price"],
                   data["quantity"])


class Category:
    """Класс для представления категории"""

    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products is not None else []
        Category.product_count += len(self._products)

    def add_product(self, product: Product):
        """Добавление продукта в категорию"""
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка продуктов"""
        return "\n".join(
            [
                f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
                for p in self._products
            ]
        )
