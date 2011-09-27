#!/bin/env python
#encoding=utf-8
'''
Customized model defination.
'''

import web
from sqlalchemy import Table, Column, Integer, Boolean, String, DateTime, TIMESTAMP, Text
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref, deferred

from common import Base, engine
from common.dbutil import utcnow


class Model(Base):
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    title = Column(String(32))
    is_active = Column(Boolean, default=False)

    fields = relationship("Field", backref=backref('model'))
    relations = relationship("Relation", backref=backref('model'))

    def __repr__(self):
        return "<Model('%s')>" % (self.name)

class Field(Base):
    __tablename__ = 'model_field'
    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    title = Column(String(32))
    type = Column(String(16), nullable=False)
    length = Column(Integer)
    model_id = Column(Integer, ForeignKey('model.id'))

    def __repr__(self):
        return "<Field('%s')>" % (self.name)

class Relation(Base):
    __tablename__ = 'model_relation'
    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    title = Column(String(32))
    type = Column(String(16), nullable=False)
    target = Column(String(16))
    backref = Column(String(16))
    secondary = Column(String(16))

    model_id = Column(Integer, ForeignKey('model.id'))

    def __repr__(self):
        return "<Relation('%s')>" % (self.name)


metadata = Base.metadata


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        metadata.create_all(engine)
    elif sys.argv[1].lower() == 'drop':
        metadata.drop_all(engine)

