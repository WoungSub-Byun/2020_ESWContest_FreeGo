import datetime
from flask import Blueprint
from flask import redirect
from flask import request
from flask import jsonify
from ..service import product_service
from ..model.find_code import find_code

api = Blueprint("material", __name__, url_prefix='/material')

@api.route('/show/<username>', methods=['GET'])
def show_entry(username):
    result = product_service.show_data(username)

    if result == 'fail':
        return jsonify({"code":404,
                        "message" : "fail"})

    return jsonify({"code":200,
                    "message": "success",
                    "data": result})
    
@api.route('/find/<username>', methods=['GET'])
def find_data(username):
    id = username
    p_name = request.args.get('p_name','fail')
    
    result = product_service.find_data(id, p_name)
    if result == 'fail':
        return jsonify({"code":404,
                        "message" : "fail"})

    return jsonify({"code":200,
                    "message": "success",
                    "data": result})

@api.route('/late/<username>', methods=['GET'])
def show_lated(username):
    result = product_service.find_lated(username)
    if len(result) == 0:
        return jsonify({"code": 200,
                    "message": "no lated data"})
    elif result == 'fail':
        return jsonify({"code":404,
                        "message" : "fail"})
    return jsonify({"code": 200,
                    "message": "success",
                    "data": result})


@api.route('/update', methods=['PUT'])
def update_entry():
    if request.method == 'PUT':
        data = request.get_json()
        
        id = data["id"]
        p_name = data["p_name"]
        p_number = data["p_number"]
        
        p_number = int(p_number)
        _existed = product_service.find_data(id, p_name)

        if _existed:
            result = product_service.update_data(id, p_name, p_number)
        else:
            return jsonify({"code": 404,
                        "message": "fail"})
        if result == 'fail':
            return jsonify({"code": 404,
                        "message": "fail"})

        return jsonify({"code": 200,
                        "message": "success"})

@api.route('/insert', methods=['POST'])
def insert_entry():
    if request.method == 'POST':
        code = request.args.get("code")
        has_img = find_code(code)
        img_link = ""
        if has_img:
            img_link = has_img[4]
        data =  request.get_json()

        id = data["id"]
        p_name = data["p_name"]

        _existed = product_service.find_data(id, p_name)
        
        if not _existed:
            p_number = data["p_number"]
            p_ex_date = data["p_ex_date"]
            
            p_number = int(p_number)
            p_ex_date = datetime.datetime.strptime(str(p_ex_date), "%Y-%m-%d").date()
                
            result = product_service.insert_data(id , p_name, p_number, str(p_ex_date), img_link)

            if result == 'fail':
                return jsonify({"code": 404,
                        "message": "fail"})
            return jsonify({"code": 200,
                            "message": "success"})
        else:
            return jsonify({"code": 404,
                            "message": "already exist"})

# Delete data from database
@api.route('/delete', methods=['DELETE'])
def delete_entry():
    data = request.get_json()
    result = product_service.delete_data(data["id"], data["p_name"])

    if result == 'fail':
        return jsonify({"code": 404,
                        "message": "fail"})

    return jsonify({"code": 200,
                    "message":"success"})