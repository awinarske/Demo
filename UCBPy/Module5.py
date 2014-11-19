# Assignment for Amy Winarske, Module 5
#Coding assignments can be saved as .py files when appropriate or .txt files otherwise, for example,
#you may want to past the code from multiple .py files into a single .txt file.
#When you've completed the assignment, attach the file(s) to the drop box for this module, which you'll find near the end of the module. Please be sure to include your last name and the course number in the file name of the document, like so: "your name X442.3 Assignment 5."

#1.Using the keys method for dictionaries and the sort method for lists,
#write a for loop that prints the keys and corresponding values of a dictionary in the alphabetical order of the keys. 
mydico={'Winarske':'Amy', 'Brignetti':'Chris', 'Bradley':'Steve', 'Hanna':'Julia', 'Simmons':'Amanda', 'Caruthers':'Bruce'}

for key in sorted(mydico.keys()):
    print(key, mydico[key])
    
#2.As an alternative to the range function, some programmers like to increment a counter inside a while loop and
#stop the while loop when the counter is no longer less than the length of the array.
#Rewrite the following code using a while loop instead of a for loop. 
a = [7,12,9,14,15,18,12] 
b = [9,14,8,3,15,17,15] 
big = [] 
#for i in range(len(a)): 
#    big.append(max(a[i],b[i])) 

i=0
while True:
    if i < len(a):
        big.append(max(a[i],b[i]))
        print(big)
        i = i+1
        print(i)
    else:
        break
else:
    print('We are done')

#3.Write a loop that reads each line of a file and counts the number of lines that are read
#until the total length of the lines is 1,000 or more characters.
#Use a break statement to make sure that you don't continue reading the file once at least 1,000 characters are read. 

# I am assuming you really meant this counts the number of characters read and not the number of lines

fileobject=open("myfile.txt",'r')
linecount=0
totalchar=0
while True:
    line=fileobject.readline()
    print(line)
    if line == "":
        print(totalchar)
        break
    elif totalchar > 1000 :
        print(totalchar)
        break
    else:
        totalchar=totalchar+len(line)

fileobject.close()


#4.Modify the program written in question 3 so that it doesn't count characters on any line that begins with a pound sign (#).

fileobject=open("myfile.txt",'r')
linecount=0
totalchar=0
while True:
    line=fileobject.readline()
    print(line)
    if line == "":
        print(totalchar)
        break
    elif totalchar > 1000 :
        print(totalchar)
        break 
    elif line[0] == '#' :
        continue
    else:
        totalchar=totalchar+len(line)

fileobject.close()
