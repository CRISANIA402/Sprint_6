import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import user_data_set_1, user_data_set_2


class TestOrder:
    @pytest.mark.parametrize(
        "user_data",
        [user_data_set_1, user_data_set_2],
        ids=["Набор 1 — Иван", "Набор 2 — Маша"]
    )
    @pytest.mark.parametrize(
        "entry_point",
        ["top", "bottom"],
        ids=["Кнопка вверху", "Кнопка внизу"]
    )
    def test_order_scooter(self, driver, user_data, entry_point):
        main_page = MainPage(driver)

        if entry_point == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page = OrderPage(driver)

        order_page.fill_first_form(
            user_data["name"],
            user_data["surname"],
            user_data["address"],
            user_data["metro"],
            user_data["phone"],
        )

        order_page.fill_second_form(
            user_data["date"],
            user_data["rental_period"],
            user_data["color"],
            user_data["comment"],
        )

        order_page.confirm_order()

        assert order_page.is_order_success_displayed(), \
            "Сообщение об успешном заказе не появилось"
