import requests
from bs4 import BeautifulSoup
import pandas as pd

w = requests.get("https://www.magicbricks.com/independent-house-for-sale-in-nalgonda-pppfs")
g = w.content

soup = BeautifulSoup(g,"html.parser") 
# print(soup.prettify())

all = soup.find_all("div",{"data-citycode":"2111"})
ex = all[0].find_all_next("div",{"class":"m-srp-card__price"})
zx = all[0].find("div",{"class":"m-srp-card__price"}).text.replace("\n","").replace(" ","")
q = all[0].find("span",{"class":"m-srp-card__title"}).text.replace("\n"," ").replace(" "," ")
e = all[0].find("div",{"class":"m-srp-card__summary__info"}).text.replace("\n","").replace(" ","")
# print(e)

h = []
for item in all:
    s = {}
    print("\n")
    s["Category"] = "House"
    s["Price"] = (item.find("div",{"class":"m-srp-card__price"}).text.replace("\n","").replace(" ",""))
    s["Address"] = (item.find_all("span",{"class":"m-srp-card__title"})[0].text.replace("\n"," ").replace(" "," "))
    s["SquareFeet"] = (item.find_all("div",{"class":"m-srp-card__summary__info"})[0].text.replace("\n","").replace(" ",""))

    h.append(s)
    # print(h)

    df = pd.DataFrame(h, index=None)
    print(df)
    df.to_csv("extract1.csv")

    # print(len(h))
    

