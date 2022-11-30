import xlrd
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

FILEPATH = "C:\\Users\\13479\\PycharmProjects\\PythonTesting\\Marketing Data.xlsx"
workbook = xlrd.open_workbook(FILEPATH)
worksheet = workbook.sheet_by_index(1)

print(worksheet.ncols)
print(worksheet.nrows)
print(worksheet.cell_value(1, 6))