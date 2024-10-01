from colorama import Fore

def log_green(message):
    print(f"{Fore.GREEN} [FILE] {Fore.RESET} {message}")

def log_red(message):
    print(f"{Fore.RED} [FOLDER] {Fore.RESET} {message}")
