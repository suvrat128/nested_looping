# print all the prefect no in given range
'''

outer loop : for -range ----> ll to ul
1. take each and every number in a given range
inner loop : for range -----> 1 to n//2+1
2. find out the sum of divisor and compare it with number



ll = int(input())
ul = int(input())
for n in range(ll,ul+1):
    summ=0
    for i in range(1,n//2+1):
        if n%i == 0:
            summ+=i
    if summ == n:
        print(n)
'''
# printing first n prefecrt number by using infinite loop
'''
count= int(input('enter how many prefect number u want:'))
n=1
c=0

while True:
    summ = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            summ+=i
    if summ == n:
        print(n)
        c+=1
        if count == c:
            break
    n+=1
'''
# print nth prefect no
'''
count= int(input('enter how many prefect number u want:'))
n=1
c=0

while True:
    summ = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            summ+=i
    if summ == n:
        
        c+=1
        if count == c:
            print(n)
            break
    n+=1
'''
#print the 5th and 10th prefect no

n=1
c=0

while True:
    summ = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            summ+=i
    if summ == n:
        c+=1
        if c>=1 and c<=3:
            print(n)
        if c==10:
            break
    n+=1
