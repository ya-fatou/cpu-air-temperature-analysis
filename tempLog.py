"""
Program: tempLog.py
Last date modified: 10/01/26
Purpose:
Count the number of records in the templog csv file
Turn the CPU and air temperatures into seperate lists
Find median, mode, mean, minmum and maximum values of the CPU and air temperatures
Script verification using pandas
Input:
tempLog.csv
file name 
Output:
Total number of records in the templog csvfile excluding the header
The median, mode, mean, minimum and maximum values of the CPU and air temperatures
"""
#request the input

filename = input("Enter the file name:")

#output the results

print("The CSV file  name:", filename)

# open the csv file

try:
    f = open("tempLog.csv", "r")

except IOError:
    print("Error: The file could not be opened.")
    exit()

# exclude the header row
f.readline()

# count the number of CPU and air temperatures records
count = 0
nextRecord = True

while nextRecord:
    line = f.readline()
    if line == "":
        nextRecord = False
    else:
        count += 1

# print the number of CPU and air temperatures records
print("Number of CPU and air temperatures records in the dataset:", count)

# Beginning of file (BOF)
f.seek(0)

# exclude the header row
f.readline()

# turn the CPU and air temperatures into list 

air = []
CPU = []

for line in f:
    numbers = line.split(",")
    air.append(float(numbers[1])) 
    CPU.append(float(numbers[2]))


#sort the list and print the CPU midpoint (median)

CPU.sort()
midpoint = len(CPU) // 2
print("The CPU median:", end = " ")
if len(CPU) % 2 == 1:
    print(CPU[midpoint])
else:
    print((CPU[midpoint] + CPU[midpoint-1]) / 2)


    
#sort the list and print the air temperature midpoint (median)

air.sort()
midpoint = len(air) // 2
print("The Air temperature median:", end = " ")
if len(air) % 2 == 1:
    print(air[midpoint])
else:
    print((air[midpoint] + air[midpoint-1]) / 2)

    
# The CPU mode

theDictionary = {}
for number in CPU:
    temperature = theDictionary.get(number,None)
    if temperature == None:
        theDictionary[number] = 1 # the number entered for the first time
    else:
        theDictionary[number] = temperature + 1
        
#find the mode by obataining the maximum value
#in the dictionary and dertmining its key

theMaximum = max(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print(" The CPU mode:", key)
        break


# The air temperature mode

theDictionary = {}
for number in air:
    temperature = theDictionary.get(number,None)
    if temperature == None:
        theDictionary[number] = 1 # the number entered for the first time
    else:
        theDictionary[number] = temperature + 1
        
#find the mode by obataining the maximum value
#in the dictionary and dertmining its key

theMaximum = max(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print(" The Air temperature mode:", key)
        break


# Find the CPU and air temperature mean

def mean(lyst):
    theSum = 0
    for number in lyst:
        theSum += number
    return theSum / len(lyst)

# print the CPU and air temperature mean 

print (" The CPU mean:", mean(CPU))

print (" The Air temperature mean:", mean(air))



# Find the CPU and air temperature minimum 

def ourMIN(lyst):
    
    minpos = 0  # Returns the position of the minimum item.
    current = 1
    while current < len(lyst):
        if lyst[current] < lyst[minpos]:
            minpos = current
        current += 1
    return minpos

# Print the CPU and air temperature minimum 

print (" The Air temperature minimum:", min(air))

print (" The CPU minimum:", min(CPU))



# Find the CPU and air temperature maximum


def ourMAX(lyst):
    
    maxpos = 0 # Returns the position of the minimum item.
    current = 1
    while current < len(lyst):
        if lyst[current] > lyst[maxpos]:
            maxpos = current
        current += 1
    return maxpos

    
# Print the CPU and air temperature maximum 

print (" The Air temperature maximum:", max(air))

print (" The CPU maximum:", max(CPU))


# close the file
f.close()


# Script verification results using pandas

import pandas

df=pandas.read_csv('tempLog.csv')

print("Script verification results using pandas")

print("Air median:", df['Air'].median())
print("CPU median:", df['CPU'].median())
print("Air mode:", df['Air'].mode()[0])
print("CPU mode:", df['CPU'].mode()[0])
print("Air mean:", df['Air'].mean())
print("CPU mean:", df['CPU'].mean())
print("Air minimum:", df['Air'].min())
print("CPU minimum:", df['CPU'].min())
print("Air maximum:", df['Air'].max())
print("CPU maximum:", df['CPU'].max())


