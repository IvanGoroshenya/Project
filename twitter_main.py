from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Настройки Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Путь к драйверу Chrome
service = Service('E:\Test_Task\chromedriver\chromedriver.exe')

# Инициализация драйвера
driver = webdriver.Chrome(service=service, options=chrome_options)


# # Открытие страницы входа в Google
# driver.get("http://twitter.com/login")
#
#


name = 'Ivan'
password = 'IvanG2000'
email = 'ivan.goroshchenya@gmail.com'




def login_to_twitter(email, password):
    driver.get("https://twitter.com/login")

    wait = WebDriverWait(driver, 10)

    # Ввод email
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input')))
    email_input.send_keys(email)

    # Ввод пароля
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "//input[@name='session[username_or_email]']")))
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    time.sleep(5)  # Дайте время для завершения входа


    # Закрытие браузера
    driver.quit()

# Пример использования функции

login_to_twitter(email, password)