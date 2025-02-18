import requests
from bs4 import BeautifulSoup
import json

# GTO Ana Sayfasının URL'si
url = "https://www.gebzeto.org.tr/"

# Sayfayı çekme
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Duyuruların bulunduğu div'i bul
duyurular_listesi = []
duyurular = soup.find_all("h2", class_="su-post-title")

# Duyuruları çekme
for duyuru in duyurular:
    baslik = duyuru.find("a").text.strip()
    link = duyuru.find("a")["href"]
    duyurular_listesi.append({"baslik": baslik, "link": link})

# JSON olarak kaydetme
json_dosyasi = "duyurular.json"
with open(json_dosyasi, "w", encoding="utf-8") as dosya:
    json.dump(duyurular_listesi, dosya, ensure_ascii=False, indent=4)
