import requests
from bs4 import BeautifulSoup
import pandas as pd
#from openpyxl.workbook import Workbook

s = requests.get("https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
p = s.content

soup = BeautifulSoup(p,"html.parser")
#print(soup.prettify())

'''if web contain mulity pages we can with this(This information(url) according my source "Udemy")'''
# base_url = "https://www.century21.com/real-estate/new-york-city-wy/LCNYNEWYORKCITY/?p="
# for page in range(0,3,2):
#     print(base_url+str(page))
#     r1 = requests.get(base_url+str(page))
#     c1 = r1.content
#     soup1 = BeautifulSoup(c1, features="html.parser")
#     all = soup1.find_all("div", {"data-zip":"10022"})

'''Exracting div elements'''

all = soup.find_all("div",{"data-zip":"82901"})
k = all[0].find_all_next("a",{"class":"listing-price"})
q = all[0].find("a",{"class":"listing-price"}).text.replace("\n","").replace(" ","")

# print(all)
# print(k)
# print(q)

'''For loop for all items (which we are tried to file csv information with) '''
y = []
for item in all:
    g = {}
    print("\n")
    g["Price"] = (item.find("a",{"class":"listing-price"}).text.replace("\n","").replace(" ",""))#price
    g["Address"] = (item.find_all("div", {"class","property-address"})[0].text.replace("\n","").replace(" ",""))#address
    g["City"] = (item.find_all("div", {"class","property-city"})[0].text.replace("\n","").replace(" ",""))#city
    g["Beds"] = (item.find_all("div", {"class","property-beds"})[0].text.replace("\n","").replace(" ",""))#beds
    try:
        g["Baths"] = (item.find("div",{"class":"property-baths"}).text.replace("\n","").replace(" ",""))#bath
    except:   
        g["Baths"] = " "
    try:
        g["Half Beds"] = (item.find("div",{"class":"property-half-baths"}).text.replace("\n","").replace(" ",""))#half bath
    except:   
        g["Half Beds"] = " "
    try:
        g["Sqft"] = (item.find("div",{"class":"property-sqft"}).text.replace("\n","").replace(" ",""))#sqft
    except:   
        g["Sqft"] = " "

    '''data in to information (csv,...'''

    y.append(g)
    print(y)
    print(len(y))

df = pd.DataFrame(y)
print(df)
#df.to_excel("Output.xlsx")
df.to_csv("Output1.csv")