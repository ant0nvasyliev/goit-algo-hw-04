from pathlib import Path

path = Path('task-1/salary-data.txt')

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()]
            total = 0
            for line in lines:
                _, salary = line.split(',')
                total += int(salary)
            average = total / len(lines)
            average = int(average)
        print(f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}')         
        return total, average
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")

total_salary(path)