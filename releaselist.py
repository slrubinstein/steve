"""
This is a script for pulling data out of a large text file consisting of
over one hundred personal releases. The releases were in PDF form, and
the text file has been created using PDFMiner. The new text file will
separate data using a % character so Excel can easily separate the data
into columns.

Steps:
0. Convert release PDFs to one large text tile using PDFMiner.
1. Open text file with all releases.
2. Use regex to findall page 3s, where personal contact info is listed.
3. Iterate through page 3s.
3a. Convert data into individual list items.
3b. Search through items in list and pull out our target data.
3c. Write data to new document, adding % as separation character.
4. Close files.
"""

import re

f = open('releasestext.txt', 'rU')
text = f.read()

#Use regex to findall page 3s, which contains contact info we need.

info = re.findall(r'2\sof\s3\s(.*?)3\sof\s3', text, re.DOTALL)

#Count number of page 3s so we know how many matches we found.

count = text.count('2 of 3')

output = open('output_releases.txt', 'w')

for i in range(0,count):

	#Convert page 3 strings into separate list items.

	words = info[i].split()

	for word in words:

		#Date is consistantly the 5th item in list

		date = str(words[4])

		#Grabs first name, which is the 2nd item after 'First'

		if str(word) == 'FIRST':
			first = words[words.index(word)+2]

		#Grabs last name, which is the 2nd item after 'Last'

		elif str(word) == 'LAST':
			last = words[words.index(word)+2]

		#Grabs address, which is everything after 'Address' and before 'Email'

		elif str(word) == 'ADDRESS:':
			addresslong = words[words.index(word)+1:]
			address = []
			for a in addresslong:
				if str(a) != 'EMAIL:':
					address.append(a)
				else:
					break
			address = ' '.join(address)

		#Grabs email, which is the 1st item after 'Email'

		elif str(word) == 'EMAIL:':
			email = words[words.index(word)+1]
		
		#Grabs phone number, which is first item after 'Number'

		elif str(word) == 'NUMBER:':
			phone = words[words.index(word)+1]
	print 'Writing to document--'
	print 'First Name: ', first
	print 'Last Name: ', last
	print 'Address: ', address
	print 'Email: ', email
	print 'Phone: ', phone
	print 'Date Signed: ', date

	#Write to new file

	output.write(first+'%'+last+'%'+address+'%'+email+'%'+phone+'%'+date+'%'+'\n')

output.close()
f.close()

