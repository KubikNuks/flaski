import requests 
from bs4 import BeautifulSoup

url = 'https://www.bankier.pl/gielda/notowania/akcje'

response = request.get(url)
status = response.status_code
print(status)