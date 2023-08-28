import random
import array
SortedArrayPosition=0
ArrayPosition=0
RecordSmallestNum=0
Array= []
SmallestUnsortedNum=0
#Creates an array
Done= 0
for i in range(3):
    #loops 3 times to create array
    rand=random.randint(1,30)
    #generates random number
    Array.append(rand)
    #adds a new element into array
    

    

for i in range(1):
    
    
    #uses the length of the array as how many times the sorting algorhythm is run
    #the length of the arran. n

    #0 first
    RecordSmallestNum=Array[SortedArrayPosition]
    for i in range(len(Array)-SortedArrayPosition):
        if Array[ArrayPosition]<=RecordSmallestNum:
            RecordSmallestNum=Array[ArrayPosition]
            SmallestUnsortedNum=ArrayPosition
            print(Array)
            print(RecordSmallestNum)
            print(SmallestUnsortedNum)

            
        
            

        ArrayPosition+=1
     
        
            
        

    
