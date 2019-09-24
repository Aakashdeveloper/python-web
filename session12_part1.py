from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

myurl='https://www.flipkart.com/search?q=iphone&otracker=start&as-show&as=off'

uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")


containers = page_soup.findAll("div",{"class":"col col-5-12 _2o7WAb"})
#print(len(containers))

#print(soup.prettify(containers[0]))

container = containers[0]
#print(container)
price = container.findAll("div",{"class":"_6BWGkk"})

#print(price[0].text)

container1 = page_soup.findAll("div",{"class":"col col-7-12"})
#print(container1)
rating = container1[0].findAll("div",{"class":"hGSR34"})
#print(rating[0].text)


for container in containers:
    price_cont = container.findAll("div",{"class":"_6BWGkk"})
    price = price_cont[0].text.strip()

    print(price)

