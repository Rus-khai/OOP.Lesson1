import pytest
from main import Product, Category, product1, product2, product3


@pytest.fixture
def test_products():
    return Product(
        name='Samsung Galaxy S23 Ultra',
        description='56GB, Серый цвет, 200MP камера',
        price=180000.0,
        quantity=5
    )


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