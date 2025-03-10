import json
import os
from src.main import Product, Category


def read_json(path: str) -> dict:
    fill_path = os.path.abspath(path)
    with open(fill_path, 'r', encoding='UTF-8') as json_file:
        data = json.load(json_file)
    return data


def create_object(data: dict):
     categories_list = []
     for categories in data:
         products_list = []
         for products in categories.get('products'):
             products_list.append(Product(**products))
         categories['products'] = products_list
         categories_list.append(Category(**categories))
     return categories_list



if __name__ == '__main__':
     raw_data = read_json('../data/products.json')
     categories_list = create_object(raw_data)
     print(categories_list[0].name)
     print(categories_list[0].description)