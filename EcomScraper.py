import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=a71e245a-0065-428b-a216-504221a288da&as-backfill=on&page=1"

r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text, "lxml")

container = soup.find("div", class_="_1YokD2 _3Mn1Gg")

product_name = []
product_price = []
product_rating = []
product_description = []
product_img = []
product_actual_price = []
product_discount = []

names = container.find_all("div", class_="_4rR01T")

# prod_name = prod.find("div", class_="_4rR01T")

for i in names:
    product_name.append(i.text)
    
print(product_name)
print(len(product_name))

prices = container.find_all("div", class_="_30jeq3 _1_WHN1")

for i in prices:
    product_price.append(i.text)

print(product_price)
print(len(product_price))


ratings = container.find_all("div", class_="_3LWZlK")

for i in ratings:
    product_rating.append(i.text)

print(product_rating)
print(len(product_rating))

imgs = container.find_all("img", class_="_396cs4")

print(imgs)

for i in imgs:
    # print(i['src'])
    product_img.append(i['src'])

print(product_img)
print(len(product_img))


actual_prices = container.find_all("div", class_="_3I9_wc _27UcVY")

for i in actual_prices:
    product_actual_price.append(i.text)

print(product_actual_price)
print(len(product_actual_price))


discount_div = container.find_all("div", class_="_3Ay6Sb")

for i in discount_div:
    product_discount.append(i.span.text)
    
print(product_discount)
print(len(product_discount))
    
    





# for i in range(2, 10):
#     # print(soup.prettify())
    
#     url = "https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=a71e245a-0065-428b-a216-504221a288da&as-backfill=on&page="+str(i)
    
#     r = requests.get(url)
#     # print(r)
#     soup = BeautifulSoup(r.text, "lxml")

#     np = soup.find("a", class_="_1LKTO3").get("href")
#     cnp = "https://www.flipkart.com" + np
#     print(cnp)
