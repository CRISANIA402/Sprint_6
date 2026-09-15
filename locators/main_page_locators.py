from selenium.webdriver.common.by import By


class MainPageLocators:
    # Логотип «Самокат»
    SCOOTER_LOGO = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]

    # Логотип «Яндекс»
    YANDEX_LOGO = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]

    # Кнопка «Заказать» вверху (в шапке)
    ORDER_BUTTON_TOP = [By.CLASS_NAME, "Button_Button__ra12g"]

    # Кнопка «Заказать» внизу страницы
    ORDER_BUTTON_BOTTOM = [By.XPATH, "//button[normalize-space()='Заказать']"]
    
    # Кнопка согласия с куками
    COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]

    # Вопросы в разделе «Вопросы о важном»
    FAQ_QUESTIONS = [By.CLASS_NAME, "accordion__heading"]

    # Ответы
    FAQ_ANSWERS = [By.CLASS_NAME, "accordion__panel"]

