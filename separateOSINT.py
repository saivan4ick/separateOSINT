import requests
from bs4 import BeautifulSoup
from googlesearch import search
from phone import phone_osint
from rich.progress import track
import time
GREEN = "\033[32m"
RED = "\u001b[31m"
BLUE = "\u001b[36m"
YELLOW = "\u001b[33m"
RESET = "\033[0m"

print(f"""
{BLUE}

░██████╗███████╗██████╗░░█████╗░██████╗░░█████╗░████████╗███████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
╚█████╗░█████╗░░██████╔╝███████║██████╔╝███████║░░░██║░░░█████╗░░
░╚═══██╗██╔══╝░░██╔═══╝░██╔══██║██╔══██╗██╔══██║░░░██║░░░██╔══╝░░
██████╔╝███████╗██║░░░░░██║░░██║██║░░██║██║░░██║░░░██║░░░███████╗
╚═════╝░╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝{RESET}
{GREEN}

░█████╗░░██████╗██╗███╗░░██╗████████╗
██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝
██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░
██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░
╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░
░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░  v1.0.2{RESET}""")

def execute_function(choice):
    if choice == "1":
        brand_to_monitor = input("Введите название того что вы хотите мониторить / Enter the name of what you want to monitor: ")
        num_results = int(input("Введите количество результатов поиска для обработки / Enter the number of search results to process: "))
        
        language_choice = input("Выберите язык / Select language (ru - Русский, en - English): ")
        supported_languages = ["ru", "en"]
        if language_choice in supported_languages:
            search_brand_mentions(brand_to_monitor, num_results, lang=language_choice)
        else:
            print("Неподдерживаемый язык / Unsupported language choice.")
    elif choice == "2":
        phone_osint()
        pass
    else:
        print("Неправильный выбор / Invalid choice.")

if __name__ == "__main__":
    print("Выберите действие:")
    print("1. Выполнить поиск упоминаний бренда (searchOSINT) / Perform brand mentions search (searchOSINT)")
    print("2. Выполнить поиск по телефону (phoneOSINT) / Perform search number phone (phoneOSINT)")
    
    user_choice = input("Введите номер выбранного действия / Enter the number of the chosen action: ")
    execute_function(user_choice)