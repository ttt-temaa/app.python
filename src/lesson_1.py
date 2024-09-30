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

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать объекты разных типов")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """Класс для представления смартфона"""

    def __init__(
        self,
            name,
            description,
            price,
            quantity,
            efficiency,
            model,
            memory,
            color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы"""

    def __init__(
        self,
            name,
            description,
            price,
            quantity,
            country,
            germination_period,
            color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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
        """Добавление продукта в категорию с проверкой на тип"""
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять"
                " только объекты класса"
                " Product или его наследников"
            )
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка продуктов"""
        return "\n".join([str(p) for p in self._products])
