from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

try:
    # Caso 1: Login seguro
    driver.get("https://saucedemo.com")

    user_input = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    user_input.send_keys("standard_user")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Caso 2: Agregar al carrito con verificacion de clic
    btn_add = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    btn_add.click()

    badge = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )
    print(f"Prueba exitosa: Carrito tiene {badge.text} producto(s).")

    # Caso 3: Validacion de error de bloqueo
    driver.get("https://saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error_container = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h3[data-test='error']")
        )
    )
    print(f"Validacion de error correcta: {error_container.text}")

finally:
    driver.quit()
