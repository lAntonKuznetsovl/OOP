import json

from config import PATH_TO_JSON
from src.category import Category
from src.product import Product


def reading_json(path_to_file: str) -> dict:
    """Функция долучения данных из json файла"""
    with open(path_to_file, encoding="UTF-8") as file:
        data_from_json = json.load(file)
    return data_from_json


data = reading_json(PATH_TO_JSON)

def create_object_from_json(data_from_json: dict):
    """Функция создания объектов класса на основе данных из json файла"""
    product_objects = []
    categories_objects = []
    for category in data_from_json:
        categories_objects.append(Category(**category))
        for element in category['products']:
            product_objects.append(Product(**element))
    return categories_objects, product_objects


if __name__ == "__main__":
    result = create_object_from_json(data)
    print(result)
