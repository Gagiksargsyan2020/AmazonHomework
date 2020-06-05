#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(executable_path)
driver.get('https://www.amazon.in')

#Get element by id
element = driver.find_element_by_id('nav-link-yourAccount')
element.click()

#Send values to element
from selenium.webdriver.common.Keys import Keys
email = driver.find_element_by_id('ap_email')
email.send_keys('qwe@gmail.com')

#Get element by name
email2:WebElement = driver.find_element_by_name('email')
email2.clear()
email2.send_keys('qwe')

email2.get_attribute('id')
u'ap_email'

#Get element by XPATH
email3 = driver.find_element_by_xpath("//*[@id= 'ap_email']")
email3.clear()
email3.send_keys('Hello')

#Get element by class

c = driver.find_element_by_class-name('a-link-normal')
c.get_attribute('href')

#Form select element


from selenium.webdriver_support.ui import Select
driver.get('https://www.amazon.com')
category = Select(driver.find_element_by_id('searchDropdownBox'))
category.select_by_index(6)












