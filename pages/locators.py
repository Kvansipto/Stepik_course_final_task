from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")
    BASKET_ITEMS = (By.CLASS_NAME, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_USER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_USER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_USER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_AMOUNT_ALERT = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
