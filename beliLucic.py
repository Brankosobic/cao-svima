from bs4 import BeautifulSoup
import requests
import csv
import lxml

# u izvorni fajl ubaciti web stranicu u htmlu i pretvoriti je u tekst sa .text
izvorni = requests.get('https://www.kupujemprodajem.com/search.php?action=list&submit%5Bsearch%5D=Tra%C5%BEi&dummy=name&data%5Bkeywords%5D=beli%20luk').text
# u soup variablu ubaciti taj izvorni tekstualni 
# fajl u obliku klase iliti funkcije 
# "BeaSou" sa parametrima(variabla u kojoj je
# url , i parser; u ovom slucaju lxml parser)
soup = BeautifulSoup(izvorni, 'lxml')

# ovo dole sluzi za ispis tog izvornog html fajla u terminalu
# print(soup.prettify())

# otvara csv fajl(imena kurseviPitona.csv) sa pisanje parametrom
csv_file = open('beliLuk.csv', 'w')

csv_pisac = csv.writer(csv_file)
csv_pisac.writerow(['naslovOglasa', 'kolicinaPregleda', 'kolkoPara'])

# iteratovati po clan u variabli = soup.find_all('article')
# for clan in 
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
# traj eksept je tu u slucaju da od neke kutije(kontejnera)
# fali komadic, pa ako fali da popuni sa None
#     try:
#         videoSnimak = clan.find('iframe', class_='youtube-player')['src']
#         vieoLink = videoSnimak.split('/')[4]
#         vieoLink = vieoLink.split('?')[0]
#         konacniLink = "https://youtube.com/watch?v=" + vieoLink
#         naslov = clan.h2.a.text
#         tekst = clan.find('div', class_='entry-content').p.text
#     except Exception as e:
#         konacniLink = None
#         naslov =None
#         tekst = None
#     print(konacniLink)
#     print(tekst)
#     print(naslov)

    csv_pisac.writerow([naslov, pregledi, cena])

csv_file.close()