from faker import Faker
import random
import csv
fake = Faker()
from faker.providers import DynamicProvider
import calendar

date1 = []
month = []
year = []
quater1 =[]
dow = []
for i in range(0,3):
	M = fake.date_between(start_date = 'today', end_date = '+30d')
	date1.append(print(M))
	month.append(M.month)
	year.append(M.year)

print(date1)
print(month)
	

