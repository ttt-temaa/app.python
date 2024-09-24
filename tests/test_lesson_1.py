from src.lesson_1 import Category, Product


def test_product_initialization():
    """Тест инициализации продукта"""

    product = Product("Product", "Description", 100.0, 10)
    assert product.name == "Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_price_setter_positive():
    """Тест работы сеттера цены с корректным значением"""

    product = Product("Product", "Description", 100.0, 10)
    product.price = 200.0
    assert product.price == 200.0


def test_product_price_setter_negative():
    """Тест работы сеттера цены с отрицательным значением"""

    product = Product("Product", "Description", 100.0, 10)
    product.price = -50.0
    assert product.price == 100.0


def test_category_initialization():
    """Тест инициализации категории без продуктов"""

    category = Category("Category", "Description")
    assert category.name == "Category"
    assert category.description == "Description"
    assert len(category._products) == 0


def test_category_with_products():
    """Тест инициализации категории с продуктом"""

    product = Product("Product", "Description", 100.0, 10)
    category = Category("Category", "Description", [product])
    assert len(category._products) == 1
    assert Category.product_count == 1


def test_add_product_to_category():
    """Тест добавления продукта в категорию"""

    category = Category("Category", "Description")
    product = Product("New Product", "New Description", 150.0, 5)

    category.add_product(product)
    assert len(category._products) == 1
    assert category._products[0].name == "New Product"
    assert Category.product_count == 2


def test_product_count():
    """Тест подсчета продуктов"""

    Category.product_count = 0
    category = Category("Test Category", "Test Description", [])
    product = Product("Test Product", "Test Description", 100.0, 10)
    category.add_product(product)
    assert Category.product_count == 1


def test_add_multiple_products():
    """Тест добавления нескольких продуктов в категорию"""

    Category.product_count = 0
    category = Category("Test Category", "Test Description", [])

    product1 = Product("Product1", "Description1", 200.0, 15)
    product2 = Product("Product2", "Description2", 300.0, 20)

    category.add_product(product1)
    category.add_product(product2)

    assert len(category._products) == 2
    assert Category.product_count == 2
    assert category._products[0].name == "Product1"
    assert category._products[1].name == "Product2"


def test_empty_category():
    """Тест инициализации пустой категории"""

    category = Category("Empty Category", "No products")
    assert len(category._products) == 0


def test_product_negative_quantity():
    """Тест проверки работы с отрицательным количеством продукта"""

    product = Product("Test Product", "Test Description", 100.0, -5)
    assert product.quantity == -5


def test_product_str():
    """Тест строкового представления объекта Product."""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_category_str():
    """Тест строкового представления объекта Category."""
    product1 = Product("Test Product 1", "Test Description 1", 100.0, 10)
    product2 = Product("Test Product 2", "Test Description 2", 50.0, 5)
    category = Category("Test Category",
                        "Test Description",
                        [product1, product2])
    assert str(category) == "Test Category, количество продуктов: 15 шт."


def test_product_add():
    """Тест магического метода сложения для объектов Product."""
    product1 = Product("Test Product 1", "Test Description 1", 100.0, 10)
    product2 = Product("Test Product 2", "Test Description 2", 50.0, 5)
    assert product1 + product2 == 1250.0
