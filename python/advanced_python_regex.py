import re
import csv

filename = 'faculty.csv'
#filename = '/Users/eastblue/ds/metis/metisgh/prework/dsp/python/faculty.csv'

''' Q1. Find how many different degrees there are, and their frequencies:
Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.'''

def find_degrees():
    with open(filename) as file:
        BioStatsFac = csv.reader(file, delimiter=',')
        header = next(BioStatsFac)
        degrees = []
        for row in BioStatsFac:
            degree = row[1].strip()
            match = re.search('\.', degree)
            if match:
                 degrees.append(degree.replace(match.group(), ""))
            else:
                degrees.append(degree)
        results = []
        for degree in degrees:
            if re.findall('[A-Z]', degree):
                results.extend(degree.split())
        degree_dict = {}
        for d in results:
            degree_dict[d] = degree_dict.get(d, 0) + 1
        print ("Types of degrees:".format(len(sorted(degree_dict.keys()))))
        print ("Frequencies:")
        for k, v in sorted(degree_dict.items(), key=lambda v: v[1], reverse=True):
            print (k,'=', v)

find_degrees()

''' Q2. Find how many different titles there are, and their frequencies:
Ex:  Assistant Professor, Professor'''

with open(filename) as file:
    next(file, None)
    BioStatsFac = csv.reader(file, delimiter=',')
    counts = dict()
    for row in BioStatsFac:
        output = row[2]
        if len(output) > 1:
            line = str(output)
            line = line.strip()
            i = re.split("(Professor)+", line)
            del i[-1]
            j = ' '.join(i)
            if j not in counts: 
                counts[j] = 1
            else:
                counts[j] += 1

print(counts)


''' Q3. Search for email addresses and put them in a list.
Print the list of email addresses.'''

with open(filename) as file:
    next(file, None)
    BioStatsFac = csv.reader(file, delimiter=',')
    emails = list()
    for row in BioStatsFac:
        output = row[3]
        if len(output) > 1:
            i = str(output)
            emails.append(i)

for i in emails:
    print(i)
    
''' Q4. Find how many different email domains there are:
(Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).
Print the list of unique email domains.'''

with open(filename) as file:
    next(file, None)
    BioStatsFac = csv.reader(file, delimiter=',')
    domains = dict()
    for row in BioStatsFac:
        output = row[3]
        if len(output) > 1:
            line = str(output)
            line = line.strip()
            i = re.split("(@)+", line)
            j = i[-1]
            if j not in domains: 
                domains[j] = 1
            else:
                domains[j] += 1

print(domains)