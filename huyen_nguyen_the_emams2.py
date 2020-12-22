#!/usr/bin/env python
# coding: utf-8
import numpy as np 
import pandas as pd
file = input('Enter a class file to grade (i.e. class1 for class1.txt): ')
#tas1
def goifile(file):
    try :
        data = open(file + '.txt',"r")
        a= data.read()
        file1=a.split('\n')
                
    except :
        print("Filem cannot be found.")
    else:
        print("Successfully opened",file)
        print("**** ANALYZING ****")
        file1=a.split('\n')        
        
        count=0
        for line in file1:
            if checkID(line) == 0:
                print("Invalid line of data: N# is invalid",line)
            elif checkRow(line) == 0:
                print("Invalid line of data: does not contain exactly 26 values:",line)
            else:
                count = count+1
        if count == len(file1):
            print("No errors found!")
        print("**** REPORT ****")
        print("Total valid lines of data:",count)
        print("Total invalid lines of data:", len(file1)-count)
        
        task3(file1)
        task4(file1, file)

#Task2=====================================================================   
def checkRow(line):
    linen = np.array(line.split(','))
    if linen.size != 26:
        return 0
    else:
        return 1
        
def checkINT(i):
    try:
         return isinstance(int(i), int)
    except:
        return False
    
def checkID(line):
    linex = line.split(',')
    line_arr = np.array(linex)
    soID = line_arr[0]
    if soID[0] != "N" or len(soID) != 9 or checkINT(soID[1:]) == False:
        return 0
    else:
        return 1 
#task3================================================================================      
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
def score(line):
    linex = line.split(',')
    ans = answer_key.split(',')
    dapso = linex[1:]
    diem =0
    for i in range(len(dapso)):
         #print(i, dapso[i], ans[i])
         if dapso[i] == ans[i]:
             diem = diem + 4
         elif dapso[i] =='':
             diem=diem
         else:
             diem = diem -1
    return diem
           
def task3(file1):
    store_score =[]
    for line in file1:
        if checkID(line)==1 and checkRow(line)==1:
            store_score.append(score(line))
    print(store_score)
    print("Mean (average) score:",np.mean(store_score))
    print("Highest score:",np.max(store_score))
    print("Lowest score:", np.min(store_score))
    print("Range of scores:",np.max(store_score) - np.min(store_score) )
    print("Median score:", np.median(store_score))

#task4=======================================================================================
def task4(file1,file):
    idx =[]
    diem =[]
    for line in file1:
         linex = line.split(',')
         if checkID(line)==1 and checkRow(line)==1:
             idx.append(linex[0])
             diem.append(score(line))
    
    c = {'Id': idx, 'Score': diem}
    df = pd.DataFrame(c)
    df.to_csv (file+'_grades.csv', index = None, header=True) 
    
goifile(file)