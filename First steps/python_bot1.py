import requests
import re



def liczba_chorych():
    page = requests.get('https://www.worldometers.info/coronavirus/country/poland/')
    pattern = r'Poland Coronavirus: (\d\d,{0,1}\d{0,})'
    obj = re.search(pattern, page.text)
    return (obj.group(1))

with open('data.txt', 'r') as f:
    SAVED_DATA = f.readline()

CURENT_DATA = liczba_chorych()

if SAVED_DATA != CURENT_DATA:
    with open('data.txt', 'w') as f:
        f.write(str(CURENT_DATA))
    print(f"nowe dane {CURENT_DATA} osób chorych""\n")
else:
    print("Nic nowego.""\n")




