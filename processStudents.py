''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv


# create a file object to open the file in read mode
students = open("students.csv","r")

# create a csv object from the file object
student_file = csv.reader(students, delimiter=",")

#skip the header row
next(student_file)

#create an outfile object for the pocessed record
CSVFILE = "processedStudents.csv"
outfile = open(CSVFILE, "w", newline="")
writer = csv.writer(outfile, delimiter=",")

fieldnames = ["stud_id", "firstname", "lastname", "major", "classification", "gpa"]
writer.writerow(fieldnames)


#create a new dictionary named 'student_dict'
student_dict = {}

#use a loop to iterate through each row of the file
for record in student_file:
    #check if the GPA is below 3.0. If so, write the record to the outfile
    if float(record[8]) < 3.0:
        stud_id = record[0]
        pin = record[1]
        firstname = record[2]
        lastname = record[3]
        city = record[4]
        state = record[5]
        major = record[6]
        classification = record[7]
        gpa = record[8]
        row = [stud_id, firstname, lastname, major, classification, gpa]
        writer.writerow(row)
    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA
    key = record[0]
    student_dict[key] = record[8]
    

#print the entire dictionary
print(student_dict)

#Print the student id 
id = "567890123"
print(id)

#print out the corresponding GPA from the dictionary
if id in student_dict:
    print(student_dict[id])
else:
    print(id, "is not in the dictionary student_dict")

#close the outfile
outfile.close()