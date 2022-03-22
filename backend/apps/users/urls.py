# -*- coding: utf-8 -*-
""" 
@author: xingxingzaixian
@create: 2020/9/6
@description: 
"""
from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import LoginView, RegisterView, UserViewset, RoleViewset, ClassViewset


router = SimpleRouter()
router.register('user', UserViewset)
router.register('role', RoleViewset)
router.register('class', ClassViewset)

urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
]

urlpatterns += router.urls
