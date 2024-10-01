import sys
from log import log_red, log_green

from pathlib import Path


def parse_folder(path):
    try:
        if not path.exists():
            raise FileNotFoundError(f"Path '{path}' does not exist.")
        if not path.is_dir():
            raise NotADirectoryError(f"Path '{path}' is not a directory.")

        for element in path.iterdir():
            if element.is_dir():
                log_red(f"[DIR] {element.name}")
                parse_folder(element)  # Рекурсивний обхід папки
            elif element.is_file():
                log_green(f"[FILE] {element.name}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except NotADirectoryError as e:
        print(f"Error: {e}")

folder_path = Path(sys.argv[1])


print(folder_path)


parse_folder(folder_path)
