# -*- coding: utf-8 -*-
"""
URLs for construction_systems app
"""

from django.conf.urls import url
from .views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
]
