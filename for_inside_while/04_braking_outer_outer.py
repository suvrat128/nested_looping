# breaking of outer loop with outer value
'''
i=1
while i<6:
    for j in range(1,6):
        print(i,j)
    if i == 3:
        break
    i+=1
'''
#ex2:
i=1
while i<6:
    if i == 3:
        break
    for j in range(1,6):
        print(i,j)

    i+=1

#process for ex2:
'''
iteration 1:
    outer loop i = 1:
        checking i == 3: false
        so we go to inner loop 
            where j = 1:
            so print 1,1
            j = 2
            so print 1,2
            j = 3
            so print 1,3
            j = 4
            so print 1,4
            j = 5
            so print 1,5
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