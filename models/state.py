#!/usr/bin/python3
""" state module """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        values_city = models.storage.all()
        list_city = []
        result = []
        for key in values_city:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                list_city.append(values_city[key])
        for elem in list_city:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
