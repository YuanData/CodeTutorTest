from data.daten import generate_test_data
from pages.contact_page import ContactPage


class TestContactForm:
    def test_form_submission(self, setup, env):
        contact_page = ContactPage(setup, env)
        test_data = generate_test_data()

        contact_page.fill_form(test_data)
        contact_page.submit_form()

        assert contact_page.is_submit_successful(), "The button text did not change to submitted"
