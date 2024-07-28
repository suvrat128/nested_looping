# given no is palandrome or not

n = int(input())
dummy = n
rev = 0

while dummy>0:
    rem = dummy%10
    dummy//=10
    rev = rev*10+rem
if rev == n:
    print('no is palndrome')
else:
    print(' not palndrome')


# print all plandrome no in given range

ll = int(input())
ul = int(input())

for n in range(ll,ul+1):
    dummy = n
    rev = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        rev = rev*10+rem
    if rev == n:
        print(n)
        