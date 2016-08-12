
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import settings
import math
import os
import requests
import robobrowser

#login
#http://www.movescount.com/auth?redirect_uri=%2foverview

br = robobrowser.RoboBrowser(history=True)

url = "http://www.movescount.com/auth?redirect_uri=%2foverview"

br.open(url)
forms = br.get_forms()

print(forms)
print()
print()

form = br.get_form(action="./auth?redirect_uri=%2foverview")

print(form)
print()
print()

form['email'].value = settings.email
form['password'].value = settings.password
#br.session.headers['Referer'] = url

form["__VIEWSTATE"].value = "/wEPDwUKLTc2MTAxNzQ4MmRkr/lAhZYueBNtINpuoLA7vkegEho="
form["__VIEWSTATEGENERATOR"].value = "CB4E55BE"
form.serialize()
print(form)

br.submit_form(form)








'''
#"http://www.movescount.com/latestmove"
response = requests.get("http://www.movescount.com/latestmove")
#print(response.headers)
#"export?id=117769218&format=xlsx"

html = response.text
#print(html)

soup = BeautifulSoup(html, "html.parser")

print(soup.find_all("link", limit=3))


data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "workbooks")
file_name = "Move_2016_08_10_16_46_13.xlsx"

wb = load_workbook(os.path.join(data_path, file_name))

x_values = []
x_sum = 0

ws = wb.active

start_row = 3
start_column = 40
measurement_length = 180


for row in range(start_row, start_row + measurement_length):
	next_cell = ws.cell(column=start_column, row=row).value
	x_values.append(next_cell)
	x_sum = x_sum + next_cell


mean = x_sum / measurement_length

sum_of_squared_errors = 0
for x in x_values:
	sq_error = x - mean
	sum_of_squared_errors = sum_of_squared_errors + (sq_error * sq_error)


variance = sum_of_squared_errors / (measurement_length - 1)
std_deviation = math.sqrt(variance)

print(std_deviation)
'''
