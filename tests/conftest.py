import pytest

from src.main import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def test_products():
    return Product(
        name='Samsung Galaxy S23 Ultra',
        description='256GB, Серый цвет, 200MP камера',
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
def test_products_3():
    return Product(
        name='Xiaomi Redmi Note 11',
        description='1024GB, Синий',
        price=31000.0,
        quantity=14
    )


@pytest.fixture
def test_products_4():
    return Product(
        name="55\" QLED 4K",
        description='Фоновая подсветка',
        price=123000.0,
        quantity=7
    )


@pytest.fixture
def test_category():
    return Category(
        name='Смартфоны',
        description=("Смартфоны, как средство не только коммуникации, "
                     "но и получения дополнительных функций для удобства жизни"),
        products=[Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                          180000.0, 5),
                  Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
                  Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
                  ]
    )


@pytest.fixture
def new_product_1():
    return {"name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5}


@pytest.fixture
def smartphone_1_product():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                      180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")


@pytest.fixture
def smartphone_2_product():
    return Smartphone("Iphone 15", "512GB, Gray space",
                      210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone_3_product():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий",
                      31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def lawngrass_1_product():
    return LawnGrass("Газонная трава", "Элитная трава для газона",
                     500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass_2_product():
    return LawnGrass("Газонная трава 2", "Выносливая трава",
                     450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_middle_price():
    return Category("Пустая категория", "Категория без продуктов", [])
