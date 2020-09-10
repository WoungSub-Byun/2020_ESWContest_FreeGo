from sqlalchemy import Column, String, Integer, Date, ForeignKey
from .db import Base

class USERS_TB(Base):
    __tablename__ = 'USERS_TB'

    id = Column(String(30), primary_key=True)
    pwd = Column(String(50))

    def __init__(self, id, pwd):
        self.id = id
        self.pwd = pwd

    def __repr__(self):
        return "USERS_TB(id={}, pw={})".format(self.id, self.pwd)


class PRODUCT_TB(Base):
    __tablename__ = 'PRODUCT_TB'

    id = Column(String(30), primary_key=True, ForeignKey=('USERS_TB.id'))
    p_name = Column(String(50), primary_key=True)
    p_number = Column(Integer)
    p_ex_date = Column(Date, index=True)
    img_link = Column(String)

    def __init__(self, id, p_name, p_number, p_ex_date, img_link):
        self.id = id
        self.p_name = p_name        
        self.p_number = p_number
        self.p_ex_date = p_ex_date
        self.img_link = img_link

    def __repr__(self):
        return "Food( id={}, p_name={}, p_number={}, p_ex_date={}, img_link={})".format( self.id, self.p_name, self.p_number, self.p_ex_date, self.img_link)