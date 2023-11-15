#Chapter 1.6 task 10
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     input1 = browser.find_element(By.CSS_SELECTOR, "label[title~='First name*'] + input[required]")
#     input1.send_keys("Robert")

#     input2 = browser.find_element(By.CSS_SELECTOR, ".second_class input[required]") #.second_class input[required]
#     input2.send_keys("Pollson")

#     input3 = browser.find_element(By.CSS_SELECTOR, ".third_class input[required]")
#     input3.send_keys("shrek@test.com")

#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()

#     time.sleep(2)

#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     welcome_text = welcome_text_elt.text

#     assert "Congratulations! You have successfully registered!" == welcome_text


# except Exception as error:
#      print( f"expected 200, but got {error}")

# finally:
#     time.sleep(10)
#     print("Test passed successfully")

#Chapter 2.1 Task 5
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math


# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))


# try:
#     link = "https://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value" )
#     x = x_element.text
#     y = calc(x)

#     answer = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer.send_keys(y)

#     robo = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
#     robo.click()

#     robo_rule = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
#     robo_rule.click()

#     button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
#     button.click()

# except Exception as error:
#      print( f"The Following error has occured: {error}")

# finally:
#     time.sleep(10)


#Chapter 2.1 Task 7
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math

# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     link = "http://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     chest = browser.find_element(By.CSS_SELECTOR, "#treasure")
#     ch_val = chest.get_attribute("valuex")
#     con_val = ch_val
#     fin_val = calc(con_val)

#     answer = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer.send_keys(fin_val)

#     im_rob = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
#     im_rob.click()

#     robo_rule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
#     robo_rule.click()

#     sub = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
#     sub.click()

# except Exception as error:
#     print(f"Something weird happened: {error}")

# finally:
#     time.sleep(10)
#     browser.quit()


#Chapter 2.2 Task 3:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time


# try:
#     link = "https://suninjuly.github.io/selects2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     num_1 = browser.find_element(By.CSS_SELECTOR, "#num1")
#     text_1 = num_1.text
#     print(text_1)
    
#     num_2 = browser.find_element(By.CSS_SELECTOR, "#num2")
#     text_2 = num_2.text
#     print(text_2)

#     oper = browser.find_element(By.CSS_SELECTOR, "div > form > h2 > span:nth-child(3)")
#     text_op = oper.text
#     print(text_op)

#     def calc(text_1, text_op, text_2):
#         if text_op == "+":
#             res = int(text_1) + int(text_2)
#             return res
        
#         elif text_op == "-":
#             res = int(text_1) - int(text_2)
#             return res

#         elif text_op == "*":
#             res = int(text_1) * int(text_2)
#             return res
 
#         elif text_op == "/":
#             res = int(text_1) / int(text_2)
#             return res

#         elif text_op == "//":
#             res = int(text_1) // int(text_2)
#             return res

#         else:
#             res = int(text_1) + int(text_2)
#             return res

#     result = calc(text_1, text_op, text_2)

#     select = Select(browser.find_element(By.CSS_SELECTOR, "select"))
#     select.select_by_value(str(result))

#     button = browser.find_element(By.CSS_SELECTOR, "button[type='submit'][class='btn btn-default']")
#     button.click()

# except Exception as error:
#     print(f"Something happened: {error}")

# finally:
#     time.sleep(10)
#     browser.quit


#Chapter 2.2 Task 6:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math


# try:
#     link = " https://SunInJuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     x = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x_text = x.text

#     def calc(x):
#         return str(math.log(abs(12*math.sin(int(x_text)))))

#     res = calc(x_text)

#     answer = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer.send_keys(res)

#     checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
#     browser.execute_script("return arguments[0].scrollIntoView(true); behavior: 'smooth'", checkbox)
#     checkbox.click()
    
#     radiobutt = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
#     radiobutt.click()

#     butt = browser.find_element(By.CSS_SELECTOR, "button[type='submit'][class='btn btn-primary']")
#     butt.click()

# except Exception as error:
#     print(f"Check your code for {error}")

# finally:
#     time.sleep(10)
#     browser.quit()

#chapter 2.2 Task 8
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import os
# import time

# try:
#     link = "http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname'][class='form-control'][required]")
#     first_name.send_keys("Bob")

#     last_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname'][class='form-control'][required]")
#     last_name.send_keys("Greyson")

#     email = browser.find_element(By.CSS_SELECTOR, "input[name='email'][class='form-control']")
#     email.send_keys("Shrek@test.com")

#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file = os.path.join(current_dir, "Death_Star_plans.txt")

#     file_button = browser.find_element(By.CSS_SELECTOR, "input[type='file'][id='file'][name='file']")
#     file_button.send_keys(file)

#     submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit'][class='btn btn-primary']")
#     submit.click()

# except Exception as error:
#     print(f'Check this {error}')

# finally:
#     time.sleep(10)
#     browser.quit()


#Chapter 2.3 Task 3
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math

# try:
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     butt = browser.find_element(By.CSS_SELECTOR, "button[type='submit'][class='btn btn-primary']")
#     butt.click()

#     diss = browser.switch_to.alert
#     diss.dismiss()

#     butt = browser.find_element(By.CSS_SELECTOR, "button[type='submit'][class='btn btn-primary']")
#     butt.click()

#     accept = browser.switch_to.alert
#     accept.accept()

#     x = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x_text = x.text

#     def calc(x):
#         return str(math.log(abs(12*math.sin(int(x_text)))))
    
#     result = calc(x_text)

#     answer = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
#     answer.send_keys(result)

#     sub = browser.find_element(By.CSS_SELECTOR, "button[type='submit'][class='btn btn-primary']")
#     sub.click()

# except Exception as error:
#     print(f"Check your code dude, {error}")

# finally:
#     time.sleep(10)
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math

# try: 
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     magic_butt = browser.find_element(By.CSS_SELECTOR, "div[class='container'] > button[type='submit'][class='trollface btn btn-primary']")
#     magic_butt.click()

#     browser.switch_to.window(browser.window_handles[1])

#     x = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x_text = x.text

#     def calc(x):
#         return str(math.log(abs(12*math.sin(int(x_text)))))

#     result = calc(x_text)

#     answer = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer.send_keys(result)

#     send_answer = browser.find_element(By.CSS_SELECTOR, "button[type='submit'][class='btn btn-primary']")
#     send_answer.click()

#     password = (browser.switch_to.alert.text).split(" ")[-1]
#     print(f"here is your password, {password}")

# except Exception as error:
#     print(f"something went wrong, check this {error}")

# finally:
#     time.sleep(10)
#     browser.quit()


#Chapter 2.4 Task 6
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# try:
#     link = "http://suninjuly.github.io/cats.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     # browser.implicitly_wait(5)
#     button = browser.find_element(By.CSS_SELECTOR, "button")

# except Exception as error:
#     print(f"The following error has been spotted:{error}")

# finally:
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)

# browser.get("http://suninjuly.github.io/wait2.html")

# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")

# assert "successful" in message.text


#Chapter 2.4 Task 8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.CSS_SELECTOR, "button[id='book']")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
    button.click()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true); behavior: 'smooth'", x)
    x_text = x.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x_text)))))

    res = calc(x_text)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(res)

    submit = browser.find_element(By.CSS_SELECTOR, "#solve").click()

    password = (browser.switch_to.alert.text).split(" ")[-1]
    print(f"here is your password, {password}")

except Exception as error:
    print(f"The following error has occured: {error}")

finally:
    time.sleep(19)
    browser.quit()


    