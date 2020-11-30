from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, nullable=False)
    first_name = Column(String(1000), nullable=False)
    second_name = Column(String(1000))
    birthday = Column(Date)
    email = Column(String(365), nullable=False)
    phone_number = Column(String(50))
    role = Column(String(30), nullable=False)


class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(String(36), primary_key=True, nullable=False)
    name = Column(String(1000), nullable=False)
    price = Column(Float(asdecimal=True), nullable=False)
    amount = Column(Integer, nullable=False)


class Buy(Base):
    __tablename__ = "buys"

    id = Column(String(36), primary_key=True, nullable=False)
    amount = Column(Integer, nullable=False)
    user_id = Column(String(36), ForeignKey(User.id), nullable=False)
    user = relationship(User)
    medicine_id = Column(String(36), ForeignKey(Medicine.id), nullable=False)
    medicine = relationship(Medicine)


class Demand(Base):
    __tablename__ = "demands"

    id = Column(String(36), primary_key=True, nullable=False)
    amount = Column(Integer, nullable=False)
    user_id = Column(String(36), ForeignKey(User.id), nullable=False)
    user = relationship(User)
    medicine_id = Column(String(36), ForeignKey(Medicine.id), nullable=False)
    medicine = relationship(Medicine)