from selenium.webdriver.common.by import By

class OrderPageLocators:
    # --- Форма «Для кого самокат» ---
    NAME_FIELD = [By.XPATH, "//input[@placeholder='* Имя']"]
    SURNAME_FIELD = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS_FIELD = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO_FIELD = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    METRO_FIRST_OPTION = [By.CLASS_NAME, "select-search__input"]
    PHONE_FIELD = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, "//button[text()='Далее']"]

    # --- Форма «Про аренду» ---
    DATE_FIELD = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    RENTAL_PERIOD_FIELD = [By.CLASS_NAME, "Dropdown-control"]
    BLACK_CHECKBOX = [By.XPATH, "//label[text()='чёрный жемчуг']//input"]
    GREY_CHECKBOX = [By.XPATH, "//label[text()='серая безысходность']//input"]
    COMMENT_FIELD = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]//button[text()='Заказать']"]
    BACK_BUTTON = [By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]//button[text()='Назад']"]
    CONFIRM_YES_BUTTON = [By.XPATH, "//button[text()='Да']"]
    SUCCESS_MESSAGE = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]

    # Логотипы на странице заказа
    SCOOTER_LOGO_ON_ORDER_PAGE = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    YANDEX_LOGO_ON_ORDER_PAGE = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]

    # Другие локаторы
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'option') and text()='{period}']")