from faker import Faker
import random
import csv
fake = Faker()
from faker.providers import DynamicProvider

data1 = []

for i in range(0,50):
    x = random.randint(1,100)
    data1.append(x)

print(data1)


data2 = []

for i in range(0,50):
    x = random.randint(1,50)
    data2.append(x)

print(data2)

data3 = []

for i in range(0,50):
    x = random.randint(1,50)
    data3.append(x)

print(data3)

data4 = []

for i in range(0,50):
    x = random.randint(1,29)
    data4.append(x)

print(data4)

data5 = []

for i in range(0,50):
    x = random.randint(1,200)
    data5.append(x)

print(data5)



file = open(r"C:\Users\admin\Desktop\service_fact.csv","a",newline='')

writer = csv.writer(file)

#

#writer.writerow(header)

for w in range(0,50):

	writer.writerow([data1[w], data2[w], data3[w], data4[w],data5[w]])

file.close()
