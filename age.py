import tabula as tb
import pandas as pd


# file = "BUNN, KEITH CARMELL.pdf"
# table = tb.read_pdf(file, pages='all')
# csv_table = tb.convert_into(file,'pdf_convert8.csv',pages="all")


#def csv34(item):
   # table = tb.read_pdf(item, pages='all')
   # csv_table = tb.convert_into(item, 'pdf_convert91.csv')

  #  print(csv_table)


#csv34("immu.pdf")

import PyPDF2

pdfFileObject = open("immrecord.pdf", 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObject)



pageObject = pdfReader.getPage(0)

text = pageObject.extractText()

month1 =[]
day1 = []
year1 = []


for line in text.splitlines()[4:5]:
    field = line.split("/")
    month1.append(field[0])
    day1.append(field[1])
    year1.append(field[2])


print(field)
month = []

for i in month1:
    for x in i:
        if x in ["0","1","2","3","4","5","6","7","8","9","10","11","12"]:
            month.append(x)

day = []

for i in day1:
    for x in i:
        if x in ["0","1","2","3","4","5","6","7","8","9","10","11","12"]:
            day.append(x)
year = []
for i in year1:
    for x in i:
        if x in ["0","1","2","3","4","5","6","7","8","9","10","11","12"]:
            year.append(x)

year = year[0:4]
monthstr = ""
daystr = ""
yearstr = ""
for i in month:
    monthstr = monthstr + i
for i in day:
    daystr = daystr + i
for i in year:
    yearstr = yearstr + i

intmonth = int(monthstr)
intday = int(daystr)
intyear = int(yearstr)

import datetime

# using now() to get current time
current_time = datetime.datetime.now()





today_year = current_time.year


today_month = current_time.month


today_day = current_time.day

today_year = int(today_year)
today_month = int(today_month)
today_day = int(today_day)


from datetime import date


def numOfDays(date1, date2):
    return (date2 - date1).days





# Driver program
date1 = date(intyear, intmonth, intday)
date2 = date(today_year, today_month, today_day)
day = numOfDays(date1, date2)

age = int(day / 365)
print(age)






