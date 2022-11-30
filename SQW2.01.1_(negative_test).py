from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

# PATH = "C:\\Users\\e190445\\Downloads\\chromedriver_win32\\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
#driver.get("https://mingle35-cloudidentities.inforgov.com/idp/SSO.saml2")

#driver = webdriver.Chrome(executable_path="/resources/drivers/chromedriver.exe")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
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
    passwordfeild.send_keys("12Qah@02infor")
else:
    print("option not found")

driver.implicitly_wait(2)

signinButton = driver.find_element_by_xpath("//*[@class='ping-button normal allow']")
if signinButton.is_displayed():
    signinButton.click()

time.sleep(4)

driver.switch_to_frame(0)
print("switching in the frame")
time.sleep(2)
buyerOption = driver.find_element_by_xpath("(//*[@class='lm-card-title']/a/span)[2]")
if buyerOption.is_displayed():
    buyerOption.click()
else:
    buyerOption.click()

time.sleep(3)

print("login successful")

buyerTabOnBuyerPage = driver.find_element_by_xpath("(//*[text()='Buyer'])[3]")
if buyerTabOnBuyerPage.is_displayed():
    buyerTabOnBuyerPage.click()
else:
    buyerTabOnBuyerPage.click()

time.sleep(3)

hamburgerOption = driver.find_element_by_xpath("//*[@id='app-menu-trigger']")
if hamburgerOption.is_displayed():
    hamburgerOption.click()

time.sleep(2)

searchTextField = driver.find_element_by_xpath("//*[@id='application-menu-searchfield']")
if searchTextField.is_displayed():
    searchTextField.click()
    searchTextField.send_keys("supplier")
else:
    searchTextField.click()
    searchTextField.send_keys("supplier")
    time.sleep(4)


#driver.quit()
