#breaking of outer loop with outer loop value

for i in range(1,6):
    j=1
    while j<6:
        print(i,j)
        j+=1
    if i==3:
        break
