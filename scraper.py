from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['header','summary','video_link'])

# get() method return a response object
# to get source code from that response object we will use "get().text"
# source = requests.get()
# print(source)

url = "http://coreyms.com/"
source = requests.get(url).text
# print(source)
soup = BeautifulSoup(source,'lxml')
# print(soup.prettify())


article = soup.find('article')
# print(article.prettify())

# header = article.header.h2.a.text
# print(header)

summary = article.find('div',class_='entry-content').p.text
print(summary)


# vid_src = article.find('iframe',class_='youtube-player')
# print(vid_src)
# print(type(vid_src))

# we can access the tag which is embedded with other tag as "dictionary"
# vid_src = article.find('iframe',class_='youtube-player')['src']
# print(vid_src)
# print(type(vid_src))

# vid_id = vid_src.split('/')[4]
# vid_id = vid_id.split('?')[0]
# print(vid_id)

# yt_link = f'https://youtube.com/watch?v={vid_id}'
# print(yt_link)






# looping for getting all the link exactly

# for article in soup.find_all('article'):
#     header = article.header.h2.a.text
#     print(header)
#
#     summary = article.find('div',class_='entry-content').p.text
#     print(summary)
#
#     try:
#         vid_src = article.find('iframe', class_='youtube-player')['src']
#         vid_id = vid_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]
#         yt_link = f'https://youtube.com/watch?v={vid_id}'
#
#     except:
#         yt_link = None
#     print(yt_link)
#     print()
#     csv_writer.writerow([header,summary,yt_link])
#
# csv_file.close()




























