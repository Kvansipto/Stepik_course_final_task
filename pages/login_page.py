from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.endswith("login/"), "Login page not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_USER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_USER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_USER_CONFIRM_PASSWORD).send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        submit_button.click()
