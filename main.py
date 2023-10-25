import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
URL = "https://www.amazon.com/SAMSUNG-Inch-Internal-MZ-77E1T0B-AM/dp/B08QBJ2YMG/ref=sr_1_1?crid=334G3RUDPCG22&keywords=evo&qid=1698222309&sprefix=evo%2Caps%2C224&sr=8-1&th=1"
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language" : "el-GR,el;q=0.9,en;q=0.8"
}
response = requests.get(url=URL,headers=header)
response.raise_for_status()
soup = BeautifulSoup(response.text,"lxml")
price = soup.find(name="span", class_="a-offscreen").getText()
price =  float(price.split("$")[1])
print(price)

if price <60:


    with smtplib.SMTP("smtp.gmail.com") as connection:
        message=f"Subject: SAMSUNG 870 EVO SATA III SSD 1TB FELL UNDER 60$: % \n\n SAMSUNG 870 EVO SATA III SSD 1TB 2.5” Internal Solid State Hard Drive, Upgrade PC or Laptop Memory and Storage for IT Pros, Creators, Everyday Users, MZ-77E1T0B/AM FELL UNDER 60$ ON AMAZON BOI"
        message.encode("UTF-8")
        connection.starttls()
        connection.login(user=, password=)
        connection.sendmail(from_addr=,
                            to_addrs=",
                            msg=(message).encode('utf-8'))