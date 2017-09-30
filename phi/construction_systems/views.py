# -*- coding: utf-8 -*-
"""
Views of construction_systems app
"""

from django.views.generic.list import ListView

from .models import ConstructionSystem


class Index(ListView):
    """Index view for construction_systems"""
    model = ConstructionSystem
    template_name = "construction_systems/index.html"
