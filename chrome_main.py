from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

# Настройки Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Путь к драйверу Chrome
service = Service('E:\Test_Task\chromedriver\chromedriver.exe')

# Инициализация драйвера
driver = webdriver.Chrome(service=service, options=chrome_options)

# Открытие страницы входа в Google
driver.get("https://accounts.google.com/signin")

# Вход в аккаунт
email = "fl561416@gmail.com"
password = "Passwordfl5614"
new_password = "Passwordfl561416"
first_name = "firstname5550"
last_name = "lastname5550"
birth_date = "14/09/1990"
recovery_email = "recovery_fl561416@gmail.com"



def func_for_email():
    # Открытие страницы входа в Google
    driver.get("https://accounts.google.com/signin")

    wait = WebDriverWait(driver, 10)

    # Ввод email
    email_input = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
    email_input.send_keys(email)
    email_input.send_keys(Keys.ENTER)
    time.sleep(2)

    # Ввод пароля
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(2)

    driver.get("https://myaccount.google.com/profile/name/edit?continue=https://myaccount.google.com/profile/name?continue%3Dhttps://myaccount.google.com/personal-info&pli=1&rapt=AEjHL4M8hWcPVftqWTzDfTHSUMb7a15VRbO_-4BEKcLa_uqzdWNmRGkI-nM5JZGFmIOUZMx6tAVqUnxEZ9yXKRJB2p0THE_rvcsWBOfl--8fxJ0D4xg4IGE")
    time.sleep(5)



    # Изменим имя
    first_name_input = driver.find_element(By.ID, 'i7')
    first_name_input.clear()
    first_name_input.send_keys(first_name)
    time.sleep(5)

    # Изменим Фамилию
    last_name_input = driver.find_element(By.ID, 'i12')
    last_name_input.clear()
    last_name_input.send_keys(last_name)
    time.sleep(5)




    save_button = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/div[3]/div[2]/div/div/button')
    save_button.click()
    time.sleep(5)

    # Получить дату рождения
    driver.get('https://myaccount.google.com/personal-info?utm_source=sign_in_no_continue')
    # birthday = driver.find_element('a.RlFDUe.I6g62c.N5YmOc.kJXJmd')
    birthday = driver.find_element(By.XPATH,'//a[@href="birthday"]').get_attribute('aria-label')



    pickle.dump(driver.get_cookies(), open(f'{first_name}_cookies, f{last_name}_cookies', 'wb'))

    my_file = open("file.txt", "w+")
    my_file.write(f"Name - {first_name}, Lats Name - {last_name}, Birthday - {birthday}")
    my_file.close()





def func_for_password():
    # Открытие страницы входа в Google
    driver.get("https://accounts.google.com/signin")

    wait = WebDriverWait(driver, 10)

    # Ввод email
    email_input = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
    email_input.send_keys(email)
    email_input.send_keys(Keys.ENTER)
    time.sleep(2)

    # Ввод пароля
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(2)
    #
    # Изменение пароля
    driver.get("https://myaccount.google.com/security")
    password_edit_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'signinoptions/password')]")))
    password_edit_button.click()
    time.sleep(5)

    current_password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    current_password_input.send_keys(new_password)
    current_password_input.send_keys(Keys.ENTER)
    time.sleep(1)

    confirm_password_input = wait.until(EC.presence_of_element_located((By.NAME, "confirmation_password")))
    confirm_password_input.send_keys(new_password)

    change_password_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//html/body/c-wiz/div/div[2]/div[2]/c-wiz/div/div[4]/form/div/div[2]/div/div/button")))
    change_password_button.click()
    # //button[@type=‘submit’]
    time.sleep(5)



func_for_email()


driver.quit()