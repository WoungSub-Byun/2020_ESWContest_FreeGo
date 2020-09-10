from flask import Blueprint
from flask import jsonify
import sqlite3

bp = Blueprint("code", __name__, url_prefix='./code')

#Lookup the gtin num in database
@bp.route('/lookupcode/<int:code>', methods=['GET'])
def select_barcode(code):
    result = find_code(code)

    if not result: #There's no data for barcode from user
        return jsonify({"code": 404,
                        "message": "fail"})
    # result = json.dumps({"gtin": result[0],
    #                     "p_desc": result[1],
    #                     "p_country": result[2],
    #                     "p_img": result[3]})
    return jsonify({"code": 200,
                    "message": "success",
                    "data": result})

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

