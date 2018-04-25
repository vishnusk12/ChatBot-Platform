'''
Created on 09-Apr-2018

@author: Vishnu
'''

from .Entity import entities
import re
from .views import db
from sklearn.externals import joblib

def checking(text, agent_name):
    data_intent = list(db.intents.find({'agent_name': agent_name}))
    data_entity = list(db.entity.find({'agent_name': agent_name}))
    system_entity = entities(text)
    model = joblib.load('/home/dev/Botzup/Botzup/' + agent_name + '.pkl')
#     model = joblib.load('C:/Users/hp/eclipse-workspace/Botzup/Botzup/' + agent_name + '.pkl')
    prediction = model.classify(text)
    new_intent = []
    dic = {}
    dic['intent_name'] = prediction
    new_intent.append(dic)
    try:
        entity_list = [i['entities'] for i in data_entity] + [i['entities'] for i in data_intent if i['intent_name'] == prediction]
    except:
        entity_list = [i['entities'] for i in data_entity]
    entity_list = dict([(key, d[key]) for d in entity_list for key in d])
    entity = []
    for key, value in entity_list.items():
        for m in value:
            match = re.compile(r"\b%s\b"%(m.lower()))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_ = {}
                dict_[key] = m
                entity.append(dict_)
    dict_entity = {}
    list_entity = []
    dict_entity['custom_entity'] = dict([(key,d[key]) for d in entity for key in d])
    dict_entity['system_entity'] = dict([(key,d[key]) for d in system_entity['property'] for key in d])
    list_entity.append(dict_entity)
    result = new_intent + list_entity
    result = dict([(key, d[key]) for d in result for key in d])
    return result
