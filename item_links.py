from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import json

url = "https://www.vinted.com/member/256710934"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)

    page.wait_for_timeout(2000) # Give the page time to load

    
    html = page.content()
    soup = BeautifulSoup(html, 'html.parser')

    # Scoll down to load all items

    # Find all items using <a> tags & class selector
    items = soup.find_all('a', class_="new-item-box__overlay new-item-box__overlay--clickable")


    item_urls = [item['href'] + item['title'] for item in items]
    print(item_urls)

    # Concatonate the names of the items for the url string 



    browser.close()

soup = BeautifulSoup(html, 'html.parser')

