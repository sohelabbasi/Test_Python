from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
PATH = "C:\\Users\\13479\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#driver.get("https://mingle35-cloudidentities.inforgov.com/idp/SSO.saml2")
driver.get("https://mingle35-portal.inforgov.com/PPLEUC_TST")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.current_url)
print(driver.title)

CloudIdentities = driver.find_element_by_xpath("//*[@class='ping-button normal']")
if CloudIdentities.is_displayed():
    CloudIdentities.click()

driver.implicitly_wait(3)

driver.implicitly_wait(5)
usernamefeild = driver.find_element_by_xpath("//*[@id='username']")
if usernamefeild.is_displayed():
    usernamefeild.click()
    usernamefeild.clear()
    usernamefeild.send_keys("snhaq@pplweb.com")
else:
    print("option not found")

driver.implicitly_wait(2)
passwordfeild = driver.find_element_by_xpath("//*[@id='password']")
if passwordfeild.is_displayed():
    passwordfeild.click()
    passwordfeild.clear()
    passwordfeild.send_keys("12Qahdeys@02")
else:
    print("option not found")

driver.implicitly_wait(2)

signinButton = driver.find_element_by_xpath("//*[@class='ping-button normal allow']")
if signinButton.is_displayed():
    signinButton.click()

driver.implicitly_wait(3)

print("login successful")

