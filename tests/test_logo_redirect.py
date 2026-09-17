import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import MAIN_PAGE_URL


class TestLogoRedirect:

    @allure.title("Переход на главную страницу по клику на логотип «Самокат»")
    def test_click_scooter_logo_from_order_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_top()

        order_page = OrderPage(driver)
        order_page.click_scooter_logo_on_order_page()

        assert driver.current_url == MAIN_PAGE_URL, \
            f"Ожидался {MAIN_PAGE_URL}, получили {driver.current_url}"

    @allure.title("Переход на Дзен по клику на логотип «Яндекс»")
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_dzen_tab_and_wait()

        assert "dzen.ru" in driver.current_url, \
            f"Ожидался переход на Дзен, получили {driver.current_url}"
