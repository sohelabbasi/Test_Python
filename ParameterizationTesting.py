import xlrd
from selenium import webdriver

FILEPATH = "TestData.xlsx"

#command to open workbook
workbook = xlrd.open_workbook(FILEPATH)

#command to open worksheet
worksheet = workbook.sheet_by_index(3)

#printing total number of rows and columns in the sheet
print(worksheet.nrows)
print(worksheet.ncols)

#username = []
#for y in range(1, worksheet.nrows):
#    username.append(worksheet.cell_value(y,1))
#print(username)


driver = webdriver.Chrome(worksheet.cell_value(1,6))
driver.maximize_window()
driver.delete_all_cookies()
driver.get(worksheet.cell_value(1,5))
print(driver.current_url)
print(driver.title)
Expected = "Google"
Actual = driver.title
assert Actual == Expected
print("Application has been launched successfully")
driver.close()










