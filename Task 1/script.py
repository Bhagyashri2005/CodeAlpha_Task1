'''Task 1 - Web Scraping
● Use Python libraries like BeautifulSoup or Scrapy to extract data from websites.
● Identify and collect relevant datasets from public web pages.
● If you don’t code, use automated tools like Octoparse or ParseHub.
● Learn to handle HTML structure and web navigation to gather accurate data.
● Create custom datasets tailored to specific analysis needs.'''

import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/catalogue/page-1.html"

with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Price', 'Availability'])

    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        books = soup.find_all('article', class_='product_pod')
        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            availability = book.find('p', class_='instock availability').text.strip()
            writer.writerow([title, price, availability])

        # Pagination: go to next page
        next_btn = soup.find('li', class_='next')
        if next_btn:
            next_page = next_btn.a['href']
            url = "http://books.toscrape.com/catalogue/" + next_page
        else:
            break

print("Books data saved to 'books.csv'")
