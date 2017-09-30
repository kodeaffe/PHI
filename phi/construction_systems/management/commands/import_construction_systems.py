# -*- coding: utf-8 -*-
"""
Command to import construction systems
"""

import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from construction_systems.models import (
    ConstructionSystemCategory, ConstructionSystem)


class Command(BaseCommand):
    help = 'Imports construction systems from a CSV file, encoded in UTF-8. Reruns will update the system.'  # noqa

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            nargs='+',
            type=str,
            help='Name of the CSV file to import',
        )

    def get_name(self, row):
        return row[0]

    def get_component_id(self, row):
        return row[1]

    def get_category(self, row):
        category, _ = ConstructionSystemCategory.objects.get_or_create(
            name=row[2])
        return category

    def get_certification_date(self, row):
        return datetime.strptime(row[3], "%d.%m.%y").date()

    def get_description_de(self, row):
        return row[4]

    def get_description_en(self, row):
        return row[5]

    def str2float(self, value):
        if not value:
            return 0.
        else:
            return float(value.replace(',', '.'))

    def get_total_thickness(self, row):
        return self.str2float(row[6])

    def get_u_value(self, row):
        return self.str2float(row[7])

    def import_row(self, row):
        try:
            system, created = ConstructionSystem.objects.update_or_create(
                name=self.get_name(row),
                component_id=self.get_component_id(row),
                category=self.get_category(row),
                certification_date=self.get_certification_date(row),
                description_de=self.get_description_de(row),
                description_en=self.get_description_en(row),
                total_thickness=self.get_total_thickness(row),
                u_value=self.get_u_value(row),
            )
            if created:
                msg = '{}: created successfully!'.format(system)
            else:
                msg = '{}: updated successfully!'.format(system)
            msg = self.style.SUCCESS(msg)
        except ValueError as err:
            msg = '{}: {}'.format(row[0], err)
            msg = self.style.ERROR(msg)
        self.stdout.write(msg)

    def handle(self, *args, **options):
        with open(options['filename'][0], encoding='utf-8') as fh:
            reader = csv.reader(fh)
            next(reader)  # skip header
            for row in reader:
                self.import_row(row)
