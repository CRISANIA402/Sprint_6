import allure
import pytest
from pages.main_page import MainPage


class TestFAQ:

    @allure.title("Проверка раскрытия ответа FAQ #{index + 1}")
    @pytest.mark.parametrize("index", list(range(8)))
    def test_faq_dropdown(self, driver, index):
        main_page = MainPage(driver)
        main_page.click_faq_question(index)
        assert main_page.is_faq_answer_visible(index), \
            f"Ответ на вопрос #{index + 1} не раскрылся"
        text = main_page.get_faq_answer_text(index)
        assert len(text) > 0, f"Текст ответа #{index + 1} пустой"
