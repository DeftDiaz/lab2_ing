from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login_page import LoginPage


def test_ejecucion_pom():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://saucedemo.com")

        login = LoginPage(driver)
        login.ingresar_credenciales("locked_out_user", "secret_sauce")
        login.click_login()

        mensaje = login.obtener_error()
        print(f"Resultado de la prueba: {mensaje}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_ejecucion_pom()
