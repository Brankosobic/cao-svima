#This is a basic scraper which i modify to scrape some info that i need
from bs4 import BeautifulSoup
import requests
import csv
import lxml
izvorni = requests.get('https://www.kupujemprodajem.com/search.php?action=list&submit%5Bsearch%5D=Tra%C5%BEi&dummy=name&data%5Bkeywords%5D=beli%20luk').text

soup = BeautifulSoup(izvorni, 'lxml')
csv_file = open('beliLuk.csv', 'w')

csv_pisac = csv.writer(csv_file)
csv_pisac.writerow(['naslovOglasa', 'kolicinaPregleda', 'kolkoPara'])

for clan in soup.find_all(class_='item clearfix'):
    try:
        naslov= clan.a.img['alt']
        naslov = naslov.strip()
        cena = clan.find('span',class_='adPrice').text
        cena = cena.strip()
        pregledi= clan.find('div', class_= 'view-count').text
        pregledi= pregledi.strip()
    except Exception as e:
        naslov = None
    print(naslov)
    print(pregledi)
    print(cena)
    csv_pisac.writerow([naslov, pregledi, cena])

csv_file.close()
