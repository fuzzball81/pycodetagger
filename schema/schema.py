#! /usr/bin/env python

# Schema file for the code tag database

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class FileList(Base):

    __tablename__ = 'filelist'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)


def __repr__(self):
    return "<FileList(id='{0}', name='{1}', path='{2}')>".format(self.id,
                                                                 self.name,
                                                                 self.path)

