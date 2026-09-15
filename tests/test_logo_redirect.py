from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.ui import WebDriverWait
from urls import MAIN_PAGE_URL


class TestLogoRedirect:
    def test_click_scooter_logo_from_order_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_top()

        order_page = OrderPage(driver)
        order_page.click_scooter_logo_on_order_page()

        assert driver.current_url == MAIN_PAGE_URL, \
            f"Ожидался {MAIN_PAGE_URL}, получили {driver.current_url}"

    def test_click_yandex_logo(self, driver):
        """Клик по логотипу «Яндекс» открывает Дзен в новом окне."""
        main_page = MainPage(driver)
        main_page.click_yandex_logo()

        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(lambda d: "dzen.ru" in d.current_url)

        assert "dzen.ru" in driver.current_url, \
            f"Ожидался переход на Дзен, получили {driver.current_url}"
