from login_page import LoginPage


def test_ejecucion_pom(driver):
    driver.get("https://saucedemo.com")

    login = LoginPage(driver)
    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()

    mensaje = login.obtener_error()
    print(f"Resultado de la prueba: {mensaje}")
