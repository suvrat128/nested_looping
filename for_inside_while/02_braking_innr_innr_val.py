# breaking of inner loop with inner value

i=1
while i<6:
    for j in range(1,6):
        print(i,j)
        if j == 3:
            break
    i+=1

#process
'''
iteration 1:
    outer loop i will 1:
        inner loop j will 1:
            so print 1,1
            check 1 == 3: false
        inner loop j = 2
            so print 1,2
            check 2 == 3: false
        inner loop j = 3
            so print 1,3
            check 3 == 3: true 
                so terminate the inner loop
        at last increment i from 1 to 2
iteration 2:
    outer loop i = 2:
        inner loop will run againg till j == 3
            so print 2,1 2,2 2,3 
            after that j is 3 so inner loop will terminted
        at last increment i from 2 to 3
iteration 3:
    outer loop i = 3:
        inner loop will run againg till j == 3
            so print 3,1 3,2 3,3 
            after that j is 3 so inner loop will terminted
        at last increment i from 3 to 4
iteration 4:
    outer loop i = 4:
        inner loop will run againg till j == 3
            so print 4,1 4,2 4,3 
            after that j is 4 so inner loop will terminted
        at last incremrnt i froom 4 to 5
iteration 5:
    outer loop i = 5:
        inner loop will run againg till j == 3
            so print 5,1 5,2 5,3 
            after that j is 3 so inner loop will terminted
        at last incremrnt i from 5 to 6

'''
