
from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class ProductPageLocators(object):
    IMAGE = (By.TAG_NAME, "img")
    HEADING = (By.TAG_NAME, 'h1')
    PRODUCT_RATING = (By.CSS_SELECTOR, 'a[href="#all_reviews"]')

class SearchResultsLocators(object):
    PRODUCTS = (By.CLASS_NAME, 'card.card-lg')
    PRODUCT_IMAGE = (By.CLASS_NAME, "wine-card__image")
    PRODUCT_TEXT = (By.CLASS_NAME, "link-color-alt-grey")
    PRODUCT_REGION = (By.CLASS_NAME, "text-block.wine-card__region")
    PRODUCT_AVARAGE = (By.CLASS_NAME, "average__container")

class HomePageLocators(object):
    SEARCH=(By.CSS_SELECTOR, 'input[aria-label="Search any wine"]')
