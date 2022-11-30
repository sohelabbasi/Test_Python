# import pandas as pd
import xlrd
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

FILEPATH = "C:\\Users\\13479\\PycharmProjects\\PythonTesting\\Marketing Data.xlsx"
workbook = xlrd.open_workbook(FILEPATH)
worksheet = workbook.sheet_by_index(1)

print(worksheet.ncols)
print(worksheet.nrows)


driver = webdriver.Chrome(worksheet.cell_value(1, 5))

driver.get(worksheet.cell_value(1, 6))
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.current_url)
print(driver.title)

firstnamevalue = worksheet.cell_value(1, 1)
phonevalue = worksheet.cell_value(1, 3)
emailvalue = worksheet.cell_value(1, 4)

driver.implicitly_wait(5)
firstNamefeild = driver.find_element_by_name("firstName")
if firstNamefeild.is_displayed():
    firstNamefeild.click()
    firstNamefeild.clear()
    firstNamefeild.send_keys(firstnamevalue)
else:
    print("option not found")

lastNamefeild = driver.find_element_by_name("lastName")
if lastNamefeild.is_displayed():
    lastNamefeild.click()
    lastNamefeild.clear()
    lastNamefeild.send_keys(worksheet.cell(1, 2))
else:
    print("option not found")

driver.implicitly_wait(3)

phonefeild = driver.find_element_by_name("phone")
if phonefeild.is_displayed():
    phonefeild.click()
    phonefeild.clear()
    phonefeild.send_keys(phonevalue)
else:
    print("option not found")

driver.implicitly_wait(3)

emailfeild = driver.find_element_by_name("userName")
if emailfeild.is_displayed():
    emailfeild.click()
    emailfeild.clear()
    emailfeild.send_keys(emailvalue)
else:
    print("option not found")

driver.implicitly_wait(3)
print("login successful")

driver.close()