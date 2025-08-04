#Run this prior to starting the exercise
from random import randint as rnd
import pandas as pd

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


'''
The two arguments for this function are the files:
  - currentMem: File containing list of current members
  - exMem: File containing list of old members
    
This function should remove all rows from currentMem containing 'no' 
in the 'Active' column and appends them to exMem.
'''
def cleanFiles(currentMem, exMem):
    # TODO: Open the currentMem file as in r+ mode
    with open(currentMem, 'r+') as writeFile:
        #TODO: Open the exMem file in a+ mode
        with open(exMem, 'a+') as appendFile:
        #TODO: Read each member in the currentMem (1 member per row) file into a list.
        # Hint: Recall that the first line in the file is the header.
            # Get the data
            writeFile.seek(0)
            members = writeFile.readlines()

            # remove header
            header = members[0]
            members.pop(0)         

            # TODO: iterate through the members and create a new list of the innactive members
            inactive = []
            for member in members:
                if 'no' in member:
                    inactive.append(member)
            # Go to the beginning of the currentMem file
            writeFile.seek(0)
            writeFile.write(header)
            # TODO: Iterate through the members list. 
            for member in members:
                # If a member is inactive, add them to exMem, otherwise write them into currentMem
                if member in inactive:
                    appendFile.write(member)
                else:
                    writeFile.write(member)
            writeFile.truncate()                   
    
    pass # Remove this line when done implementation

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'


# The code below is to help you view the files.
# Do not modify this code for this exercise.
testWrite = './Module_4/members.txt'
testAppend = './Module_4/inactive.txt'
fee =('yes','no')
passed = True
genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogWrite = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')

with open(testWrite,'r') as file:
    clWrite = file.readlines()

with open(testAppend,'r') as file:
    clAppend = file.readlines()
        
# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False
    
for line in clWrite:
    if  'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print ("{}".format(testMsg(passed)))
    

df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
print(df['a']==1) 