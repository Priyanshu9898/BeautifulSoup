import requests

url = "https://www.amazon.in/s?k=iphone&crid=12YCJ829KML6A&sprefix=iphon%2Caps%2C236&ref=nb_sb_noss_2"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def fetchAndSaveData(url, path, headers= headers):
    r = requests.get(url, headers = headers);
    # print(r.text)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

fetchAndSaveData(url, "data/index.html", headers)