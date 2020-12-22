#!/usr/bin/env python
# coding: utf-8

file = input('Enter a class file to grade (i.e. class1 for class1.txt): ')

def goifile(file):
    try :
        data = open(file + '.txt',"r")
        a= data.read()
        print(type(a))        
    except :
        print("File cannot be found.")
    else:
        print("Successfully opened",file)
        print("**** ANALYZING ****")
        file1=a.split('\n')        
        
        count=0
        for line in file1:
            if checkID(line) == 0:
                print("Invalid line of data: N# is invalid",line)
            elif check1(line) == 0:
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
        
        
#task2   
def check1(line):
    linex = line.split(',')
    #print(linex)
    if len(linex)!=26:
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
    #print(linex)
    id = linex[0]
    soID = id[1:]
    
    if id[0:1] != "N" or len(id) != 9 or checkINT(soID) == False:
        return 0
    else:
        return 1
          
#task3
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
        if checkID(line)==1 and check1(line)==1:
            store_score.append(score(line))
    print(store_score)
    print("Mean (average) score:",sum(store_score)/len(store_score))
    print("Highest score:",max(store_score))
    print("Lowest score:", min(store_score))
    print("Range of scores:",max(store_score) - min(store_score) )
 
    score_sort = sorted(store_score)
    if len(store_score)%2==0:
        i = int(len(store_score)/2)
        median = (score_sort[i-1] + score_sort[i])/2
        print("Median score:",median)
    else:
        k = int(len(store_score)/2)
        print("Median score:",score_sort[k])
    

#task4
def task4(file1, file):
    f= open(file + "_grades.txt",'w')
    for line in file1:
        linex = line.split(',')
        if checkID(line)==1 and check1(line)==1:
            a = linex[0]
            f.write(a + ','+str(score(line)) + '\n')
    f.close()

goifile(file)