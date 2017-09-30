# -*- coding: utf-8 -*-
"""
Models of construction_systems app
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _


class CompanyAddress(models.Model):
    """Defines a company's address"""

    street = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_('Street'),
        help_text=_('Street of the address'),
    )
    postcode = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default='',
        verbose_name=_('Post code'),
        help_text=_('Post code of the address (if applicable)'),
    )

    locality = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Locality'),
        help_text=_('Locality of the address, e.g. village, city'),
    )
    region = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Region'),
        help_text=_('Region of the address, e.g. state, province, county'),
    )
    country = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Country'),
        help_text=_('Country of the address, e.g. nation state'),
    )

    class Meta:
        ordering = ['street']
        verbose_name = _('Company Address')
        verbose_name_plural = _('Company Addresses')

    def __str__(self):
        return '{}, {}'.format(self.street, self.locality)


class Company(models.Model):
    """Defines a company"""

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        # unique=True,
        verbose_name=_('Name'),
        help_text=_('Name of the company'),
    )
    address = models.ForeignKey(
        CompanyAddress,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('Address'),
        help_text=_('Address of the company'),
    )

    class Meta:
        ordering = ['name']
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name


class ConstructionSystemCategory(models.Model):
    """Defines the category of a construction system"""

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        # unique=True,
        verbose_name=_('Name'),
        help_text=_('Name of the category'),
    )

    class Meta:
        ordering = ['name']
        verbose_name = _('Construction System Category')
        verbose_name_plural = _('Construction System Categories')

    def __str__(self):
        return self.name


class ConstructionSystem(models.Model):
    """Defines a construction system"""

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        # unique=True,
        verbose_name=_('Name'),
        help_text=_('Name of the construction system'),
    )
    component_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        # unique=True,
        verbose_name=_('Component ID'),
        help_text=_('Component ID of the construction system'),
    )
    category = models.ForeignKey(
        ConstructionSystemCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('Category'),
        help_text=_('Category of the construction system'),
    )
    certification_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Certification Date'),
        help_text=_('When the construction system was certified'),
    )
    description_de = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Description (de)'),
        help_text=_('German description of the construction system'),
    )
    description_en = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Description (en)'),
        help_text=_('English description of the construction system'),
    )
    total_thickness = models.FloatField(
        blank=True,
        null=True,
        verbose_name=_('Total Thickness'),
        help_text=_('Total thickness of the construction system in m'),
    )
    u_value = models.FloatField(
        blank=True,
        null=True,
        verbose_name=_('U-Value'),
        help_text=_('Thermal transmittance of the construction system in W/(m2K)'),  # noqa
    )

    class Meta:
        ordering = ['name', 'certification_date']
        verbose_name = _('Construction System')
        verbose_name_plural = _('Construction Systems')

    def __str__(self):
        return self.name
