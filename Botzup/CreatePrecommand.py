'''
Created on 18-Apr-2018

@author: Vishnu
'''

from .views import db

def createprecommand(json):
    db.trigger.insert_one(json)
