import time

import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo_num',
                         ["0", "1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_bucket()
    page.solve_quiz_and_get_code()
    page.check_product_name()
    page.check_product_price()
