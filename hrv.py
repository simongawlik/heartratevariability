
from openpyxl import load_workbook
import os
import math

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