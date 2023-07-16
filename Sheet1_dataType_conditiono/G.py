# --------- Summation from 1 to N --
""" 
Given a number N
. Print the summation of the numbers that is between 1 and N
 (inclusive).

.∑i=1Ni
Input
Only one line containing a number N
 (1≤N≤109)
Output
Print the summation of the numbers that are between 1 and N
 (inclusive).

"""
N = int(input())
sum = 0
for i in range(1, N+1):
   sum += i

print(sum)   
