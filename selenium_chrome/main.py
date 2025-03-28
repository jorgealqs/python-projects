from selenium import webdriver  # type: ignore
from selenium.webdriver.chrome.service import Service  # type: ignore
from selenium.webdriver.chrome.options import Options  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support import (  # type: ignore
    expected_conditions as EC
)
from selenium.common.exceptions import (  # type: ignore
    TimeoutException,
    NoSuchElementException
)
from fake_useragent import UserAgent  # type: ignore
import random
import time


def create_driver():
    ua = UserAgent()
    options = Options()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"user-agent={ua.random}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--disable-gpu")
    options.add_argument("--lang=en-US,en;q=0.9")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    service = Service("./chrome_driver/mac_arm64/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    return driver


def random_sleep():
    """Añade delays aleatorios para simular comportamiento humano"""
    time.sleep(random.uniform(3, 7))


def get_product_info(url):
    driver = create_driver()
    try:
        driver.get(url)
        random_sleep()

        # Simular scroll para cargar la página correctamente
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight / 4);")
        time.sleep(2)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight / 2);")
        time.sleep(2)

        wait = WebDriverWait(driver, 10)  # Esperar hasta 10 segundos

        product_info = {}

        # Título del producto
        try:
            title_element = wait.until(
                EC.presence_of_element_located((By.ID, "productTitle")))
            product_info["title"] = title_element.text.strip()
        except TimeoutException:
            product_info["title"] = "No encontrado"

        # Precio del producto (buscando en diferentes selectores)
        try:
            price_element = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "span.a-price > span.a-offscreen")
            ))
            product_info["price"] = price_element.text.strip()
        except TimeoutException:
            try:
                price_element = driver.find_element(
                    By.CSS_SELECTOR, "span#price_inside_buybox")
                product_info["price"] = price_element.text.strip()
            except NoSuchElementException:
                product_info["price"] = "No disponible"

        # Disponibilidad
        try:
            availability_element = wait.until(
                EC.presence_of_element_located((By.ID, "availability")))
            product_info["availability"] = availability_element.text.strip()
        except TimeoutException:
            product_info["availability"] = "No especificado"

        # Reseñas
        try:
            reviews_element = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "span#acrCustomerReviewText")))
            product_info["reviews"] = reviews_element.text.strip()
        except TimeoutException:
            product_info["reviews"] = "No disponible"

        return product_info

    except Exception as e:
        print(f"❌ Error: {e}")
        return None
    finally:
        driver.quit()


if __name__ == "__main__":
    product_url = "https://www.amazon.com/dp/B09JKWQDB2"
    info = get_product_info(product_url)

    if info:
        print("\n🔹 Información del producto 🔹")
        for key, value in info.items():
            print(f"{key.capitalize()}: {value}")
