from openpyxl import load_workbook
import pandas as pd
wb = load_workbook('БД школа.xlsx')
ws = wb.active
# ws.print_area = 'A1:B2'