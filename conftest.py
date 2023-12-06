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
def domain_url():
    """
    Domain URL.

    :return: str
    """
    env = "Local"
    return {
        "Local": "http://localhost:1313/",
        "PROD": "https://yuandata.github.io/CodeTutor/",
    }.get(env)
