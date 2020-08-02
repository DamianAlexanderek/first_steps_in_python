import re
import requests
import datetime

def aktualny_kurs_euro():
    page = requests.get('https://www.nbp.pl/home.aspx?f=/kursy/kursya.html')
    pattern = r'<td class="bgt2 left"> euro </td> <td class="bgt2 right">1 EUR</td> <td class="bgt2 right">(\d,{0,1}\d{4})'
    obj = re.search(pattern, page.text)
    return(f'Aktualny kurs z dnia {datetime.datetime.now().strftime("%B %d, %Y")} = {obj.group(1)}')


d = datetime.datetime.now().strftime("%B %d, %Y")
with open('data4.txt', 'r') as f:
    KURS = f.readline()

EURO = aktualny_kurs_euro()

if EURO >= "4,5000":
    with open('data4.txt', 'w') as f:
        f.write(str(EURO))
        print(f'{EURO} - NIE SPRZEDAWAJ, TRZYMAJ W SKARPECIE!!!''\n')
else:
    print(f'{EURO} - SPRZEDAWAJ I JEDŹ NA WAKACJE W POLSKĘ!!!''\n')
