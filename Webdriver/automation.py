from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(executable_path='./chromedriver')
chrome_browser = webdriver.Chrome(service=service)


# button = chrome_browser.find_element(By.CLASS_NAME, 'radius')

successful_username = 'tomsmith'
successful_password = 'SuperSecretPassword!'
def login_succesful(login, password):
    chrome_browser.get('http://the-internet.herokuapp.com/login')
    try:
        assert 'The Internet' in chrome_browser.title
        assert 'Login' in chrome_browser.page_source
        assert 'username' in chrome_browser.page_source
        assert 'password' in chrome_browser.page_source
        username = chrome_browser.find_element(By.ID, 'username')
        username.clear()
        username.send_keys(login)
        user_password = chrome_browser.find_element(By.XPATH, '//*[@id="password"]')
        user_password.clear()
        user_password.send_keys(password)
        user_password = chrome_browser.find_element(By.XPATH, '//*[@id="password"]')
        user_password.clear()
        user_password.send_keys(password)
        button2 = chrome_browser.find_element(By.XPATH, '//*[@id="login"]/button')
        button2.click()
    except AssertionError as err:
        print(err)
login_succesful(successful_username, successful_password)
# input()