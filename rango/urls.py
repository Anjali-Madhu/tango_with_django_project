# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:43:50 2020

@author: anjali

"""
from django.urls import path
from rango import views

app_name = 'rango'
urlpatterns = [
        path('',views.index,name='index'),
        path('about/',views.about,name='about'),
        path('category/<slug:category_name_slug>/',views.show_category,name='show_category'),
        
        ]

