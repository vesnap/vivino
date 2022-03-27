from selenium import webdriver
import random
from tests.pages.homepage import Homepage
from tests.pages.product import Product
from tests.pages.search_results import SearchResults
import pytest
from tests.utils import helpers
#e2e test , we use fixture to setup the test, browser or driver is shared in the test, and all Page classes have driver
#attribute

@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = webdriver.Chrome()
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test(browser, keyword):
    base_url = helpers.load_setting()['url']
    homepage = Homepage(browser,base_url)
    homepage.open()
    homepage.search_by_keyword(keyword)
    search_page=SearchResults(browser,base_url)
    product_list=search_page.get_products()
    products = search_page.parse_products(product_list)
    i = random.choice(range(len(product_list)))
    search_page.click_on_product(product_list[i])
    product_page=Product(browser, base_url)
    product = {"image_url": product_page.get_image_href(), "product_winery": product_page.get_winery(),
               "product_name": product_page.get_vine_name(), "product_rating": product_page.get_review()}
    assert products[i]['avarage'] == product["product_rating"]
    assert product["product_winery"] in products[i]['winery']
    assert product["product_name"] in products[i]['winery']
    assert keyword in products[i]['winery']
    assert keyword in product['product_name']






