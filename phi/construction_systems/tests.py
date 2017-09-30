# -*- coding: utf-8 -*-
"""
Tests of construction_systems app

These tests just exist as a show-case
"""

from django.test import TestCase

from .models import ConstructionSystem


class ConstructionSystemTestCase(TestCase):
    def setUp(self):
        ConstructionSystem.objects.create(name='TestConstructionSystem0')
        ConstructionSystem.objects.create(
            name='TestConstructionSystem1', component_id='CID')

    def test_component_id(self):
        count = ConstructionSystem.objects.count()
        self.assertEqual(count, 2)
        cs = ConstructionSystem.objects.get(name='TestConstructionSystem0')
        self.assertEqual(cs.component_id, None)
        cs = ConstructionSystem.objects.get(name='TestConstructionSystem1')
        self.assertEqual(cs.component_id, 'CID')
