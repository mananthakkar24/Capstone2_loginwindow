from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome(r"C:\Users\Lenovo\Desktop\chromedriver.exe")
browser.get('http://127.0.0.1:5001/')
browser.find_element_by_link_text("Register").click()
#browser.find_element_by_id('name').send_keys("Steve")
browser.implicitly_wait(10) # seconds
myDynamicElement = browser.find_element_by_id("name")
myDynamicElement.send_keys('Alister')
myDynamicElement = browser.find_element_by_id("username")
myDynamicElement.send_keys('Alsiter99')
myDynamicElement = browser.find_element_by_id("email")
myDynamicElement.send_keys('alister.cool4545@gmail.com')
myDynamicElement = browser.find_element_by_id("password")
myDynamicElement.send_keys('Alsit@awsm99')
myDynamicElement = browser.find_element_by_id("confirmpassword")
myDynamicElement.send_keys('Alsit@awsm99')
myDynamicElement = browser.find_element_by_id("phone")
myDynamicElement.send_keys('9874563210')
myDynamicElement = browser.find_element_by_id("age")
myDynamicElement.send_keys('22')
myDynamicElement = browser.find_element_by_id("address")
myDynamicElement.send_keys('Niit University , Neemrana')
myDynamicElement = browser.find_element_by_id("city")
myDynamicElement.send_keys('Neemrana')
myDynamicElement = browser.find_element_by_id("state")
myDynamicElement.send_keys('Rajasthan')
myDynamicElement = browser.find_element_by_id("bd")
myDynamicElement.send_keys('98.4')
browser.find_element_by_css_selector("input[type='radio'][id = 'rn1'][value='1']").click()
browser.find_element_by_css_selector("input[type='radio'][id = 'ba1'][value='1']").click()
browser.find_element_by_css_selector("input[type='radio'][id = 'db3'][value='0']").click()
browser.find_element_by_css_selector("input[type='radio'][id = 'dc1'][value='1']").click()
browser.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[2]").click()
browser.find_element_by_link_text("Login").click()
browser.implicitly_wait(10)
browser.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]").send_keys("Alsiter99")
browser.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/input[1]"),.send_keys("Alsit@awsm99")









#en = ui.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.grid_size:nth-child(8)')))
#browser.find_element_by_id("email").send_keys("sd@gmail.com")
#print(browser.title)
#button = browser.find_element_by_id('searchField').send_keys("Movies")
#button.click()
#username = browser.find_element_by_id('user_full_name')
#username.send_keys('John Doe')
#browser.close()

