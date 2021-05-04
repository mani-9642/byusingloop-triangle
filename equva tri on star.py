# = 6
#m = (3 * n)-6
#for i in range(n):
    #for j in range(m):
        #print(end=" ")
    #m = m - 1  # decrementing m after each loop
    #for j in range(i + 1):
        # printing full Triangle pyramid using stars
        #print(" " + "*" + " ", end=' ')
    #print()
n=10
for x in range(1,6):
    print(" "*n,end="")
    print("*"*x)
    n-=1