# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# time.sleep(5)

# driver.get("https://suninjuly.github.io/text_input_task.html")
# time.sleep(5)

# textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# textarea.send_keys("get()")
# time.sleep(5)

# submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# submit_button.click()
# time.sleep(5)

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element(By.ID, "submit_button")

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()