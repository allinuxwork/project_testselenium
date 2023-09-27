import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="firefox",
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        "--language",
        action="store",
        default=None,
        help="Choose from langs: (en/ru/es/...)",
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": user_language}
        )
        print("\n\nStart Chrome for test...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = Options()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        print("Browser<browser_name> still is not implemented")
    yield browser
    print("\nQuit browser...")
    browser.quit()
