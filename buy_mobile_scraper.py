from bs4 import BeautifulSoup
import requests
import csv
import time

csv_file = open("buy_mobile_scraper.csv",'w')
csv_write = csv.writer(csv_file)
csv_write.writerow(['Item','Title','Price','Image_link','Purchase_link'])

def get_product_details(url):
    print(url)
    from selenium import webdriver

    PATH = '/home/promise/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(PATH,options=options)
    driver.get(url)


    source = driver.page_source
    soup = BeautifulSoup(source,'lxml')
    products = soup.find('div',class_='row catebg')\
        .find_all('div',class_='product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12')
    for product in products:
        try:
            item = product.find('div',class_='caption').h4.a.text.split()[0]
            if item == "iPhone":
                item = item.replace("iPhone","Apple")
            if item == "Iphone":
                item = item.replace("Iphone","Apple")
            # print("item: ",item)
            title = product.find('div',class_='caption').h4.a.text
            # print("title: ", title)
            image_link = product.find('div',class_='image').img['src']
            # print("image_link: ", image_link)
            purchase_link = product.find('div',class_='image').a['href']
            # print("purchase_link: ", purchase_link)
            price = product.find('p', class_='price').text.split('৳')[1]
            # print("price: ", price)
            csv_write.writerow([item,title,price,image_link,purchase_link])

        except:
            price = product.find('span', class_='price-new').text.split('৳')[1]
            # print("price: ",price)
            csv_write.writerow([item, title, price, image_link, purchase_link])




def checking_next_page(url):
    page_number = 2
    while page_number <= 35:
        try:
            base_url = url
            link_updated = base_url + '?page=' + str(page_number)
            get_product_details(link_updated)
            page_number += 1
        except:
            break


products_url = ['https://www.buymobile.com.bd/latest-mobile-phone']

for url in products_url:
    get_product_details(url)
    checking_next_page(url)


csv_file.close()



