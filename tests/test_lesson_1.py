import pytest

from src.lesson_1 import Category, LawnGrass, Product, Smartphone


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


def test_add_product_to_category():
    """Тест добавления продукта в категорию"""
    category = Category("Category", "Description")
    product = Product("New Product", "New Description", 150.0, 5)
    category.add_product(product)
    assert len(category._products) == 1
    assert category._products[0].name == "New Product"


def test_product_add_same_class():
    """Тест сложения объектов одного класса"""
    smartphone1 = Smartphone("Samsung Galaxy",
                             "256GB",
                             1000.0,
                             2,
                             90,
                             "S10",
                             256,
                             "Black")
    smartphone2 = Smartphone("Iphone",
                             "512GB",
                             1200.0,
                             1,
                             95,
                             "12",
                             512,
                             "Silver")
    assert smartphone1 + smartphone2 == 3200.0


def test_product_add_different_classes():
    """Тест сложения объектов разных классов (ожидаем ошибку)"""
    smartphone = Smartphone("Samsung Galaxy",
                            "256GB",
                            1000.0,
                            2,
                            90,
                            "S10",
                            256,
                            "Black")
    grass = LawnGrass("Газонная трава",
                      "Для газона",
                      500.0,
                      5,
                      "Россия",
                      "7 дней",
                      "Зеленый")
    with pytest.raises(TypeError):
        smartphone + grass


def test_category_product_count():
    """Тест подсчета продуктов в категории"""
    Category.product_count = 0
    category = Category("Test Category", "Test Description")
    product = Product("Test Product", "Test Description", 100.0, 10)
    category.add_product(product)
    assert Category.product_count == 1


def test_product_creation_mixin(capsys):
    """Тест для проверки миксера"""
    Product("Test Product", "Test Description", 100.0, 10)
    messages = capsys.readouterr()
    assert messages.out.strip() == ('Создан объект класса Product с параметрами: Test Product, 100.0, Test '
                                    'Description, 10')
