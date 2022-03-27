from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import sys
import random


keyword=sys.argv[1]
driver = webdriver.Chrome()
driver.get("https://www.vivino.com")
search=driver.find_element(By.CSS_SELECTOR,'input[aria-label="Search any wine"]')
search.send_keys(keyword)
search.send_keys(Keys.ENTER)
product_list=driver.find_elements(By.CLASS_NAME,'card.card-lg')
products=[]
for product in product_list:
    prodobj={}
    prodobj["image"]=product.find_element(By.CLASS_NAME,"wine-card__image").get_attribute("style")
    prodobj["text"] = product.find_element(By.CLASS_NAME, "link-color-alt-grey").text
    prodobj["region"] = product.find_element(By.CLASS_NAME, "text-block.wine-card__region").text
    prodobj["avarage"] = product.find_element(By.CLASS_NAME, "average__container").text
    products.append(prodobj)
random_product=random.choice(product_list)

random_product.find_elements(By.CSS_SELECTOR,"*")[2].click()
image=driver.find_element(By.TAG_NAME,"img")
image_url=image.get_attribute("src")
print(image_url)
driver.implicitly_wait(1000)
product_winery=driver.find_element(By.TAG_NAME,'h1').find_elements(By.CSS_SELECTOR,"*")[1]
product_name=driver.find_element(By.TAG_NAME,'h1').find_elements(By.CSS_SELECTOR,"*")[2]
product_rating=driver.find_element(By.CSS_SELECTOR,'a[href="#all_reviews"]')
print("winery "+product_winery.text+" name "+product_name.text+" rating "+product_rating.find_elements(By.CSS_SELECTOR,"*")[1].text)


