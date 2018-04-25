"""Botzup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from .views import Entities, Create, Update, CreateEntity, UpdateEntity, CheckEntity, CreatePrecommand, Trigger, Classifier
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'entities', Entities, 'Entities')
router.register(r'createintent', Create, 'Create')
router.register(r'updateintent', Update, 'Update')
router.register(r'createentity', CreateEntity, 'CreateEntity')
router.register(r'updateentity', UpdateEntity, 'UpdateEntity')
router.register(r'checkentity', CheckEntity, 'CheckEntity')
router.register(r'createprecommand', CreatePrecommand, 'CreatePrecommand')
router.register(r'trigger', Trigger, 'Trigger')
router.register(r'classifier', Classifier, 'Classifier')
urlpatterns = [url(r'^', include(router.urls)), ]
