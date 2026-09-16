import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Нажать кнопку «Принять куки»")
    def click_cookie_button(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON, timeout=3)
        except Exception:
            pass

    @allure.step("Клик по кнопке заказа сверху")
    def click_order_button_top(self):
        self.click_cookie_button()
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Клик по кнопке заказа снизу")
    def click_order_button_bottom(self):
        self.click_cookie_button()
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Нажать кнопку заказа: {entry_point}")
    def click_order_button(self, entry_point: str):
        if entry_point == "top":
            self.click_order_button_top()
        else:
            self.click_order_button_bottom()

    @allure.step("Клик на вопрос FAQ по индексу: {index}")
    def click_faq_question(self, index: int):
        self.click_cookie_button()
        questions = self.find_elements(MainPageLocators.FAQ_QUESTIONS)
        questions[index].click()

    @allure.step("Проверить видимость ответа FAQ по индексу: {index}")
    def is_faq_answer_visible(self, index: int) -> bool:
        answers = self.find_elements(MainPageLocators.FAQ_ANSWERS)
        return answers[index].is_displayed()

    @allure.step("Получить текст ответа FAQ по индексу: {index}")
    def get_faq_answer_text(self, index: int) -> str:
        answers = self.find_elements(MainPageLocators.FAQ_ANSWERS)
        return answers[index].text

    @allure.step("Клик по логотипу «Самокат»")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу «Яндекс»")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)
