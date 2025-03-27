import pytest

from src.main import Category, Product


def test_main_product(test_products):
    assert test_products.name == 'Samsung Galaxy S23 Ultra'
    assert test_products.description == '256GB, Серый цвет, 200MP камера'
    assert test_products.price == 180000.0
    assert test_products.quantity == 5


def test_main_product_2(test_products_2):
    assert test_products_2.name == 'Iphone 15'
    assert test_products_2.description == '512GB, Gray space'
    assert test_products_2.price == 210000.0
    assert test_products_2.quantity == 8


def test_main_product_3(test_products_3):
    assert test_products_3.name == 'Xiaomi Redmi Note 11'
    assert test_products_3.description == '1024GB, Синий'
    assert test_products_3.price == 31000.0
    assert test_products_3.quantity == 14


def test_main_product_4(test_products_4):
    assert test_products_4.name == "55\" QLED 4K"
    assert test_products_4.description == 'Фоновая подсветка'
    assert test_products_4.price == 123000.0
    assert test_products_4.quantity == 7


def test_main_len_products(test_category):
    assert len(test_category.products_in_list) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_main_product_in_list(test_category):
    assert test_category.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток:5шт.\n'
                                      'Iphone 15, 210000.0 руб. Остаток:8шт.\n'
                                      'Xiaomi Redmi Note 11, 31000.0 руб. Остаток:14шт.\n')


def test_set_negative_price(capsys):
    """Тест на попытку установки отрицательной цены."""
    new_product = Product(
        name='Samsung Galaxy S23 Ultra',
        description='256GB, Серый цвет, 200MP камера',
        price=180000.0,
        quantity=8
    )
    new_product.price = -50
    captured = capsys.readouterr()  # Перехватываем вывод в консоль
    assert captured.out.strip().split('\n')[-1] == 'Цена не должна быть нулевая или отрицательная'
    assert new_product.price == 180000.0
    """Тест на установку корректной цены."""
    new_product.price = 100
    assert new_product.price == 100


def test_category_add_product(test_category, test_products_4):
    test_category.add_product(product=Product("55\" QLED 4K",
                                              "Фоновая подсветка",
                                              123000.0,
                                              7))
    assert test_category.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток:5шт.\n'
                                      'Iphone 15, 210000.0 руб. Остаток:8шт.\n'
                                      'Xiaomi Redmi Note 11, 31000.0 руб. Остаток:14шт.\n'
                                      '55" QLED 4K, 123000.0 руб. Остаток:7шт.\n')


def test_new_product(capsys):
    product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_str(test_products):
    assert str(test_products) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток:5шт.'


def test_product_add(test_products, test_products_2, test_products_3):
    assert test_products + test_products_2 == 2580000.0
    assert test_products + test_products_3 == 1334000.0
    assert test_products_2 + test_products_3 == 2114000.0


def test_category_str(test_category):
    assert str(test_category) == "Смартфоны, количество продуктов: 27 шт."


def test_main_smartphone_1_product_init(smartphone_1_product):
    assert smartphone_1_product.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1_product.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1_product.price == 180000.0
    assert smartphone_1_product.quantity == 5
    assert smartphone_1_product.efficiency == 95.5
    assert smartphone_1_product.model == "S23 Ultra"
    assert smartphone_1_product.memory == 256
    assert smartphone_1_product.color == "Серый"


def test_main_smartphone_2_product_init(smartphone_2_product):
    assert smartphone_2_product.name == "Iphone 15"
    assert smartphone_2_product.description == "512GB, Gray space"
    assert smartphone_2_product.price == 210000.0
    assert smartphone_2_product.quantity == 8
    assert smartphone_2_product.efficiency == 98.2
    assert smartphone_2_product.model == "15"
    assert smartphone_2_product.memory == 512
    assert smartphone_2_product.color == "Gray space"


def test_main_smartphone_3_product_init(smartphone_3_product):
    assert smartphone_3_product.name == "Xiaomi Redmi Note 11"
    assert smartphone_3_product.description == "1024GB, Синий"
    assert smartphone_3_product.price == 31000.0
    assert smartphone_3_product.quantity == 14
    assert smartphone_3_product.efficiency == 90.3
    assert smartphone_3_product.model == "Note 11"
    assert smartphone_3_product.memory == 1024
    assert smartphone_3_product.color == "Синий"


def test_main_lawngrass_1_product_init(lawngrass_1_product):
    assert lawngrass_1_product.name == "Газонная трава"
    assert lawngrass_1_product.description == "Элитная трава для газона"
    assert lawngrass_1_product.price == 500.0
    assert lawngrass_1_product.quantity == 20
    assert lawngrass_1_product.country == "Россия"
    assert lawngrass_1_product.germination_period == "7 дней"
    assert lawngrass_1_product.color == "Зеленый"


def test_main_lawngrass_2_product_init(lawngrass_2_product):
    assert lawngrass_2_product.name == "Газонная трава 2"
    assert lawngrass_2_product.description == "Выносливая трава"
    assert lawngrass_2_product.price == 450.0
    assert lawngrass_2_product.quantity == 15
    assert lawngrass_2_product.country == "США"
    assert lawngrass_2_product.germination_period == "5 дней"
    assert lawngrass_2_product.color == "Темно-зеленый"


def test_main_add_product(smartphone_1_product, smartphone_2_product):
    assert smartphone_1_product + smartphone_2_product == 2580000.0


def test_main_add_product_error(smartphone_1_product, smartphone_2_product):
    with pytest.raises(TypeError):
        smartphone_1_product + 1


def test_main_add_product_lawngrass(lawngrass_1_product, lawngrass_2_product):
    assert lawngrass_1_product + lawngrass_2_product == 16750.0


def test_main_add_product_lawngrass_error(lawngrass_1_product, lawngrass_2_product):
    with pytest.raises(TypeError):
        lawngrass_1_product + 1


def test_print_mixin(capsys):
    Product(
        name='Samsung Galaxy S23 Ultra',
        description='256GB, Серый цвет, 200MP камера',
        price=180000.0,
        quantity=5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra,256GB, Серый цвет, 200MP камера,180000.0, 5)"
