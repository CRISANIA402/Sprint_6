from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_cookie_button(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON, timeout=3)
        except Exception:
            pass  

    def click_order_button_top(self):
        self.click_cookie_button()
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click_cookie_button()
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_faq_question(self, index):
        self.click_cookie_button()
        questions = self.find_elements(MainPageLocators.FAQ_QUESTIONS)
        questions[index].click()

    def is_faq_answer_visible(self, index):
        answers = self.find_elements(MainPageLocators.FAQ_ANSWERS)
        return answers[index].is_displayed()

    def get_faq_answer_text(self, index):
        answers = self.find_elements(MainPageLocators.FAQ_ANSWERS)
        return answers[index].text

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)
