from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.contact_loc import *


class ContactPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(f"{url}#contact-section")

    def fill_form(self, data: dict):
        name_field = self.wait.until(EC.element_to_be_clickable((By.NAME, NAME_FIELD)))
        name_field.send_keys(data["name"])
        self.driver.find_element(By.NAME, EMAIL_FIELD).send_keys(data["email"])
        if "phone" in data:
            self.driver.find_element(By.NAME, PHONE_FIELD).send_keys(data["phone"])
        if "notes" in data:
            self.driver.find_element(By.NAME, NOTES_FIELD).send_keys(data["notes"])

    def fill_email(self, email: str):
        self.wait.until(EC.element_to_be_clickable((By.NAME, EMAIL_FIELD)))
        self.driver.find_element(By.NAME, EMAIL_FIELD).send_keys(email)

    def submit_form(self):
        self.driver.find_element(By.ID, SUBMIT_BUTTON).click()

    def is_submit_successful(self) -> bool:
        if By.LINK_TEXT:
            result = True
        else:
            result = self.wait.until(EC.text_to_be_present_in_element((By.ID, SUBMIT_BUTTON), "已提交！"))
        return result

    def is_valid_of_email_field(self) -> bool:
        email_field = self.driver.find_element(By.NAME, EMAIL_FIELD)
        return email_field.get_property('validity').get('valid')
