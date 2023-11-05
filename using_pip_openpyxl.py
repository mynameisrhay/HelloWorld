import openpyxl as xl
wb = xl.load_workbook("transactions.xlsx")
sheet = wb['Sheet1']
cell = sheet.cell(1, 1)
print(f'Cell value of A1 is {cell.value}')
cell = sheet.cell(1, 2)
print(f'Cell value of B2 is {cell.value}')
# cell = sheet.cell(X or column, Y or row)

max_row = sheet.max_row
print(f'''Max row for this spreadsheet is {max_row}
''')

print("will reiterate the contents of C2 to C4 cells below:")
for row in range(2, max_row + 1):
    cell = sheet.cell(row, 3)
    print(cell.value)
