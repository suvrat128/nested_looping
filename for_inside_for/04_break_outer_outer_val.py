#breaking outer loop with outer loop value
#ex1

for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if i == 3:
        break
    

#ex2

for i in range(1,6):
    if i == 3:
        break
    for j in range(1,6):
        print(i,j)

#process 
'''
iteration 1:
    outer loop i = 1:
        checking i == 3: false
        so we go to inner loop 
            where j = 1:
            so print 1,1
        now j = 2:
            so print 1,2
        now j =3:
            so print 1,3
        now j = 4:
            so print 1,4
        now j =5:
            so print 1,5
iteration 2:
    outer loop i =2:
        checking i == 3: false
        so we go to inner loop
            where again inner loop run for 5 time 
                so print 2,1 2,2 2,3 2,4 2,5
iteration 3:
    outer loop i =3:
        checking i == 3: true
        so terminate the outer loop so program will end at this point only
        

'''