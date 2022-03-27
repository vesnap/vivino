
from tests.pages.page import Page
from tests.utils.helpers import *
from tests.utils.locators import *
class Product(Page):
    def __init__(self,driver,base_url):
        self.locator = ProductPageLocators
        super().__init__(driver,base_url)

    def get_image_href(self):
        return self.driver.find_element(*self.locator.IMAGE).get_attribute("src")
    def get_winery(self):
        self.driver.implicitly_wait(1000)
        return get_all_children(self.driver.find_element(*self.locator.HEADING))[1].text
    def get_vine_name(self):
        self.driver.implicitly_wait(1000)
        return get_all_children(self.driver.find_element(*self.locator.HEADING))[2].text
    def get_review(self):
        return self.driver.find_element(*self.locator.PRODUCT_RATING).find_elements(By.CSS_SELECTOR,"*")[1].text



