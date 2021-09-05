from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_bucket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_link.click()

    def check_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text
        assert product_name == alert_product_name, "Наименование товара в аллерте не совпадает с добавленным в корзину"

    def check_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_product_price = self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT_ALERT).text
        assert product_price == alert_product_price, "Стоимость корзины не совпадает с ценой товара"
