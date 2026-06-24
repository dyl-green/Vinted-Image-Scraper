from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import json


def alter_title(title):
    return title.split(",")[0].strip().lower().replace(" ", "-").replace("'", "").replace("%", "")

member_url = "https://www.vinted.com/member/256710934"
member_item_urls = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(member_url)

    page.wait_for_timeout(2000) # Give the page time to load
    # Scoll down to load all items, I want to fins a better way fpr this eventually
    # For now, I'll use a simple scroll approach

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(2000) # Give the page time to load the new items
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(2000) # Give the page time to load the new items
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(2000) # Give the page time to load the new items  
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(2000) # Give the page time to load the new items  


    

    html = page.content()
    soup = BeautifulSoup(html, 'html.parser')


    # Find all items using <a> tags & class selector
    items = soup.find_all('a', class_="new-item-box__overlay new-item-box__overlay--clickable")

    # Concatonate the names of the items for the url string 
    item_urls = ["www.vinted.com" + item['href'] + "/" + alter_title(item['title']) for item in items]
    member_item_urls.extend(item_urls)

    print(item_urls)


    browser.close()

print(member_item_urls)
