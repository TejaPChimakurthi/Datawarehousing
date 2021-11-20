from faker import Faker
import random
import csv
fake = Faker()
from faker.providers import DynamicProvider

free_id = []

for i in range(0,400):
    x = random.randint(1,100)
    free_id.append(x)

print(free_id)

bid_time = []

for i in range(0,400):
    x = random.randint(1,30)
    bid_time.append(x)

print(bid_time)

amount = random.sample(range(1,1000), 400)

print(amount)

desc = []

my_word_list = [
'good','excellent','I',
'am','skills','worked',
'for','many','years',
'looking','forward','to','work', 'with', 'you']

for i in range(0, 400):
	desc.append(fake.sentence(ext_word_list=my_word_list))


file = open(r"C:\Users\admin\Desktop\bidfact_data.csv","a",newline='')

writer = csv.writer(file)

#header = ['first_name', 'second_name', 'email_id','skills', 'desc']

#writer.writerow(header)

for w in range(0,400):

	writer.writerow([free_id[w], bid_time[w], amount[w], desc[w]])

file.close()