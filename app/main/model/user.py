from ..db import Base
from sqlalchemy import Column, String
from .. import db, flask_bcrypt


class USERS_TB(Base):
    __tablename__ = 'USERS_TB'

    id = Column(String(30), primary_key=True)
    pwd_hash = Column(String(100))

    def __init__(self, id, pwd_hash):
        self.id = id
        self.pwd_hash = pwd_hash

    @property
    def password(self):
        raise AttributeError('pwd: write-only field')

    @password.setter
    def password(self, password):
        self.pwd_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.pwd_hash, password)
    
    def __repr__(self):
        return "<user - {} >".format(self.id)