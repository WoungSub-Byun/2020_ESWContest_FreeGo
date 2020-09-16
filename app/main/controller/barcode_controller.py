from flask import Blueprint
from flask import jsonify
from ..model import find_code
import sqlite3


api = Blueprint("code", __name__, url_prefix='/code')

#Lookup the gtin num in database
@api.route('/lookupcode/<int:code>', methods=['GET'])
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

