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


class CompanyAddressInline(admin.TabularInline):
        model = CompanyAddress

class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        CompanyAddressInline,
    ]


admin.site.register(Company, CompanyAdmin)


class ConstructionSystemAdmin(admin.ModelAdmin):
    list_display = ['name', 'component_id', 'category', 'certification_date']


admin.site.register(ConstructionSystem, ConstructionSystemAdmin)


admin.site.register([
    CompanyAddress,
    ConstructionSystemCategory,
])
