from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Page class is base class that has most common methods that are used for page manipulation
class Page:

    def __init__(self,driver,base_url):
        self.driver = driver
        self.timeout = 30
        self.base_url=base_url

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def open(self):
        self.driver.get(self.base_url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_text(self,element):
        return element.text

    def get_attr(self,element,attribute):
        return element.get_attribute(attribute)

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()
