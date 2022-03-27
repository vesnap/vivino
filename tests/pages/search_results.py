import random
from tests.utils.locators import *
from selenium.webdriver.common.by import By

from tests.pages.page import Page

class SearchResults(Page):
    instance = None

    def __init__(self,driver, base_url):
        super().__init__(driver, base_url)
        self.locator = SearchResultsLocators

    def get_products(self):
        return self.find_elements(*self.locator.PRODUCTS)

    def parse_products(self, product_list):
        products = []
        for product in product_list:
            prodobj = {}
            prodobj["image"] = self.get_attr(product.find_element(*self.locator.PRODUCT_IMAGE), "style")
            prodobj["winery"] = self.get_text(product.find_element(*self.locator.PRODUCT_TEXT))
            prodobj["region"] = self.get_text(product.find_element(*self.locator.PRODUCT_REGION))
            prodobj["avarage"] = self.get_text(product.find_element(*self.locator.PRODUCT_AVARAGE)).split("\n")[1]
            products.append(prodobj)
        return products

    def click_on_product(self, product):
        product.find_elements(By.CSS_SELECTOR, "*")[2].click()
