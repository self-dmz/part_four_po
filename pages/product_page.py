from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_workable_add_to_basket_button(self):
        title_before = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_ON_PAGE).text
        price_before = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ON_PAGE).text
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()
        lst = self.browser.find_elements(*ProductPageLocators.STRONG_LIST)
        title_after = lst[3].text
        price_after = lst[5].text
        assert title_before == title_after and price_before == price_after, 'WRONG book or price in the basket!'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def if_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
