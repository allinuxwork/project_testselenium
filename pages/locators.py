from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#register_form input[type=email]")
    PASSWORD_FIELD = (
        By.CSS_SELECTOR,
        "#register_form input[name=registration-password1]",
    )
    PASSWORD_CONFIRM = (
        By.CSS_SELECTOR,
        "#register_form input[name=registration-password2]",
    )
    REG_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")
