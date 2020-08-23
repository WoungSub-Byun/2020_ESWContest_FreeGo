from flask import Flask, request, jsonify
import json
import datetime
import sqlite3, os
from orm import controller


app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return jsonify({"code":200,
                    "message": "hellouser"})

@app.route('/init', methods=['GET'])
def create_table():
    result = controller.create_table()

    if result == 'fail':
        return jsonify({"code" : 400,
                    "message": "fail"})

    return jsonify({"code" : 200,
                    "message": "success"})

@app.route('/register', methods=['POST'])
def register_entry():

    data = request.get_json()
    
    result = controller.register_user(data['id'], data['pwd'])
    if result == 'fail':
        return jsonify({"code": 400,
                        "message":"fail"})
    elif result == "id existed":
        return jsonify({"code": 400, "message": "id already existed"})
    return jsonify({"code": 200,
                    "message": "register success"})

@app.route('/finduser/<username>', methods=['GET'])
def find_user(username):
    result = controller.find_user(username)

    if result == 'fail':
        return jsonify({"code": 400, "message": "fail"})
    elif result == True:
        return jsonify({"code": 200, "message": "existed"})
    elif not result:
        return jsonify({"code": 404, "message": "not exist"})



@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    id = data["id"]
    password = data["pwd"]

    result = controller.login_user(id, password)

    if result == 'fail':
        return jsonify({"code": 400, "message":"fail"})
    elif result == "id not found":
        return jsonify({"code": 404, "message": "id not found"})
    elif result == "pwd is wrong":
        return jsonify({"code" : 404, "message": "pwd is wrong"})
    else:
        return jsonify({"code": 200, "message": "login success"})


@app.route('/show/<username>', methods=['GET'])
def show_entry(username):
    result = controller.show_data(username)

    if result == 'fail':
        return jsonify({"code":404,
                        "message" : "fail"})

    return jsonify({"code":200,
                    "message": "success",
                    "data": result})

@app.route('/find/<username>', methods=['GET'])
def find_data(username):
    id = username
    p_name = request.args.get('p_name','fail')
    
    result = controller.find_data(id, p_name)
    if result == 'fail':
        return jsonify({"code":404,
                        "message" : "fail"})

    return jsonify({"code":200,
                    "message": "success",
                    "data": result})


@app.route('/late/<username>', methods=['GET'])
def show_lated(username):
    result = controller.find_lated(username)
    if len(result) == 0:
        return jsonify({"code": 200,
                    "message": "no lated data"})
    elif result == 'fail':
        return jsonify({"code":404,
                        "message" : "fail"})
    return jsonify({"code": 200,
                    "message": "success",
                    "data": result})
    

@app.route('/update', methods=['PUT'])
def update_entry():
    if request.method == 'PUT':
        data = request.get_json()
        
        id = data["id"]
        p_name = data["p_name"]
        p_number = data["p_number"]
        
        p_number = int(p_number)
        _existed = controller.find_data(id, p_name)

        if _existed:
            result = controller.update_data(id, p_name, p_number)
        else:
            return jsonify({"code": 404,
                        "message": "fail"})
        if result == 'fail':
            return jsonify({"code": 404,
                        "message": "fail"})

        return jsonify({"code": 200,
                        "message": "success"})

# Insert data
@app.route('/insert', methods=['POST'])
def insert_entry():
    if request.method == 'POST':
        
        data = data = request.get_json()
        id = data["id"]
        p_name = data["p_name"]

        _existed = controller.find_data(id, p_name)
        
        if not _existed:
            p_number = data["p_number"]
            p_ex_date = data["p_ex_date"]
            
            p_number = int(p_number)
            p_ex_date = datetime.datetime.strptime(str(p_ex_date), "%Y-%m-%d").date()
                
            result = controller.insert_data(id , p_name, p_number, str(p_ex_date))

            if result == 'fail':
                return jsonify({"code": 404,
                        "message": "fail"})
            return jsonify({"code": 200,
                            "message": "success"})
        else:
            return jsonify({"code": 404,
                            "message": "already exist"})
        
# Delete data from database
@app.route('/delete', methods=['DELETE'])
def delete_entry():
    data = request.get_json()
    result = controller.delete_data(data["id"], data["p_name"])

    if result == 'fail':
        return jsonify({"code": 404,
                        "message": "fail"})

    return jsonify({"code": 200,
                    "message":"success"})
##
#Use the Barcode
##
#Lookup the gtin num in database
@app.route('/lookupcode/<int:code>', methods=['GET'])
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




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
