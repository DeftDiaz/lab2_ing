from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)


def ejecutar_pruebas():
    try:
        # Caso 1: Login exitoso
        print("Ejecutando Caso 1: Login...")
        driver.get("https://saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert "inventory.html" in driver.current_url
        print("Caso 1 completado con exito.")

        # Caso 2: Agregar al carrito
        print("Ejecutando Caso 2: Agregar producto...")
        boton_agregar = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        )
        boton_agregar.click()

        badge_carrito = driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge"
        ).text
        assert badge_carrito == "1"
        print("Caso 2 completado con exito.")

        # Caso 3: Login fallido (usuario bloqueado)
        print("Ejecutando Caso 3: Login fallido...")
        driver.delete_all_cookies()
        driver.get("https://saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        error_msg = driver.find_element(
            By.CSS_SELECTOR, "h3[data-test='error']"
        ).text
        assert "locked out" in error_msg
        print("Caso 3 completado con exito.")

        time.sleep(1)

    except Exception as e:
        print(f"Error durante la ejecucion: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    ejecutar_pruebas()
