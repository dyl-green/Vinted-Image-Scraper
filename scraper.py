from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import json


def extract_item_info(soup):

    title = soup.find('h1', class_="web_ui__Text__text web_ui__Text__title web_ui__Text__left").text
    print(f"Title: {title}")

    description = soup.find('span', class_="web_ui__Text__text web_ui__Text__body web_ui__Text__left web_ui__Text__format").text
    print(f"Description: {description}")

    return title, description


url = "https://www.vinted.com/member/256710934"

url = "https://www.vinted.com/items/9176775363-vintage-nike-track-pants-large-navy-blue-baggy-lined-y2k-grunge-skater"


item = 1
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)

    page.wait_for_timeout(2000) # Give the page time to load
    # Much shorter, safer, and less prone to breaking
    # Direct click using your exact selector path
    
    page.locator("html body.v_inter_b0f5c119-module__kyvDTG__className div.next-page div.standard-layout.is-wide main.site.u-background-white div div.site-content div.container div.row.u-position-relative div#content.grid12 div.body-content main.item-information div#content.item-page-content section.item-main section.item-photos__container div.item-photos figure.item-description.u-flexbox.item-photo.item-photo--5 button.item-thumbnail").click()
    
    page.wait_for_timeout(2000) # Give the page time to load

    html = page.content()

    soup = BeautifulSoup(html, 'html.parser')

    images = soup.find_all('img', class_="image-carousel__image")
    image_count = 0
    for img in images:

        image_count += 1
        current_image = img['src']

        response = page.request.get(current_image)
        
        if response.status == 200:
            # Write the image bytes directly to a local file
            save_path = f"image_{item}_{image_count}.jpg"
            with open(save_path, "wb") as file:
                file.write(response.body())
            print(f"Success: Saved image to {save_path}")
        else:
            print(f"Failed to fetch image. Status code: {response.status}")
            
    #extract_item_info(soup)
    browser.close()
    