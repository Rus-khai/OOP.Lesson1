import pytest
from main import Product, Category, product1, product2, product3

@pytest.fixture
def test_products_2():
    return Product(
        name='Iphone 15',
        description='512GB, Gray space',
        price=210000.0,
        quantity=8
    )

@pytest.fixture
def test_category():
    return Category(
        name='Смартфоны',
        description='Cмартфоны, как средство не только коммуникации, '
                    'но и получения дополнительных функций для удобства жизни',
        products=[product1, product2, product3]
    )

@pytest.fixture
def test_products():
    return Product(
        name='Samsung Galaxy S23 Ultra',
        description='56GB, Серый цвет, 200MP камера',
        price=180000.0,
        quantity=5
    )


def test_main(test_products_2):
    assert test_products_2.name == 'Iphone 15'
    assert test_products_2.description == '512GB, Gray space'
    assert test_products_2.price == 210000.0
    assert test_products_2.quantity == 8

def test_main_product(test_products):
    assert test_products.name == 'Samsung Galaxy S23 Ultra'
    assert test_products.description == '56GB, Серый цвет, 200MP камера'
    assert test_products.price == 180000.0
    assert test_products.quantity == 5

def test_main_category(test_category):
    assert test_category.name == 'Смартфоны'
    assert test_category.description == ('Cмартфоны, как средство не только коммуникации, '
                                         'но и получения дополнительных функций для удобства жизни')
    assert test_category.products == [product1, product2, product3]


