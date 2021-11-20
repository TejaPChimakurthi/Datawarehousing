from faker import Faker
import random
import csv
fake = Faker()
from faker.providers import DynamicProvider

#status_provider = DynamicProvider(
 #    provider_name="status1",
  #   elements=["Completed","active","in-process"],
#)

#fake.add_provider(status_provider)

caterory_provider = DynamicProvider(
     provider_name="caterory",
     elements=["Computer & IT","Accounting & Finance","Project Management","Customer Service","Healthcare",
     "Education & Training","HR & Recruiting","Graphic Design","Data Entry"],
)

fake.add_provider(caterory_provider)

my_word_list = ["I","need","a","mathematical","proof","without","plagiarism","for","submitting","an","assignment","Looking","for","a","Data","Scraper","Looking","for","a","good","writer","for","a","regular","freelance","remote","workProject","is","about","creating","content","from","existing","available","information"]


Skills_provider_it = DynamicProvider(
     provider_name="freelancer_it",
     elements=["Java", "javascript", "SQL", "Python", "CSS", "Machinelearning", "angular"],
)
"logo design", "data entry", "Accounting", "Marketing", "jenkins", "Dockers"
fake.add_provider(Skills_provider_it)

Skills_provider_accounting = DynamicProvider(
     provider_name="freelancer_accounting",
     elements=["Accounting", "word","Finance","documentation"]
)
fake.add_provider(Skills_provider_accounting)

Skills_provider_mangement = DynamicProvider(
     provider_name="freelancer_mangement",
     elements=["manager", "word","powerpoint","payscale Management"]
)
fake.add_provider(Skills_provider_mangement)

Skills_provider_service = DynamicProvider(
     provider_name="freelancer_service",
     elements=["debugging the code","powerpoint","front desk"]
)

fake.add_provider(Skills_provider_service)

Skills_provider_Healthcare = DynamicProvider(
     provider_name="freelancer_healthcare",
     elements=["machine learning", "nlp","Finance"]
)

fake.add_provider(Skills_provider_Healthcare)

Skills_provider_Education = DynamicProvider(
     provider_name="freelancer_Education",
     elements=["Teaching", "advisor"]
)

fake.add_provider(Skills_provider_Education)

Skills_provider_Recruiting = DynamicProvider(
     provider_name="freelancer_Recruiting",
     elements=["HR"]
)

fake.add_provider(Skills_provider_Recruiting)

Skills_provider_design = DynamicProvider(
     provider_name="freelancer_design",
     elements=["UX/UI", "logo design"]
)

fake.add_provider(Skills_provider_design)

Skills_provider_dataentry = DynamicProvider(
     provider_name="freelancer_dataentry",
     elements=["excel", "word", "PDF"]
)

fake.add_provider(Skills_provider_dataentry)


Title = []
project_desc = []
status = []
caterory1 = []
Skills = []

#example = ['example','google','yahoo','gmail','hotmail']
#domain= ['.com','.net','.edu']

#example_random = random.choice(example)
#domain_random = random.choice(domain)

for i in range(0,50):
	Title.append(fake.sentence(ext_word_list=my_word_list, nb_words= 4))
	project_desc.append(fake.sentence(ext_word_list=my_word_list, nb_words= 12))
	
	L = fake.caterory()
	caterory1.append(L)
	if L == "Computer & IT":
		Skills.append(fake.freelancer_it())
	elif L == "Accounting & Finance":
		Skills.append(fake.freelancer_accounting())
	elif L == "Project Management":
		Skills.append(fake.freelancer_mangement())
	elif L == "Customer Service":
		Skills.append(fake.freelancer_service())
	elif L == "Healthcare":
		Skills.append(fake.freelancer_healthcare())
	elif L == "Education & Training":
		Skills.append(fake.freelancer_Education())
	elif L == "HR & Recruiting":
		Skills.append(fake.freelancer_Recruiting())
	elif L == "Graphic Design":
		Skills.append(fake.freelancer_design())
	elif L == "Data Entry":
		Skills.append(fake.freelancer_dataentry())
	

#first_name = []
#second_name = []

#for i in free:
#	first_name.append(i.split(" ")[0])
#	second_name.append(i.split(" ")[1])
#	email_id.append(i.replace(" ","") + "@" + example_random + domain_random)

print(Title)
print(project_desc)
print(caterory1)
print(Skills)

file = open(r"C:\Users\admin\Desktop\service_data.csv","a",newline='')

writer = csv.writer(file)

header = ['Title', 'project_desc', 'status','caterory', 'Skills']

#writer.writerow(header)

for w in range(0,50):

	writer.writerow([Title[w], project_desc[w], caterory1[w], Skills[w]])

file.close()