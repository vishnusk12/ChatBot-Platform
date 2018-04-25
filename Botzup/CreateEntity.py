'''
Created on 06-Apr-2018

@author: Vishnu
'''

from .views import db

def create_entity(json):
    agent_name = json['agent_name']
    entity = json['entity']
    db.entity.insert_one({'agent_name': agent_name, 
                          'entities': entity})
