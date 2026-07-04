import requests
from bs4 import BeautifulSoup

def get_takealot_price(product_url):
    """Scrapes product name and price from Takealot"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.find('h1').get_text().strip()
    price_element = soup.find('span', {'data-ref': 'buybox-price-main'})
    price = price_element.get_text().strip() if price_element else "Price not found"
    
    return f"Product: {title}\nPrice: {price}"

if __name__ == "__main__":
    url = "https://www.takealot.com/apple-iphone-15/PLID94984488"
    print(get_takealot_price(url))
