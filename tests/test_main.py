from src.main import Category, Product


def test_main_product(test_products):
    assert test_products.name == 'Samsung Galaxy S23 Ultra'
    assert test_products.description == '56GB, Серый цвет, 200MP камера'
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
    assert len(test_category.products_in_list) == 4
    assert Category.category_count == 1
    assert Category.product_count == 4


def test_main_product_in_list(test_category):
    assert test_category.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток:5шт.'
                                              'Iphone 15, 210000.0 руб. Остаток:8шт.'
                                              'Xiaomi Redmi Note 11, 31000.0 руб. Остаток:14шт.'
                                              '55" QLED 4K, 123000.0 руб. Остаток:7шт.')

