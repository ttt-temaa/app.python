from src.lesson_1 import Category, Product


def test_product_initialization():
    """Тест инициализации продукта"""

    product = Product("Product", "Description", 100.0, 10)
    assert product.name == "Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization():
    """Тест инициализации категории без продуктов"""

    category = Category("Category", "Description")
    assert category.name == "Category"
    assert category.description == "Description"
    assert len(category.products) == 0


def test_category_with_products():
    """Тест инициализации категории с продуктом"""

    product = Product("Product", "Description", 100.0, 10)
    category = Category("Category", "Description", [product])
    assert len(category.products) == 1
    assert Category.product_count == 1


def test_add_product_to_category():
    """Тест добавления продукта в категорию"""

    category = Category("Category", "Description")
    product = Product("New Product", "New Description", 150.0, 5)

    # Проверяем, что продукт добавляется корректно
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0].name == "New Product"
    assert Category.product_count == 2


def test_category_count():
    """Тест подсчета категорий"""
    Category.category_count = 0
    _ = Category("Category1", "Description1")
    _ = Category("Category2", "Description2")
    assert Category.category_count == 2


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

    # Добавляем несколько продуктов
    product1 = Product("Product1", "Description1", 200.0, 15)
    product2 = Product("Product2", "Description2", 300.0, 20)
    category.add_product(product1)
    category.add_product(product2)

    assert len(category.products) == 2
    assert Category.product_count == 2
    assert category.products[0].name == "Product1"
    assert category.products[1].name == "Product2"


def test_empty_category():
    """Тест инициализации пустой категории"""
    category = Category("Empty Category", "No products")
    assert len(category.products) == 0


def test_product_negative_price():
    """Тест проверки работы с отрицательной ценой продукта"""
    product = Product("Test Product", "Test Description", -50.0, 10)
    assert product.price == -50.0
    assert product.quantity == 10


def test_product_negative_quantity():
    """Тест проверки работы с отрицательным количеством продукта"""
    product = Product("Test Product", "Test Description", 100.0, -5)
    assert product.quantity == -5
