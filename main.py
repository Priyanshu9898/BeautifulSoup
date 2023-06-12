import requests

url = "https://timesofindia.indiatimes.com/?from=mdr"

def fetchAndSaveData(url, path):
    r = requests.get(url);
    # print(r.text)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

fetchAndSaveData(url, "data/times.html")