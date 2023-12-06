import pytest

from data.daten import generate_test_data
from pages.contact_page import ContactPage


class TestContactForm:
    def test_form_submission(self, setup, env):
        contact_page = ContactPage(setup, env)
        test_data = generate_test_data()
        print(test_data)
        contact_page.fill_form(test_data)
        contact_page.submit_form()
        assert contact_page.is_submit_successful(), "The button text did not change to submitted"

    @pytest.mark.parametrize("email, expected_validity", [
        ("", False),  # email為空
        ("no-at-sign", False),  # email没有包含@
        ("no-domain@", False),  # email没有@後面的部分
        ("valid@test.com", True),  # 有效的email
    ])
    def test_email_validity(self, setup, env, email, expected_validity):
        contact_page = ContactPage(setup, env)
        contact_page.fill_email(email)
        is_valid = contact_page.is_valid_of_email_field()
        assert is_valid == expected_validity, f"Email validity for '{email}' should be {expected_validity}"
