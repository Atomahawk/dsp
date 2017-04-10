import csv
import re

filename = 'faculty.csv'
# filename = '/users/eastblue/ds/metis/metisgh/prework/dsp/python/faculty.csv'

# Q6
def fac_dict():
	faculty_dict = {}
	with open(filename, 'r') as file:
		BioStatFac = csv.reader(file, delimiter=',')
		header = next(BioStatFac)
		for row in BioStatFac:
			names = row[0]
			degrees = row[1].strip()
			positions = row[2]
			emails = row[3]

			last = re.findall(r'[A-Z][a-z]*\S$', names)
			for i in last:
				if i not in faculty_dict:
					faculty_dict[i] = [degrees, positions, emails]
				else:
					faculty_dict[i] = [[degrees, positions, emails], faculty_dict[i]]
	return faculty_dict

for k, v in sorted(make_faculty_dict().items())[:3]:
	print (k, v)

print(fac_dict())


# Q7
def prof_dict():
	professor_dict = {}
	with open(filename, 'r') as file:
		BioStatFac = csv.reader(file, delimiter=',')
		header = next(BioStatFac)
		for row in BioStatFac:
			names = row[0]
			degrees = row[1].strip()
			positions = row[2]
			emails = row[3]
			
			last = re.findall(r'[A-Z][a-z]*\S$', names)
			first = re.findall(r'^[A-Z][a-z]*\S*', names)
			full_name = zip(first, last)
			for i in full_name:
				professor_dict[i] = [degrees, positions, emails]
	return professor_dict

for k, v in sorted(prof_dict().items())[:3]:
	print (k, v)

# Q8
for k, v in sorted(prof_dict().items(), key=lambda k: k[0][1])[:3]:
	print (k, v)

print(prof_dict())