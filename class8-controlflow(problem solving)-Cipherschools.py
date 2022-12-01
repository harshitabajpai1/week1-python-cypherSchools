'''
5 5 5 5 5
5 4 4 4 5
5 4 3 4 5
5 4 4 4 5
5 5 5 5 5
'''

'''
6 6 6 6 6 6 
6 5 5 5 5 6 
6 5 4 4 5 6 
6 5 4 4 5 6 
6 5 5 5 5 6 
6 6 6 6 6 6 
'''

'''
7 7 7 7 7 7 7 
7 6 6 6 6 6 7 
7 6 5 5 5 6 7 
7 6 5 4 5 6 7 
7 6 5 5 5 6 7 
7 6 6 6 6 6 7 
7 7 7 7 7 7 7 
'''
#Cases
'''
n=5
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()
n=5
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()
n=5
for i in range(n):
    for j in range(n):          #It gives distance from bottom most wall 
        print(n-i,end=" ")
    print()
n=5
for i in range(n):
    for j in range(n):          #It gives distance from top most wall
        print(i+1,end=" ")
    print()
n=5
for i in range(n):
    for j in range(n):           #It gives distance from right most wall
        print(n-j,end=" ")
    print()
n=5
for i in range(n):
    for j in range(n):           #It gives distance from left most wall
        print(j+1,end=" ")
    print()
'''
'''
print(max(1,2,3,4,5,6,7))
'''

n=int(input())
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j),end=" ")
    print()

"""
n=int(input())
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1),max(n-i,n-j),end=" ")
    print()
"""

#Overlap the cases and make patterns

'''
0 1 2 3 4 
1 1 2 3 4 
2 2 2 3 4 
3 3 3 3 4 
4 4 4 4 4 
'''

'''
0 1 2 3 4 5 
1 1 2 3 4 5 
2 2 2 3 4 5 
3 3 3 3 4 5 
4 4 4 4 4 5 
5 5 5 5 5 5 
'''

'''
0 1 2 3 4 5 6 
1 1 2 3 4 5 6 
2 2 2 3 4 5 6 
3 3 3 3 4 5 6 
4 4 4 4 4 5 6 
5 5 5 5 5 5 6 
6 6 6 6 6 6 6 
'''

n=int(input())
for i in range(n):
    for j in range(n):
        print(max(i,j),end=" ")
    print()


'''
5 4 4 4 4 
4 3 3 3 3 
3 2 2 2 2 
2 1 1 1 1 
1 0 0 0 0
'''

'''
6 5 5 5 5 5 
5 4 4 4 4 4 
4 3 3 3 3 3 
3 2 2 2 2 2 
2 1 1 1 1 1 
1 0 0 0 0 0 
'''

'''
7 6 6 6 6 6 6 
6 5 5 5 5 5 5 
5 4 4 4 4 4 4 
4 3 3 3 3 3 3 
3 2 2 2 2 2 2 
2 1 1 1 1 1 1 
1 0 0 0 0 0 0 
'''
n=int(input())
for i in range(n):
    for j in range(n):
        print(max(n-j-i,n-i-1),end=" ")
    print()