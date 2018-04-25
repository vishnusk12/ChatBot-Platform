'''
Created on 14-Nov-2017

@author: Vishnu
'''

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
import spacy
from pymongo import MongoClient

connection = MongoClient('52.221.4.121', 38128)
db = connection.botzup

nlp = spacy.load('en')

from .Entity import entities
from .CreateIntent import create
from .UpdateIntent import update
from .CreateEntity import create_entity
from .UpdateEntity import update_entity
from .EntityChecking import checking
from .CreatePrecommand import createprecommand
from .FetchPrecommand import trigger
from .Classifier import classifier

@permission_classes((permissions.AllowAny,))
class Entities(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        result = entities(question['messageText'])
        return Response(result)

@permission_classes((permissions.AllowAny,))
class Create(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        result = create(question)
        return Response(result)

@permission_classes((permissions.AllowAny,))    
class Update(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        result = update(question)
        return Response(result)
    
@permission_classes((permissions.AllowAny,))    
class CreateEntity(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        result = create_entity(question)
        return Response(result)
    
@permission_classes((permissions.AllowAny,))    
class UpdateEntity(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        result = update_entity(question)
        return Response(result)

@permission_classes((permissions.AllowAny,))    
class CheckEntity(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        result = checking(question['messageText'], question['agent_name'])
        return Response(result)
    
@permission_classes((permissions.AllowAny,))
class CreatePrecommand(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        result = createprecommand(question['agent_name'])
        return Response(result)
    
@permission_classes((permissions.AllowAny,))
class Trigger(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        result = trigger(question['agent_name'])
        return Response(result)

@permission_classes((permissions.AllowAny,))
class Classifier(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        result = classifier(question['agent_name'])
        return Response(result)
