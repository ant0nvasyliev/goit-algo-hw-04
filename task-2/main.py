from pathlib import Path

path = Path('task-2/cats-data.txt')

def get_cats_info(path):
    try:
        with open(path, "r", encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()]
            list_cats_data = []
            for line in lines:
                id, name, age = line.split(',')
                cat_data = {'id': id, 'name': name, 'age': age}
                list_cats_data.append(cat_data)
            return list_cats_data
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
         

about_cats = get_cats_info(path)
print(about_cats)