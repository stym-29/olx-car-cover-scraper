from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv

options = webdriver.ChromeOptions()
options.add_argument("--headless")
service = Service()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.olx.in/items/q-car-cover")
time.sleep(5)
items = driver.find_elements(By.CSS_SELECTOR, "li.EIR5N")

with open("olx_car_covers.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Location", "URL"])
    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, "span._2tW1I").text
            price = item.find_element(By.CSS_SELECTOR, "span._89yzn").text
            location = item.find_element(By.CSS_SELECTOR, "span._2FRXm").text
            url = item.find_element(By.TAG_NAME, "a").get_attribute("href")
            writer.writerow([title, price, location, url])
        except:
            continue

driver.quit()
print("Scraping completed. Data saved to olx_car_covers.csv")
