row= input("enter the number of rows:")
col= input("enter the number of  cloumns:")
print(" the hollow square is :")
for i in range(1, int(row)+1):
    for j in range(1, int(col)+1):
        if i==1:
            print("*", end="   ")
        elif  j==1:
            print(" ", end="   ")
        print()