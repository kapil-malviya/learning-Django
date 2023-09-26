import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRUDfbv.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *

faker = Faker()

def populate(n):
	for i in range(n):
		feno = randint(101, 999)
		fename = faker.name()
		fesal = randint(50000, 90000)
		fecity = faker.city()
		emp_record = Employee.objects.get_or_create(eno=feno, ename=fename, esal=fesal, ecity=fecity)

populate(18)