import sqlite3

def find_code(GTIN):
    conn = sqlite3.connect('barcode.db')
    cs = conn.cursor()

    query = "select * from BARCODE_TB where GTIN={}".format(GTIN)
    cs.execute(query)
    rows = cs.fetchall()
    conn.close()
    if not rows:
        return False
    return list(rows[0])
