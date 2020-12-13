from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config import Base
import uuid

class User(Base):
    __tablename__ = "users"

    def __init__(self, first_name, last_name, email, password, birthday = None, phone_number = None, role = 'user'):
        self.id = str(uuid.uuid1())
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.role = role

    id = Column(String(36), primary_key=True, nullable=False)
    first_name = Column(String(1000), nullable=False)
    last_name = Column(String(1000))
    birthday = Column(Date)
    email = Column(String(365), nullable=False)
    phone_number = Column(String(50))
    password = Column(String(5000), nullable=False)
    role = Column(String(30), nullable=False)


class Medicine(Base):
    __tablename__ = "medicines"

    def __init__(self, name, price, amount):
        self.id = str(uuid.uuid1())
        self.name = name
        self.price = price
        self.amount = amount

    id = Column(String(36), primary_key=True, nullable=False)
    name = Column(String(1000), nullable=False)
    price = Column(Float, nullable=False)
    amount = Column(Integer, nullable=False)


class Buy(Base):
    __tablename__ = "buys"

    def __init__(self, user_id, medicine_id, amount):
        self.id = str(uuid.uuid1())
        self.user_id = user_id
        self.medicine_id = medicine_id
        self.amount = amount

    id = Column(String(36), primary_key=True, nullable=False)
    amount = Column(Integer, nullable=False)
    user_id = Column(String(36), ForeignKey(User.id), nullable=False)
    user = relationship(User)
    medicine_id = Column(String(36), ForeignKey(Medicine.id), nullable=False)
    medicine = relationship(Medicine)


class Demand(Base):
    __tablename__ = "demands"

    def __init__(self, user_id, medicine_id, amount):
        self.id = str(uuid.uuid1())
        self.user_id = user_id
        self.medicine_id = medicine_id
        self.amount = amount

    id = Column(String(36), primary_key=True, nullable=False)
    amount = Column(Integer, nullable=False)
    user_id = Column(String(36), ForeignKey(User.id), nullable=False)
    user = relationship(User)
    medicine_id = Column(String(36), ForeignKey(Medicine.id), nullable=False)
    medicine = relationship(Medicine)