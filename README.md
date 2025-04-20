
### Установка
1. Клонирование репозитория:
```
git@github.com:Rus-khai/OOP.Lesson1.git
```
## Модуль main.py
### **Классы:**
#### **class Product(PrintMixin, BaseProduct):**
#### **class Category:**
#### **class LawnGrass(Product):**
#### **class Smartphone(Product):**
#### **class BaseProduct(ABC):**

## Tests:
### **conftest.py:**
### **test_main.py:**
ef1073e786e10ce16bd2aa2bd1575049

 mock_lict = {
                  "pagination": {
                                "limit": 100,
                                "offset": 0,
                                "count": 100,
                                "total": 100
                                },
                  "data": [
                         {
                          "open": 248.0,
                          "high": 249.98,
                          "low": 244.91,
                          "close": 247.04,
                          "volume": 46872348.0,
                          "adj_high": 250.0,
                          "adj_low": 244.91,
                          "adj_close": 247.04,
                          "adj_open": 248.0,
                          "adj_volume": 47275651.0,
                          "split_factor": 1.0,
                          "dividend": 0.0,
                          "symbol": "AAPL",
                          "exchange": "XNAS",
                          "date": "2025-02-25T00:00:00+0000"
                          }
                         ]
                  }
    mock_get_1.return_value.json.return_value = mock_lict
    assert get_share_price() == [{'stock': 'AAPL', 'price': 247.04},
                                 {'stock': 'NVDA', 'price': 247.04},
                                 {'stock': 'MSFT', 'price': 247.04},
                                 {'stock': 'AMZN', 'price': 247.04},
                                 {'stock': 'GOOGL', 'price': 247.04}]
