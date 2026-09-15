from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    def fill_first_form(self, name, surname, address, metro, phone):
        self.find_element(OrderPageLocators.NAME_FIELD).send_keys(name)
        self.find_element(OrderPageLocators.SURNAME_FIELD).send_keys(surname)
        self.find_element(OrderPageLocators.ADDRESS_FIELD).send_keys(address)

        metro_field = self.find_element(OrderPageLocators.METRO_FIELD)
        metro_field.send_keys(metro)
        metro_field.send_keys(Keys.DOWN)
        metro_field.send_keys(Keys.ENTER)

        self.find_element(OrderPageLocators.PHONE_FIELD).send_keys(phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form(self, date, rental_period, color, comment):
        date_field = self.find_element(OrderPageLocators.DATE_FIELD)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        from selenium.webdriver.common.by import By
        rental_option = self.driver.find_element(
            By.XPATH, f"//div[contains(@class, 'option') and text()='{rental_period}']"
        )
        rental_option.click()

        if color == "black":
            self.click_element(OrderPageLocators.BLACK_CHECKBOX)
        elif color == "grey":
            self.click_element(OrderPageLocators.GREY_CHECKBOX)

        self.find_element(OrderPageLocators.COMMENT_FIELD).send_keys(comment)
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    def is_order_success_displayed(self):
        return self.wait_for_element_visible(OrderPageLocators.SUCCESS_MESSAGE).is_displayed()

    def get_success_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)

    def click_scooter_logo_on_order_page(self):
        self.click_element(OrderPageLocators.SCOOTER_LOGO_ON_ORDER_PAGE)

    def click_yandex_logo_on_order_page(self):
        self.click_element(OrderPageLocators.YANDEX_LOGO_ON_ORDER_PAGE)
