import tabula as tb
import pandas as pd


#file = "BUNN, KEITH CARMELL.pdf"
#table = tb.read_pdf(file, pages='all')
#csv_table = tb.convert_into(file,'pdf_convert8.csv',pages="all")



def csv34(item):
    table = tb.read_pdf(item, pages='all')
    csv_table = tb.convert_into(item, 'pdf_convert90.csv', pages="all")

    print(csv_table)

