from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
import time

class Command(BaseCommand):

    def handle(self, *args, **karags):
        
        db_up = False

        while db_up == False:
            
            try:
                self.check(databases=['default'])
                db_up = True
            except:
                time.sleep(1)
                print("Database reconnecting...")

        print("Database connected successfully...")