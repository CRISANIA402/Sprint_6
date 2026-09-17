import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, surname, address, metro, phone):
        name_field = self.find_element(OrderPageLocators.NAME_FIELD)
        name_field.clear()
        name_field.send_keys(name)

        surname_field = self.find_element(OrderPageLocators.SURNAME_FIELD)
        surname_field.clear()
        surname_field.send_keys(surname)

        address_field = self.find_element(OrderPageLocators.ADDRESS_FIELD)
        address_field.clear()
        address_field.send_keys(address)

        metro_field = self.find_element(OrderPageLocators.METRO_FIELD)
        metro_field.clear()
        metro_field.send_keys(metro)

        self.wait_for_element_visible(OrderPageLocators.METRO_FIRST_OPTION, timeout=5)
        self.click_element(OrderPageLocators.METRO_FIRST_OPTION)

        phone_field = self.find_element(OrderPageLocators.PHONE_FIELD)
        phone_field.clear()
        phone_field.send_keys(phone)

        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму")
    def fill_second_form(self, date, rental_period, color, comment):
        date_field = self.find_element(OrderPageLocators.DATE_FIELD)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)

        locator_tpl = OrderPageLocators.RENTAL_PERIOD_OPTION[1]
        locator = (By.XPATH, locator_tpl.format(period=rental_period))
        rental_option = self.find_element(locator)
        rental_option.click()

        if color == "black":
            self.click_element(OrderPageLocators.BLACK_CHECKBOX)
        elif color == "grey":
            self.click_element(OrderPageLocators.GREY_CHECKBOX)

        self.find_element(OrderPageLocators.COMMENT_FIELD).send_keys(comment)
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждает заказ в модальном окне")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Проверяет, что появилось сообщение об успешном заказе")
    def is_order_success_displayed(self):
        return self.wait_for_element_visible(OrderPageLocators.SUCCESS_MESSAGE).is_displayed()

    @allure.step("Возвращает текст сообщения об успешном заказе")
    def get_success_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)

    @allure.step("Кликает логотип «Самокат» на странице заказа")
    def click_scooter_logo_on_order_page(self):
        self.click_element(OrderPageLocators.SCOOTER_LOGO_ON_ORDER_PAGE)

    @allure.step("Кликает логотип «Яндекс» на странице заказа")
    def click_yandex_logo_on_order_page(self):
        self.click_element(OrderPageLocators.YANDEX_LOGO_ON_ORDER_PAGE)
