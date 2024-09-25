#scraper.py

import requests
from bs4 import BeautifulSoup
import re

def scrape_books():
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []
    for article in soup.find_all('article', class_='product_pod'):
        title = article.h3.a['title']
        
        # Extract the price and convert it to float after removing the currency symbol
        price_str = article.find('p', class_='price_color').text
        
        # Clean the price string to remove any unwanted characters
        cleaned_price_str = re.sub(r'[^\d.]', '', price_str)  # Remove everything except digits and decimal points
        
        try:
            # Convert the cleaned string to float
            price = float(cleaned_price_str)
        except ValueError as e:
            print(f"Error converting price: {price_str} - {e}")
            continue  # Skip this book if there's an error

        availability = article.find('p', class_='instock availability').text.strip()
        rating = article.p['class'][1]
        product_url = "https://books.toscrape.com/catalogue" + article.h3.a['href'][8:]

        book_data = {
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "product_url": product_url
        }
        books.append(book_data)
    
    return books
