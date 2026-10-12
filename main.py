from bs4 import BeautifulSoup
import pandas as pd

html_content = """
<div class="product-card">
    <span class="title">Смартфон Apple iPhone 15</span>
    <span class="price old-price">95000 руб</span>
    <span class="price current-price">89000 руб</span>
</div>
<div class="product-card">
    <span class="title">Смартфон Samsung Galaxy S24</span>
    <span class="price current-price">79000 руб</span>
</div>
<div class="product-card">
    <span class="title">Смартфон Xiaomi 14</span>
    <span class="price old-price">65000 руб</span>
    <span class="price current-price">55000 руб</span>
</div>
<div class="product-card">
    <span class="title">Смартфон Google Pixel 8</span>
    <span class="price current-price">69000 руб</span>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

blocks_div = soup.find_all('div', class_='product-card')

data = []

for block_div in blocks_div:
    old_price = block_div.find(class_="price old-price")
    if old_price:
        title = block_div.find(class_="title").text
        old_price_val = int(block_div.find(class_="price old-price").text.replace(" руб", ""))
        price = int(block_div.find(class_="price current-price").text.replace(" руб", ""))
        discount = old_price_val - price

        data.append({
                'Название': title,
                'Старая цена': old_price_val,
                'Новая цена': price,
                'Скидка': discount
        })

df = pd.DataFrame(data)

df.to_excel('discounts.xlsx', index=False)