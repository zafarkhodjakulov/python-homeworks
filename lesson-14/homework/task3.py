import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
# chrome_options.add_argument("--headless")  
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--window-position=-2500,-200")
chrome_options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

URL = "https://www.demoblaze.com/"
driver.get(URL)
time.sleep(3) 

driver.find_element(By.LINK_TEXT, "Laptops").click()
time.sleep(3)

driver.find_element(By.ID, "next2").click()
time.sleep(3)

laptops_data = []

def scrape_page():
    """Bitta sahifada joylashgan barcha laptoplarni scraping qilish"""
    items = driver.find_elements(By.CLASS_NAME, "card-block")

    for item in items:
        try:
            name = item.find_element(By.TAG_NAME, "h4").text.strip()
            price = item.find_element(By.TAG_NAME, "h5").text.strip()
            description = item.find_element(By.TAG_NAME, "p").text.strip()

            laptops_data.append({
                "name": name,
                "price": price,
                "description": description
            })
        except:
            continue 

def scrape_all_pages():
    """Hamma sahifalardagi ma'lumotlarni yig'ish"""
    while True:
        scrape_page()
        try:
            next_button = driver.find_element(By.ID, "next2")
            if next_button.is_enabled():
                next_button.click()
                time.sleep(3)  
            else:
                break
        except:
            break 

scrape_all_pages()

driver.quit()

with open("laptops.json", "w", encoding="utf-8") as json_file:
    json.dump(laptops_data, json_file, indent=4, ensure_ascii=False)

print("Laptop ma'lumotlari laptops.json fayliga saqlandi!")
