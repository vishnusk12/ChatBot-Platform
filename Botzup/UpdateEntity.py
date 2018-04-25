'''
Created on 06-Apr-2018

@author: Vishnu
'''

from .views import db

def update_entity(json):
    agent_name = json['agent_name']
    entity = json['entity']
    db.entity.update({'agent_name': agent_name}, 
                     {'agent_name': agent_name,
                      'entities': entity})
