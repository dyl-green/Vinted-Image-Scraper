from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import json


url = "https://www.vinted.com/member/256710934"

url = "https://www.vinted.com/items/9176775363-vintage-nike-track-pants-large-navy-blue-baggy-lined-y2k-grunge-skater"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    html = page.content()
    browser.close()

soup = BeautifulSoup(html, 'html.parser')