import os


def dish(file):
    """ключ - name_dish и списком ингредиентов - ingredients"""
    name_dish = file.readline().strip()
    count_ingredient = int(file.readline().strip())
    ingredients = list()
    for ingredient in range(count_ingredient):
        ingredient_name, quantity, measure = file.readline().strip().split(" | ")
        ingredients.append({'ingredient_name': ingredient_name,
                            'quantity': int(quantity),
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


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    shop_list = dict()
    for food in dishes:
        for ingredient in cook_book[food]:
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': ingredient['measure'],
                                              'quantity': ingredient['quantity']*person_count}
            else:
                shop_list[ingredient_name]['quantity'] += ingredient['quantity']*person_count
    return shop_list


def print_cook_book(book: dict):
    for key, value in book.items():
        print(f'{key} :')
        for i in value:
            print(i)
        print("---------")


def print_shop_list(shop_list: dict):
    for key, value in shop_list.items():
        print(f'{key} : {value}')
    print('--------------')


base_path = os.getcwd()
file_dir = 'books'
file_name = "recipes.txt"
file_path_all = os.path.join(base_path, file_dir, file_name)

cook_book = dict()

file_to_dict(file_path_all, cook_book)

print(file_path_all)

print_cook_book(cook_book)

print_shop_list(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2))
print_shop_list(get_shop_list_by_dishes(['Омлет', 'Омлет'], 1))
print_shop_list(get_shop_list_by_dishes(['Омлет'], 2))