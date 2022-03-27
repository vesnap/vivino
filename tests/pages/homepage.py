from selenium.webdriver import Keys
from tests.utils.locators import *
from tests.pages.page import Page

#Homepage is page used for performing the search
class Homepage(Page):
    instance = None

    def __init__(self,driver,base_url):
        super().__init__(driver,base_url)
        self.locator = HomePageLocators

    def search_by_keyword(self,keyword):
        search = self.find_element(*self.locator.SEARCH)
        search.send_keys(keyword)
        search.send_keys(Keys.ENTER)


