# Name = Sovit Bhandari
# U-number= U83561265
# Brief discription = The following code makes dictionary for set of list and then the dictionary is used to get the required number for required ouptput.
course = input('Enter a course number:').upper()

#Creating dictionary for Course Name
Course_Name = {'COP 2510': 'Programming Concepts',
               'EGN 3000L':'Foundations of Engineering Lab',
               'MAC 2281': 'Calculus I',
               'MUH 3016': 'Survey of Jazz',
               'PHY 2048': 'General Physics I'}

#Creating dictionary for Instrutor name
Instructur_Name = {'COP 2510': 'S.Small',
               'EGN 3000L':'J. Anderson',
               'MAC 2281': 'A. Makaryus',
               'MUH 3016': 'A. Wilkins',
               'PHY 2048': 'G. Pradhan'}

#Creating dictionary for Course Time
Course_Time = {'COP 2510': 'TR 8:00am - 9:15am',
               'EGN 3000L':'TR 11:00am - 12:15pm',
               'MAC 2281': 'MW 9:30am - 10:45am',
               'MUH 3016': 'online asynchronous',
               'PHY 2048': 'TR 5:00pm - 6:15pm'}
#Using conditon to print the desired output while accessing the dictionary
if course in Course_Name:
    print(f'The course details are:\nCourse Name: {Course_Name[course]}\nInstructor: {Instructur_Name[course]}\nClass Times:{Course_Time[course]}')
#if the input is not expected
else:
    print(f'{course} is an invalid course number.')





















'''course = input('Enter a course number:').upper()
COP = {'Course Name': 'Programming Concepts,', 
'Instructor': 'S. Small', 
'Class Times': 'TR 8:00am - 9:15am'  } 
EGN ={'Course Name': 'Foundations of Engineering Lab', 'Instructor': 'J.Anderson', 'Class Time': 'TR 11:00am - 12:15pm'}
MAC ={'Course Name': 'Calculus I', 'Instructor': 'A.Makaryus', 'Class Times': 'MW 9:30am - 10:45am'}
MUH ={'Course Name': 'Survey of Jazz', 'Instructor':'A.Wilkins', 'Class Times':'online asynchronous'}
PHY ={'Course Name':'General Physics I', 'Instructor':'G.Pradhan', 'Class Times':'TR 5:00pm - 6:15pm'}
if course == 'COP 2510':
    print(f'The course details are:\n Course Name:{COP["Course Name"]}\n Instructor: {COP["Instructor"]}\n Class Times: {COP["Class Times"]}')
elif course == 'EGN 3000L':
    print(f'The course details are:\n Course Name: {EGN["Course Name"]}\n Instructor: {EGN["Instructor"]}\n Clas Times: {EGN["Class Times"]}')
elif course == 'MAC 2281':
    print(f'The course details are:\n Course Name: {MAC["Course Name"]}\n Instructor: {MAC["Instructor"]}\n CLass Times: {MAC["Class Times"]}')
elif course == 'MUH 3016':
    print(f'The course details are:\n Course Name: {MUH["Course Name"]}\n Instructor: {MUH["Instructor"]}\n CLass Times: {MUH["Class Times"]}')
elif course == 'PHY 2048':
    print(f'The course details are:\n Course Name: {PHY["Course Name"]}\n Instructor: {PHY["Instructor"]}\n CLass Times: {PHY["Class Times"]}')
'''