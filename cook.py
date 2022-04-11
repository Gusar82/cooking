import os


def dish(name: str, count_ingredient: int, ingredients: list) -> dict:
    """Создает словарь с одним ключом - name,
     и значением - список словарей в количестве count_ingredient"""
    pass


def file_to_dict(file_path: str, cook_dict: dict):
    """добавляет в словарь из файла"""
    pass


base_path = os.getcwd()
file_dir = 'books'
file_name = "recipes.txt"
file_path_all = os.path.join(base_path, file_dir, file_name)

cook_book = dict()

file_to_dict(file_path_all, cook_book)

print(file_path_all)
print(cook_book)
