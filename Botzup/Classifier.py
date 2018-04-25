# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 12:04:37 2018

@author: Vishnu
"""

from textblob.classifiers import DecisionTreeClassifier
from sklearn.externals import joblib
from .views import db

def classifier(agent_name):
    data_intent = list(db.intents.find({'agent_name': agent_name}))
    list_intent = []
    for i in data_intent:
        dict_intent = {}
        dict_intent[i['intent_name']] = i['user_expressions']
        list_intent.append(dict_intent)
    intent_list = dict([(key, d[key]) for d in list_intent for key in d])
    d = {i: k for k, v in intent_list.items() for i in v}
    train = list(d.items())
    clf = DecisionTreeClassifier(train)
    joblib.dump(clf, '/home/dev/Botzup/Botzup/' + agent_name + '.pkl')
#     joblib.dump(clf, 'C:/Users/hp/eclipse-workspace/Botzup/Botzup/' + agent_name + '.pkl')
