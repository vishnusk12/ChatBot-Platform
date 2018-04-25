'''
Created on 18-Apr-2018

@author: Vishnu
'''

from .views import db

def trigger(agent_name):
    data = list(db.trigger.find({'agent_name': agent_name}))
    result = {}
    result['pre-commands']  = data[0]['pre-command']
    return result
