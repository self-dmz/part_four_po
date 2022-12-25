from .base_page import BasePage
from .locators import LoginPageLocators
from faker import Faker
fake_en = Faker('En')
Faker.seed()


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.find_element(*LoginPageLocators.LOGIN_FORM).get_attribute('action')
        print('url:', url)
        assert 'login' in url, 'URL in Login Form is absent or wrong'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login Form is absent or something else is wrong'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Reg Form is absent or something else is wrong'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PSW_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PSW_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_UP_BUTTON).click()









