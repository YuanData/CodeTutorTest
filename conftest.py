import pytest
from selenium.webdriver import Chrome, ChromeOptions


@pytest.fixture(autouse=True)
def setup():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = Chrome(options=chrome_options)

    yield driver
    driver.close()


@pytest.fixture
def env():
    """
    Provides the environment for the test.
    Available environments are:
    - PROD
    - QA

    :return: str - The environment for the test. Default is "UAT".
    """
    return "PROD"
