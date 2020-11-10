from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

# without indentation
# print(soup)

# indentation html file
# print(soup.prettify())

# it will return only the first element
# match = soup.title.text
# match = soup.div
# print(match)

# if i want to find specific element then we should use "find" method
# class hossche python er special character tai "class_" use kora hoise
# specific_match = soup.find('div',class_="footer")
# print(specific_match)

# here we find the element from "browser inspect"
# article = soup.find('div',class_='article')
# print(article)

# if we want a specific element to show of that finded element then do following
# headline = article.h2.a.text
# print(headline)
# summary = article.p.text
# print(summary)

# this is very important section
# for find all the element we will use "find_all" instead find method
# it will return a list of tags which match those "arguments"

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)
    print()









