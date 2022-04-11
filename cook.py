import os


def dish(file):
    """ключ - name_dish и списком ингредиентов - ingredients"""
    name_dish = file.readline().strip()
    count_ingredient = int(file.readline().strip())
    ingredients = list()
    for ingredient in range(count_ingredient):
        ingredient_name, quantity, measure = file.readline().strip().split(" | ")
        ingredients.append({'ingredient_name': ingredient_name,
                            'quantity': quantity,
                            'measure': measure})
    return name_dish, ingredients


def file_to_dict(file_path: str, cook_dict: dict):
    """добавляет в словарь из файла"""
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            key, list_ingredients = dish(file)
            cook_dict[key] = list_ingredients
            empty_line = file.readline()
            if not empty_line:
                return


base_path = os.getcwd()
file_dir = 'books'
file_name = "recipes.txt"
file_path_all = os.path.join(base_path, file_dir, file_name)

cook_book = dict()

file_to_dict(file_path_all, cook_book)

print(file_path_all)

for key, value in cook_book.items():
    print(f"{key} : ")
    for ingredient in value:
        print(ingredient)
