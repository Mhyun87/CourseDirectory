print("course directory")
print()

# add some course numbers and course descriptions to the course directory
print("Add some course numbers and course descriptions to the course directory")
print()

# use a while loop to prompt the user for course numbers and descriptions
# store them in the course directory
num = []
desc = []
while True:
    courseNumber = input("Enter a course number (e.g., COSC 1315) or a blank string when finished: ")
    # if courseNumber empty
    # store the course in a courseDirectory
    if courseNumber == "":
        break
    else:
        # appending courseNumber in num
        num.append(courseNumber)
        # asking for courseDescription
        courseDescription = input("Enter the course description: ")        
        desc.append(courseDescription)

# converting num and desc to dictonary
courseDirectory = dict(zip(num, desc))

print ("\n Course Directory:")
# print the course directory
print(courseDirectory)
print()

print()
print("search for a specific course number in the course directory")
# search for a specific course number in the course directory
# use a while loop to allow multiple course description lookups
# enter a course number and look up the course description
print()
courseNumber = input("Enter a course number or a blank string when finished: ")

while courseNumber != "":
    # check to see if the course is in the course directory
    if courseNumber in courseDirectory:
        # while courseNumber !="":
        print("Course found")
        
        # print the course description
        print ("The description for that course is: ", courseDirectory[courseNumber])
        
    else:
        print("Course not found")
    
    print()
    courseNumber = input("Enter a course number or a blank string when finished: ")
    
# hold window open to allow user to view output
print()
input("Press ENTER to continue ")
