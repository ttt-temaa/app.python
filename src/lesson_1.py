class Product:
    """Класс для представления продукта"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # приват
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

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

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        return NotImplemented


class Category:
    """Класс для представления категории"""

    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products is not None else []
        Category.product_count += len(self._products)

    def __str__(self):
        total_quantity = sum([p.quantity for p in self._products])
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        """Добавление продукта в категорию"""
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка продуктов"""
        return "\n".join([str(p) for p in self._products])

    def __iter__(self):
        return CategoryIterator(self)


class CategoryIterator:
    def __init__(self, category):
        self._category = category
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._category._products):
            product = self._category._products[self._index]
            self._index += 1
            return product
        raise StopIteration
