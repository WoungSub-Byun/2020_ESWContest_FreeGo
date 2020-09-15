from flask import Blueprint
from flask import redirect
from flask import request
from flask import jsonify
from ..service import user_service

api = Blueprint("auth", __name__, url_prefix='/auth')



@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    result = user_service.register_user(data['id'], data['pwd'])
    if result == 'fail':
        return jsonify({"code": 400,
                        "message":"fail"})
    elif result == "id existed":
        return jsonify({"code": 400, "message": "id already existed"})
    return jsonify({"code": 200,
                    "message": "register success"})


@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    id = data["id"]
    password = data["pwd"]

    result = user_service.login_user(id, password)

    if result == 'fail':
        return jsonify({"code": 400, "message":"fail"})
    elif result == "id not found":
        return jsonify({"code": 404, "message": "id not found"})
    elif result == "pwd is wrong":
        return jsonify({"code" : 404, "message": "pwd is wrong"})
    else:
        return jsonify({"code": 200, "message": "login success"})

        

@api.route('/finduser/<username>', methods=['GET'])
def find_user(username):
    result = user_service.find_user(username)

    if result == 'fail':
        return jsonify({"code": 400, "message": "fail"})
    elif result == True:
        return jsonify({"code": 200, "message": "existed"})
    elif not result:
        return jsonify({"code": 404, "message": "not exist"})