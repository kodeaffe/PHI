# -*- coding: utf-8 -*-
"""
Admin configuration of construction_systems app
"""

from django.contrib import admin

from .models import (
    CompanyAddress,
    Company,
    ConstructionSystemCategory,
    ConstructionSystem,
)


class ConstructionSystemAdmin(admin.ModelAdmin):
    list_display = ['name', 'component_id', 'category', 'certification_date']


admin.site.register(ConstructionSystem, ConstructionSystemAdmin)
admin.site.register([
    CompanyAddress,
    Company,
    ConstructionSystemCategory,
])
