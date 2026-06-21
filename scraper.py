from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import json


url = "https://www.vinted.com/member/256710934"

url = "https://www.vinted.com/items/9176775363-vintage-nike-track-pants-large-navy-blue-baggy-lined-y2k-grunge-skater"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    page.wait_for_timeout(2000) # Give the page time to load

    html = page.content()
    browser.close()

soup = BeautifulSoup(html, 'html.parser')

title = soup.find('h1', class_="web_ui__Text__text web_ui__Text__title web_ui__Text__left").text
print(f"Title: {title}")

description = soup.find('span', class_="web_ui__Text__text web_ui__Text__body web_ui__Text__left web_ui__Text__format").text
print(f"Description: {description}")