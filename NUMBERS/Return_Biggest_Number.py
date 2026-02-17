'''QUESTION: Write a python program, where the input is a list of numbers and output is the biggest number among them
EXAMPLE:
INPUT: 11 12 13 14 15
OUTPUT: 15
'''

#PROGRAM
a=list(map(int,input().split()))
b=max(a)
print(b)
