# wapt to prijnt prime number in a given range
'''
ll = int(input())
ul = int(input())
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)




# printing first n prime number by using infinite loop
count= int(input('enter hoe many prime numbers u need'))
n =1
pc=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)
            pc+=1
            if pc>=count:
                break
    n+=1




# printing first n prime numb by using normal condition'
count= int(input('enter hoe many prime numbers u need'))
n =1
pc=0
while pc<count:
    if n>1:
        
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)
            pc+=1
    n+=1


# print nth prime nuumbeer

count= int(input('enter hoe many prime numbers u need'))
n =2
pc=0
while True:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        pc+=1
        if pc>=count:
            print(n)
            break

    n+=1
'''

# write a program to print 5th to 10th prime no

n =1
pc=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            pc+=1
            if pc>=5 and pc<=10:
                print(n)
            if pc==10:
                break
    n+=1