# print all the prefect no in given range
'''

outer loop : for -range ----> ll to ul
1. take each and every number in a given range
inner loop : for range -----> 1 to n//2+1
2. find out the sum of divisor and compare it with number

'''

ll = int(input())
ul = int(input())
for n in range(ll,ul+1):
    summ=0
    for i in range(1,n//2+1):
        if n%1 == 0:
            summ+=i
    if summ == n:
        print(n)

# printing first n prefecrt number by using infinite loop

