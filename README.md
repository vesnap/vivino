# Vivino assignement


Test that validate search feature on [Vivno website](https://www.vivino.com/).

1. Start a browser and navigate to [Vivno website](https://www.vivino.com/)

2. Enter `<keyword>` into the search input and submit it by clicking on the search button

3. Parse the 1st page with search results: store info given on the 1st page of search results as structured data of any chosen by your type.

4. Make sure at least one attribute (title, country, etc) of each item (found wine) from parsed search results contains `<keyword>` Log in stdout which wine and attributes contain `<keyword>` and which do not.

5. Click on random wine's title

6. Collect info from the wine page

7. Check that each attribute value is equal to one of those stored in the structure created in step #3

8. Check whether at least one attribute contains `<keyword>` and log which one

## Tech stack
- [Python](https://www.python.org/downloads/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [Pytest](https://docs.pytest.org/en/7.1.x/)

## Instructions
- Install Python 3 and pip
- Clone the project and navigate to project directory
- Create virtal environment
```sh
    python3 -m venv /path/to/new/virtual/environment
```
- Start virtual environment
```sh
    source /path/to/new/virtual/environment/bin/activate
```
- Install requirements
```sh
    pip install -r requirements.txt
```
- Run tests
```sh
     pytest tests/e2e_test.py --verbose --capture=no --keyword <keyword>
```
## About solution
Page Object Model is used in order to reduce code duplication and improves test maintenance. Locators module for elemen selectors is used to separate page logic and page eleents, and again to improve code mainianance and reusability. Tests are configurable and we can chose browser, base_url and test input (keyword).
There is a sandbox file in which you can perform investigation prior to writing test.
