#Control Flow Statements
#Conditional Statements

a=True
if True:                         #Colon in python represents starting of a block
    print("the value is true")   #1 indent= 2 spaces, 4 spaces, 8 spaces
print("end")


a=False
if a:
    print("this value is true")
else:
    print("this value is false")
    
a=5
if a==3:
    print("this value is 3")
elif a==5:
    print("this value is 5")
else:
    print("this value is not 3 or 5")


#What's not cool with this approach???
'''
if x<0:
    sign=-1
if x==0:
    sign=0
if x>0:
    sign=1
'''

"""
It will check every if conditions
"""

'''
x: int (-inf,inf)
G -> x
a = x<0
b = x==0
c = x>0
a n b= b n c = a n c = phi
Conditions are mutually exclusive
Then we go with if elif
we should use else statement if after the conditions someothers are left
a u b u c !=G
'''


'''
#q = Can A access profile B
a= isFriend
b= isBlocked
c= isAdmin
d= isMarkZuckerburg
#Making k map (Truth Table)
a b c d q
0 0 0 0 0
0 0 0 1 1
0 0 1 0 1
0 0 1 1 1
0 1 0 0 0
0 1 0 1 1
0 1 1 0 0
0 1 1 1 1
1 0 0 0 1
1 0 0 1 1
1 0 1 0 1
1 0 1 1 1
1 1 0 0 0
1 1 0 1 1
1 1 1 0 0
1 1 1 1 1
if (condition):
    print("has access")
else:
    print("access denied")
'''