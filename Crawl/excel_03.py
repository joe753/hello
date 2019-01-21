import openpyxl
from openpyxl.chart import (
    Reference,
    BarChart
)



book = openpyxl.Workbook()
sheet = book.active

rows = [
    ['김일수', 33],
    ['김이수', 11],
    ['김삼수', 55],
    ['김사수', 22],
    ['김오수', 5],
    ['김육수', 43],
    ['김칠수', 27],
    ['김팔수', 91],
]

for row in rows:
    sheet.append(row)

datax = Reference(sheet, min_col=2, 
		min_row=1, max_col=2, max_row=len(rows))
categs = Reference(sheet, min_col=1,
				 min_row=1, max_row=len(rows))

chart = BarChart()
chart.add_data(data=datax)
chart.set_categories(categs)

chart.legend = None  # 범례
chart.varyColors = True
chart.title = "차트 타이틀"

sheet.add_chart(chart, "A10")


book.save("./data/output2.xlsx")