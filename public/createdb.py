import sqlite3, os
import numpy as np
import pandas as pd

def createTable():    
    os.chdir('C:\\workspace\\freego\\client\\public')
    conn = sqlite3.connect('barcode.db')
    cs = conn.cursor()

    xls = pd.read_excel('barcodedata.xlsx')
    header = xls.columns.tolist()

    query = '''CREATE TABLE IF NOT EXISTS BARCODE_TB(
                    "{0}" TEXT PRIMARY KEY NOT NULL,
                    "{1}" TEXT,
                    "{2}" TEXT,
                    "{3}" TEXT,
                    "{4}" TEXT
        );'''.format(header[0], header[1], header[2], header[3], header[4])
    cs.execute(query)
    conn.commit()

def Insert():
    os.chdir('C:\\workspace\\freego\\client\\public')
    conn = sqlite3.connect('barcode.db')
    cs = conn.cursor()
    xls = pd.read_excel('barcodedata.xlsx')
    header = xls.columns.tolist()
    contents = xls.values.tolist()

    for i in range(len(contents)):
        VALUES = InsertValue(contents, 0, len(header), i)
        query = f'INSERT INTO BARCODE_TB ("GTIN","DSCRGTINK","NVL(MENUFACT,CONAMEK)","COUNTRYDESCR","IMGPATH1") VALUES ({VALUES})'
        cs.execute(query)
    conn.commit()
    conn.close()

def ColumnSelect(HEADER, a, b):
    text=""
    for i in range(a, b):
        text+= '"'+HEADER[i]+'",'
    text=text[:-1]
    return text

def InsertValue(CONTENTS, a, b, k):
    text=""
    for i in range(a, b):
        value = str(CONTENTS[k][i])
        if '"' in value:
            value = value.replace('"','')
        text += '"' + value+'",'
    text=text[:-1]
    return text

def selectValue():
    os.chdir('C:\\workspace\\freego\\client\\public')
    conn = sqlite3.connect('barcode.db')
    cs = conn.cursor()

    query = "select * from BARCODE_TB"
    cs.execute(query)
    rows = cs.fetchall()
    if not rows:
        print("table is empty")
    for row in rows:
        print(row)
    conn.close()

def find():
    os.chdir('C:\\workspace\\freego\\client\\public')
    xls = pd.read_excel('barcodedata.xlsx')
    header = xls.columns.tolist()
    contents = xls.values.tolist()

    for i in range(len(contents)):
        for j in range(len(header)):
            if '미닛메이드' in str(contents[i][j]):
                print("index is [{}][{}]".format(i,j)+" data is: {}".format(contents[i][j]))

def main():
    createTable()
    Insert()

main()