#break outer loop with outer loop value

i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        j+=1
    if i==3:
        break
    i+=1

#ex2:
i=1
while i<6:
    j=1
    if i==3:
        break
    while j<6:
        print(i,j)
        j+=1
    i+=1
#process for ex2:
'''
iteration 1:
    outer loop i = 1:
        checking i == 3: false
        so we go to inner loop 
            where j = 1:
            so print 1,1
            increment j from 1 to 2
            so print 1,2
            j increment from 2 to 3
            so print 1,3
            j increment from 3 to 4
            so print 1,4
            j incremnet from 4 to 5
            so print 1,5
            j increment from 5 to 6
        at last increment i from 1 to 2
iteration 2:
    outer loop i =2:
        checking i == 3: false
        so we go to inner loop
            where again inner loop run for 5 time 
                so print 2,1 2,2 2,3 2,4 2,5
        at last increment i from 2 to 3
iteration 3:
    outer loop i =3:
        checking i == 3: true
        so terminate the outer loop so program will end at this point only

        '''