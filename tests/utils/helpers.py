import json
from selenium.webdriver.common.by import By
#util/helper module with different functions that are reused in the framework, it can be further refactored
#in the future in separate files related to different uses
def get_all_children(element):
    return element.find_elements(By.CSS_SELECTOR,"*")

def get_attribute(element, attr_name):
    return element.get_attribute(attr_name)

def load_setting():
    with open('tests/data/settings.json') as f:
        data = f.read()
    js = json.loads(data)
    return js
