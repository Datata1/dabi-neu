from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Basis-Klasse für ORM-Modelle
Base = declarative_base()    
    
class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    order_number = Column(String, nullable=False)
    user_id = Column(Integer)
    day_of_the_week = Column(Integer)
    hour_of_day = Column(Integer)
    days_since_prior_order = Column(Float, nullable=True)
    tips = Column(Boolean, default=None, nullable=True)

    products = relationship("Product", secondary="einkaufskorb", back_populates="orders")
    einkaufskorb = relationship("Einkaufskorb", back_populates="order", overlaps="products")



class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    aisle_id = Column(Integer, ForeignKey('aisles.aisle_id'))
    department_id = Column(Integer, ForeignKey('departments.department_id'))

    orders = relationship("Order", secondary="einkaufskorb", back_populates="products", overlaps="einkaufskorb")
    einkaufskorb = relationship("Einkaufskorb", back_populates="product", overlaps="orders,products")

    aisle = relationship("Aisle", back_populates="products")
    department = relationship("Department", back_populates="products")


class Einkaufskorb(Base):
    __tablename__ = 'einkaufskorb'

    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    add_to_cart_order = Column(Integer)

    order = relationship("Order", back_populates="einkaufskorb", overlaps="orders,products")
    product = relationship("Product", back_populates="einkaufskorb", overlaps="orders,products")


class Aisle(Base):
    __tablename__ = 'aisles'

    aisle_id = Column(Integer, primary_key=True)
    aisle_name = Column(String)

    products = relationship("Product", back_populates="aisle")


class Department(Base):
    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True)
    department_name = Column(String)

    products = relationship("Product", back_populates="department")
