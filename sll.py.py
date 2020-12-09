from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
import numpy as np 
print("Test case started")
length = 6
e_f = 8
e_b = 5
e_l = 3
ap = []
letters = string.ascii_lowercase
name = ''.join(random.choice(letters) for i in range(length))
username = ''.join(random.choice(letters) for i in range(length+2))
pas = "Mast@2020"
email = ''.join(random.choice(letters) for i in range(e_f)) 
email = email + '@'
email = email + ''.join(random.choice(letters) for i in range(e_b)) 
email = email  + '.'
email = email + ''.join(random.choice(letters) for i in range(e_l))
number = random.randint(1000000000,9999999999)
age = random.randint(10,99)
address = ''.join(random.choice(letters) for i in range(10)) +',' + ''.join(random.choice(letters) for i in range(10))  
browser = webdriver.Firefox()
city = ''.join(random.choice(letters) for i in range(8))
state = ''.join(random.choice(letters) for i in range(8))
temp = random.randint(80,103)

#browser = webdriver.Firefox(executionpath ="/Users/mananthakkar/Desktop/Capstone2_loginwindow/geckodriver")
browser.get('http://127.0.0.1:5001/')
browser.find_element_by_link_text("Register").click()
#browser.find_element_by_id('name').send_keys("Steve")
browser.implicitly_wait(10) # seconds
myDynamicElement = browser.find_element_by_id("name")
myDynamicElement.send_keys(name)
myDynamicElement = browser.find_element_by_id("username")
myDynamicElement.send_keys(username)
myDynamicElement = browser.find_element_by_id("email")
myDynamicElement.send_keys(email)
myDynamicElement = browser.find_element_by_id("password")
myDynamicElement.send_keys(pas)
myDynamicElement = browser.find_element_by_id("confirmpassword")
myDynamicElement.send_keys(pas)
myDynamicElement = browser.find_element_by_id("phone")
myDynamicElement.send_keys(str(number))
myDynamicElement = browser.find_element_by_id("age")
myDynamicElement.send_keys(str(age))
myDynamicElement = browser.find_element_by_id("address")
myDynamicElement.send_keys(address)
myDynamicElement = browser.find_element_by_id("city")
myDynamicElement.send_keys(city)
myDynamicElement = browser.find_element_by_id("state")
myDynamicElement.send_keys(state)
myDynamicElement = browser.find_element_by_id("bd")
myDynamicElement.send_keys(str(temp))
browser.find_element_by_css_selector("input[type='radio'][id = 'rn1'][value='1']").click()
browser.find_element_by_css_selector("input[type='radio'][id = 'ba1'][value='1']").click()
browser.find_element_by_css_selector("input[type='radio'][id = 'db3'][value='0']").click()
browser.find_element_by_css_selector("input[type='radio'][id = 'dc1'][value='1']").click()
browser.implicitly_wait(10)
browser.find_element_by_css_selector("body.modal-open:nth-child(2) div.site-wrapper:nth-child(1) div.site-wrapper-inner div.cover-container div.modal.fade.show:nth-child(2) div.modal-dialog div.modal-content div.modal-footer > button.btn.btn-primary:nth-child(2)").click()
#browser.implicitly_wait(10)
browser.find_element_by_link_text("Login").click()
browser.implicitly_wait(10)
browser.find_element_by_xpath("//form[@action='/login/']//div[@class='form-group']//input[@id='email']").send_keys(username)
browser.find_element_by_xpath("//form[@action='/login/']//div[@class='form-group']//input[@id='password']").send_keys(pas)
browser.find_element_by_xpath("//button[contains(text(),'Login')]").click()
browser.implicitly_wait(60)
browser.find_element_by_xpath("//a[@class='mt-2 btn btn-lg btn-default']").click() 
browser.close()
print ("Test Case Passed")

#en = ui.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.grid_size:nth-child(8)')))
#browser.find_element_by_id("email").send_keys("sd@gmail.com")
#print(browser.title)
#button = browser.find_element_by_id('searchField').send_keys("Movies")
#button.click()
#username = browser.find_element_by_id('user_full_name')
#username.send_keys('John Doe')
#browser.close()

