from bs4 import BeautifulSoup
import requests

#r = requests.get("https://www.flipkart.com/search?q=watches&sid=r18/f13&as=on&as-show=on&marketplace=FLIPKART&otracker=start&as-pos=1_1_ic_watches")
r = requests.get("https://www.sapnaonline.com/general-search?searchkey=computer")

c = r.content

soup = BeautifulSoup(c,"html.parser")
#print(soup.prettify)

content = soup.find_all("div",{"class":"row no-margin"})
print(content[0].find("div",{"class":"large-12 twelve small-12 tablet-8 hide-for-small columns product-book-details-text sapna_product_description_tag"}))
print(content[0].find("span",{"class":"discount l_p_off"}).text)
print(content[0].find("span",{"class":"actual-price"}).text.replace(" ",""))
