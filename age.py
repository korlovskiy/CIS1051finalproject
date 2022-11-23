import tabula as tb
import pandas as pd
# Importing the os library
import os

# Inbuilt function to remove files


# file = "BUNN, KEITH CARMELL.pdf"
# table = tb.read_pdf(file, pages='all')
# csv_table = tb.convert_into(file,'pdf_convert8.csv',pages="all")


#  print(csv_table)


# csv34("immu.pdf")

# The code with run the CSV file if the age is met to be true

import PyPDF2
from datetime import date


def numOfDays(date1, date2):
    return (date2 - date1).days


def age(filename):
    file = filename + ".pdf"

    pdfFileObject = open(file, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

    pageObject = pdfReader.getPage(0)

    text = pageObject.extractText()

    month1 = []
    day1 = []
    year1 = []

    for line in text.splitlines()[4:5]:
        field = line.split("/")
        month1.append(field[0])
        day1.append(field[1])
        year1.append(field[2])

    month = []

    for i in month1:
        for x in i:
            if x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
                month.append(x)

    day = []

    for i in day1:
        for x in i:
            if x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
                day.append(x)
    year = []
    for i in year1:
        for x in i:
            if x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
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

    current_time = datetime.datetime.now()

    today_year = current_time.year

    today_month = current_time.month

    today_day = current_time.day

    today_year = int(today_year)
    today_month = int(today_month)
    today_day = int(today_day)

    date1 = date(intyear, intmonth, intday)
    date2 = date(today_year, today_month, today_day)
    day = numOfDays(date1, date2)

    user_age = int(day / 366)
    return user_age


def appropriate_age(file):
    user_age = age(file)
    if user_age >= 19:
        return True
    else:
        print("You need to be 19 and up to use this code: ")
        print("Come back in", 19 - user_age, "year(s).")
        return False


# use tabula to read the file as a pdf to csv and manipulate
def CSV_creation(file):
    if appropriate_age(file):
        file = file + ".pdf"
        tb.read_pdf(file, pages="all")
        name = 'imm_to_csv'
        tb.convert_into(file, name, pages="all")
        # os.remove('pdf_convert102.csv')
        # print("File removed successfully")
        return name
def CSV_reading(file):
    name = CSV_creation(file)
    firstname = []
    lastname = []
    racetime = []
    personalbest = []
    data = open(filename, 'r')
    for line in data:
        fields = line.split(",")
        firstname.append(fields[0])
        lastname.append(fields[1])
        racetime.append(int(fields[2]))
        personalbest.append(int(fields[3]))
    return firstname, lastname, racetime, personalbest


def isfilename(file):
    file = file + ".pdf"
    try:
        open(file, 'rb')
        return True
    except:
        return False


print("Make sure that the file and the code are both in the same folder")

filename = input("Enter the name of the immunization record file without the .pdf: ")

while not isfilename(filename):
    print("Make sure that the pdf file is in the same folder as the Python program :).")
    filename = input("Enter the name of the immunization record file without the .pdf: ")
    isfilename(filename)

CSV_creation(filename)
