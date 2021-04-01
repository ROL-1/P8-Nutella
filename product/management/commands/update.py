#! /usr/bin/env python3
# coding: utf-8
"""Custom command to update database from api datas."""

from django.core.management.base import BaseCommand

from product.offapi.apirequests import ApiRequests
from product.offapi.insertdb import deletedata, insertdb
from product.offapi.charmax import Charmax


class Command(BaseCommand):
    """Custom command to clear and fill database from api datas."""

    def databasefill(self):
        """Command to clear and fill database from api datas."""
        # Retrieves the maximum number of characters for the fields.
        Fields_charmax = Charmax.characters_max()
        # Retrives datas from Api and reject unsuitable datas.
        Api_data = ApiRequests().api_get_data(Fields_charmax)
        # Insertion in database.
        Insert = insertdb(Api_data)
        print("Database installed.")

    def handle(self, *args, **options):
        """Call customs commands."""
        self.databasefill()
        return
