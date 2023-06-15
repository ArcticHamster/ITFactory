
# Pachete python. Interacțiune cu fișiere.

"""
Create a text file called “hello.txt” and add the following text inside of it:
Python
Java
Javascript
C/C++/C#
PHP
Node.js
Write a short program to read and display the text file

"""
# import csv

# with open('hello.txt') as f:
#     lines = f.read()
#     print(lines)

"""
Write a short program to append the following lines to “hello.txt” (you will use a list of strings and a for-loop):
Go                                                                                              
Kotlin
Swift
Display the new contents of the file.
Write a short program that reads the “hello.txt” file and displays every other line (only odd lines).
"""
# list = ['Go', 'Kotlin', 'Swift']
# with open('hello.txt','a') as f:
#     f.write('\n')
#     for i in list:
#         f.write(i+'\n')
#
# with open('hello.txt') as f:
#     lines = f.read()
#     print(lines)


"""
Write a short program that reads the “hello.txt” file and displays every other line (only odd lines).
"""

# with open('hello.txt', 'r') as f:
#
#     lines = f.readlines()
#     for i in range(0, len(lines), 2):
#         print(lines[i])

"""
Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. Each file will contain the sentences below:
My name is letter X.
I am the 24th letter of the alphabet.
Make sure you use the correct ending for the letter’s number (e.g. 1st, 2nd, 3rd, etc.)
"""
# alphabet = []
# start = ord('A')
#
# for i in range(26):
#     alphabet.append(chr(start + i))
#
# for letter in alphabet:
#     with open(f'FILES/{letter}.txt', 'w') as new_file:
#         new_file.writelines(f'My name is letter {letter}.\n')
#         if letter == 'A':
#             var  = 'st'
#         elif letter == 'B':
#             var = 'nd'
#         elif letter == 'C':
#             var = 'rd'
#         else:
#             var = 'th'
#
#         new_file.write(f'I am the {ord(letter)-ord("A")+1}{var} letter of the alphabet.\n')

"""
Create a csv file called “students.csv” and add the following text inside of it:
id,fname,lname,age,grade
1,Maria,Popescu,31,7.5
2,Andrei,Ionescu,26,8.0
3,Adriana,Marinescu,21,7.5
4,Matei,Gheorghescu,42,8.5
5,Eusebiu,Pop,33,9.5
6,Ioana,Popa,29,9.0
"""

# import csv
#
#
#
# with open('FILES/students.csv', 'w', newline='') as csv_file:
#     create_file = csv.writer(csv_file)
#     create_file.writerow(['id', 'fname', 'lname', 'age', 'grade'])
#     create_file.writerow(['1','Maria','Popescu','31','7.5'])
#     create_file.writerow(['2','Andrei','Ionescu','26','8.0'])
#     create_file.writerow(['3','Adriana','Marinescu','21','7.5'])
#
# with open('FILES/students.csv', 'r') as csv_file:
#     read_file = csv.reader(csv_file)
#     header = next(read_file)
#     print(f'{header[0]:3} {header[1]:13} {header[2]:16} {header[3]:5} {header[4]:5}')
#     print('_'*55)
#     for row in read_file:
#         print(f'{row[0]:3} {row[1]:13} {row[2]:16} {row[3]:5} {row[4]:5}')


"""
Read again the information from the csv file above, store it all in a list of data, and then write a new file, called “students.json”, which will contain a valid JSON object. 
Use the following format for each student (and use Python’s standard JSON module):
[
	{
		"id": 1,
		"fname": "Maria",
		"lname": "Popescu",
		"age": 31,
		"grade": 7.5	
	},
	...
]
"""
import json
import csv

data = []
with open('FILES/students.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        data.append(row)
print(data)
with open('FILES/students.json', 'w') as csv_file:
    json.dump(data, csv_file, indent=4)
print(f'Data has been written to "{csv_file}" in JSON format')