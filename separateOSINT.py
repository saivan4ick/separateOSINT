import requests
from bs4 import BeautifulSoup
from googlesearch import search

# ANSI escape-коды для цветового форматирования
GREEN = "\033[32m"
RED = "\u001b[31m"
BLUE = "\u001b[36m"
YELLOW = "\u001b[33m"
RESET = "\033[0m"

print(f"""
{RED}

░██████╗███████╗██████╗░░█████╗░██████╗░░█████╗░████████╗███████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
╚█████╗░█████╗░░██████╔╝███████║██████╔╝███████║░░░██║░░░█████╗░░
░╚═══██╗██╔══╝░░██╔═══╝░██╔══██║██╔══██╗██╔══██║░░░██║░░░██╔══╝░░
██████╔╝███████╗██║░░░░░██║░░██║██║░░██║██║░░██║░░░██║░░░███████╗
╚═════╝░╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝{RESET}
{BLUE}

░█████╗░░██████╗██╗███╗░░██╗████████╗
██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝
██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░
██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░
╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░
░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░  v1.0.0{RESET}""")

def search_brand_mentions(brand_name, num_results=5):
    search_query = f"{brand_name} mentions"
    search_results = search(search_query, num_results=num_results, lang="en")
    for url in search_results:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            if brand_name.lower() in text.lower():
                print(f"{GREEN}Brand {brand_name} mentioned in: {url}{RESET}\n")
        except Exception as e:
            print(f"{RED}An error occurred while processing {url}: {e}{RESET}\n")
if __name__ == "__main__":
    brand_to_monitor = input(f"Enter the brand name to monitor: ")
    num_results = int(input(f"Enter the number of search results to process: "))
    search_brand_mentions(brand_to_monitor, num_results)
input()
