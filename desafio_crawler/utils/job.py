"""
import sys
from quote import SiteScraper

# Redirecione a saída padrão e de erro para um arquivo de log
sys.stdout = open("/var/log/job.log", "a")
sys.stderr = open("/var/log/job.log", "a")

print("Script job.py iniciado.")

url = "https://quotes.toscrape.com/"
site = SiteScraper(url)
site.get_all_quotes_and_save_to_csv()

# Adicione uma mensagem de conclusão para verificar se o script terminou
print("Script job.py concluído.")

"""
