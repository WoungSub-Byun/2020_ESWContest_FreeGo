from ..db import db_session
from ..model.user import USERS_TB

def register_user(id, pwd):
    try:
        if not find_user(id):
            table = USERS_TB(id = id, pwd = pwd)
            db_session.add(table)
            db_session.commit()
            return 'success'
        else:
            return "id already existed"
    except Exception as err:
        print("Error Log: [{}]".format(err))
        return 'fail'

def find_user(id):
    try:
        queries = db_session.query(USERS_TB).filter(USERS_TB.id == id)
        entry = [dict(id = q.id, pwd=q.pwd) for q in queries]
        if len(entry) == 0:
            return False
        else:
            return True
    except Exception as err:
        print('Error Log: [{}]'.format(err))
        return 'fail'

def login_user(id, pwd):
    try:
        queries = db_session.query(USERS_TB).filter(USERS_TB.id == id)
        entry = [dict(id = q.id, pwd=q.pwd) for q in queries]
        if len(entry) == 0:
            return "id not found"
        else:
            queries = db_session.query(USERS_TB).filter(USERS_TB.id == id).filter(USERS_TB.pwd == pwd)
            entry = entry = [dict(id = q.id, pwd=q.pwd) for q in queries]
            if len(entry) == 0:
                return "pwd is wrong"
            return "found"
    except Exception as err:
        print('Error Log: [{}]'.format(err))
        return 'fail'