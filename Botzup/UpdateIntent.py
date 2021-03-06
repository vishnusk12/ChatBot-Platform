'''
Created on 05-Apr-2018

@author: Vishnu
'''

from .views import db

def update(json):
    agent_name = json['agent_name']
    intent_name = json['intent_name']
    exp = json['user_expressions']
    ent = json['entities']    
    resp = json['responses']
    db.intents.update({'intent_name': intent_name}, 
                      {'agent_name': agent_name, 
                       'intent_name': intent_name, 
                       'user_expressions': exp, 
                       'responses': resp,
                       'entities': ent})
