from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chrome_browser = webdriver.Chrome('chromedriver.exe')
s = Service('D:\Automation-Testing\chromedriver.exe')
driver = webdriver.Chrome(service=s)
chrome_browser = driver
# print(chrome_browser)

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# print('Selenium Easy Demo' in chrome_browser.title)

show_message_button = chrome_browser.find_element(by=By.CLASS_NAME, value='btn-default')
# print(show_message_button.get_attribute('innerHTML'))

# assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(by=By.ID, value='user-message')
# user_button2 = chrome_browser.find_element(by=By.CSS_SELECTOR, value='#get-input > .btn')
# print(user_button2)
user_message.clear()
user_message.send_keys('Mi name is Salvador')

show_message_button.click()

output_message = chrome_browser.find_element(by=By.ID, value='display')

# assert 'Mi name is Salvador' in output_message.text

# chrome_browser.close()
# chrome_browser.quit()
