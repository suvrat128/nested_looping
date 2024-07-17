Nested looping statements: 

1. It is a process of defining a loop inside another loop  

2. We can create nested looping statement in 4 ways : 

1. For inside for 

2. For inside while 

3. While inside for  

4. While inside while


# for inside for:
'''It is a process of defining a for loop inside another for loop'''

# both inner and outer loops are executing completely

    for in range(1,6):
        for j in range(1,6):
            print(i,j)

# braking inner loop with inner loop value

    for in range(1,6):
      for j in range(1,6):
          print(i,j)
          if j ==3:
              break
# breaking inner loop with outer loop value

    for in range(1,6):
      for j in range(1,6):
          print(i,j)
          if i == 3:
             break

#braking outer loop with outer loop value
#ex1

     for in range(1,6):
        for j in range(1,6):
            print(i,j)
        if i == 3:
           break


#ex2

    for in range(1,6):
        if i == 3:
            break
        for j in range(1,6):
            print(i,j)



# braking outer loop with inner loop value
#ex1

    for i on range(1,6):
        if j==3:
            break
        for j in range(1,6):
            print(i,j)

'''error because j is not define'''

#ex2:

    for i on range(1,6):
        for j in range(1,6):
            print(i,j)
        if j==3:
            break

''' loop will not break because from inner loop j is comming out with
5 as its values'''

#ex3:

    for i on range(1,6):
        for j in range(1,6):
            print(i,j)
        if j==5:
            break
