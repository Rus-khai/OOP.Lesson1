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
    assert test_products_4.name == '55\" QLED 4K'
    assert test_products_4.description == 'Фоновая подсветка'
    assert test_products_4.price == 123000.0
    assert test_products_4.quantity == 7



def test_main_category(test_category):
    assert test_category.name == 'Смартфоны'
    assert test_category.description == ("Смартфоны, как средство не только коммуникации, "
                         "но и получения дополнительных функций для удобства жизни")
    assert test_category.products == [Product("Samsung Galaxy S23 Ultra",
                                              "256GB, Серый цвет, 200MP камера", 180000.0, 5),
                                      Product("Iphone 15",
                                              "512GB, Gray space", 210000.0, 8),
                                      Product("Xiaomi Redmi Note 11",
                                              "1024GB, Синий", 31000.0, 14)]


def test_main_category_1(test_category_1):
    assert test_category_1.name == 'Телевизоры'
    assert test_category_1.description == ("Современный телевизор, который позволяет наслаждаться просмотром, "
                                           "станет вашим другом и помощником")
    assert test_category_1.products == [Product("55\" QLED 4K","Фоновая подсветка", 123000.0, 7)]


def test_main_len_products(test_category):
    assert len(test_category.products) == 3
    assert Category.category_count == 3
    assert Category.product_count == 3
