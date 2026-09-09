#task_1
i=1
while i<=20:
    print(i)
    i=i+1

#task_2
minute_left=5
while minute_left>=0:
    print("offer end in",minute_left,"minutes")
    minute_left-=1

#task_3
i=1
while i<=5:
    print("*"*i )
    i=i+1

#task_4
counter = 0
while   True:
        print("loading")
        counter += 1
        if counter ==3:
            break

#task_5
row=1
while row<=4:
    spaces =4-row
    while spaces>0:
        print(" ",end="")
        spaces -=1
    stars = 2*row-1
    while stars>0:
        print("*",end="")
        stars -=1
    print()
    row+=1





