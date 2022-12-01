#while Loop

a=1
while a<10:
    print(a)
    a+=1
#When do we use while and for?
'''
If we don,t know how many iteration will it take to end this loop
then we use while loop
E.g: Temple Run
'''


#for Loop
'''
Python for loop works on the concept of sequences
Like a string, array, range, list are sequences
int, float is not sequence
'''

#a=1
#print(a.__iter__)     #__iter__ is a dunder

a="jatin"
print(a.__iter__)

for i in a:
    print(i)
    print(type(i))


a=range(5)
print(a)


for i in range(5):
    print(i)

#for i in 5: ---->Error
    #print(i)


#break, continue and pass

print("aaaaaa"*4)

for i in range(5):
    if i==3:
        continue
    print(i)

for i in range(5):
    print(i)
    if i==3:
        continue

for i in range(5):
    print(i)
    if i==3:
        break

for i in range(5):
    print(i)
    i=100
    print(i)

a=1
print(a)
del a  #Deleted a from memory
#print(a)---> Error

for i in range(5):
    print(i)
    del i

for i in [0,1,2,3,4]:
    print(i) #i=0
    i=100    #i=100
    print(i) #i=100

'''
if True:                       
    #I don't know what to do        #Can't have empty blocks in python, atleast one line should be given
print("rest of the code")
'''

if True:                        
    '''I don't know what to do'''   #This Proves That triple quotes is not a comment
print("rest of the code")

if True:                        
    pass                            #It is an empty statement, use to create empty block in python
print("rest of the code")


for i in range(5):
    print(i)
else:                               #This else binds to the for statement 
    print("something")              #Executes once the for loop ends



for i in range(5):
    if i==3:
        break
    else:
        print(i)
else:                               #If the for loop is ended then the else loop doesn't execute 
    print("something") 
    
