import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_login_fallido(driver):
    driver.get("https://saucedemo.com")
    login = LoginPage(driver)

    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()

    assert "locked out" in login.obtener_error()


def test_login_exitoso(driver):
    driver.get("https://saucedemo.com")
    login = LoginPage(driver)

    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()

    assert "inventory.html" in driver.current_url
