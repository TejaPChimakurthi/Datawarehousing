from faker import Faker
import random
import csv
fake = Faker()
from faker.providers import DynamicProvider




#fake.add_provider(Skills_provider)


free = []
email_id = []
password = []

example = ['example','google','yahoo','gmail','hotmail']
domain= ['.com','.net','.edu']

example_random = random.choice(example)
domain_random = random.choice(domain)

for i in range(0,10):
	free.append(fake.name())
	password.append(fake.sentence(nb_words = 4))

first_name = []
second_name = []

for i in free:
	first_name.append(i.split(" ")[0])
	second_name.append(i.split(" ")[1])
	email_id.append(i.replace(" ","") + "@" + example_random + domain_random)

print(free)
print(first_name)
print(second_name)
print(email_id)
print(password)



file = open(r"C:\Users\admin\Desktop\client_data.csv","a",newline='')

writer = csv.writer(file)

header = ['first_name', 'second_name', 'email_id','password']

#writer.writerow(header)

for w in range(0,10):

	writer.writerow([first_name[w], second_name[w], email_id[w],password[w]])

file.close()