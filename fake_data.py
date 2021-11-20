from faker import Faker
import random
import csv
fake = Faker()
from faker.providers import DynamicProvider


Skills_provider = DynamicProvider(
     provider_name="freelancer",
     elements=["Java", "javascript", "SQL", "Python", "CSS", "Machinelearning", "angular", "logo design", "data entry", "Accounting"
     "Marketing","jenkins", "Dockers"],
)

my_word_list = [
'good','excellent','I',
'am','skills','worked',
'for','many','years',
'looking','forward','to','work', 'with', 'you']

fake.add_provider(Skills_provider)

#City_provider = DynamicProvider(
#    provider_name="freelancer_city",
#    elements=["Denton","Austin","Tampa","Irving","New York"],
#)

fake.add_provider(City_provider)

skill = []
free = []
email_id = []
desc = []
#city = []
example = ['example','google','yahoo','gmail','hotmail']
domain= ['.com','.net','.edu']

example_random = random.choice(example)
domain_random = random.choice(domain)

for i in range(0,15):
	free.append(fake.name())
	skill.append(fake.freelancer())
	desc.append(fake.sentence(ext_word_list=my_word_list))
#	city.append(fake.freelancer_city())
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
print(skill)
print(desc)


file = open(r"C:\Users\admin\Desktop\srishtit\srishtit_seller.csv","a",newline='')

writer = csv.writer(file)

header = ['first_name', 'second_name', 'email_id','skills', 'desc']

#writer.writerow(header)

for w in range(0,15):

	writer.writerow([first_name[w], second_name[w], email_id[w], skill[w], desc[w]])

file.close()