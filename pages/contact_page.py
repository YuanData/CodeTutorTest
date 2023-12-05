from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config_manager import ConfigManager
from locators.contact_loc import *


class ContactPage:
    def __init__(self, driver, env):
        config_manager = ConfigManager()
        self.domain = config_manager.get_domain(env)
        self.url_contact = f"{self.domain}#contact-section"

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url_contact)

    def fill_form(self, data: dict):
        name_field = self.wait.until(EC.element_to_be_clickable((By.NAME, NAME_FIELD)))
        name_field.send_keys(data["name"])
        self.driver.find_element_by_name(EMAIL_FIELD).send_keys(data["email"])
        if "phone" in data:
            self.driver.find_element_by_name(PHONE_FIELD).send_keys(data["phone"])
        if "notes" in data:
            self.driver.find_element_by_name(NOTES_FIELD).send_keys(data["notes"])

    def submit_form(self):
        self.driver.find_element_by_id(SUBMIT_BUTTON).click()

    def is_submit_successful(self):
        return self.wait.until(EC.text_to_be_present_in_element((By.ID, SUBMIT_BUTTON), "已提交！"))
