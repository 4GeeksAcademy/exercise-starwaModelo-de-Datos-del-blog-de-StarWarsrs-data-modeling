import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    user_favorite = relationship("Favorite", backref="user", uselist=True)




class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    person = relationship(User)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String, nullable=False )
    planets_favorite =relationship("Favorite", backref="planet", uselist=True)

 
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)    
    age = Column(Integer, unique=False, nullable=False)
    gender = Column(String(120), nullable=False)
    people_favorite = relationship("Favorite", backref="people", uselist=True)
    
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
