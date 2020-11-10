from bs4 import BeautifulSoup
import requests
import time
import csv

csv_file = open('sumash.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Item','Title','Price','Image_link'])


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/promise/chromedriver"
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument("--start-fullscreen")
# driver = webdriver.Chrome(PATH)
# driver.get('https://www.sumash-tech.com/collection/apple')


# popup closed
# WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH,"//a[@title='Close']"))).click()

# not clickable the "next page" element because of overlapping!! how to solve this?????
# WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH,"//span[text()='»']"))).click()




def get_product_details(brand,url):
    print(url)
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')

    for product in soup.find_all('div',class_='row items'):
       try:
           product_items = product.find_all('div', class_='item')
           for i in product_items:
               product_details = i.find('div', class_="item-single-product")
               title = product_details.span.text
               # print(title)
               price = product_details.find('span', class_='price').text.split("BDT")[1]
               # print(price)
               image_link = product.find('div', class_='slide transform').img['src']
               # print(image_link)
               csv_writer.writerow([brand,title,price,image_link])
       except:
            image_link = None




products_url =[('Apple','https://www.sumash-tech.com/collection/apple'),
               ('Oppo','https://www.sumash-tech.com/collection/oppo'),
               ('Samsung','https://www.sumash-tech.com/collection/samsung'),
               ('xiaomi','https://www.sumash-tech.com/collection/xiaomi'),
               ('huawei','https://www.sumash-tech.com/collection/huawei'),
               ('honor','https://www.sumash-tech.com/collection/honor'),
               ('realme','https://www.sumash-tech.com/collection/realme'),
               ('asus','https://www.sumash-tech.com/collection/asus'),
               ('vivo','https://www.sumash-tech.com/collection/vivo'),
               ('oneplus','https://www.sumash-tech.com/collection/oneplus'),
               ('umidigi','https://www.sumash-tech.com/collection/umidigi'),
              ]

for url in products_url:
    get_product_details(url[0],url[1])

csv_file.close()