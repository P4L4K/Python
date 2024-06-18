for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            print("W ",end="")
        else:
            print("B ",end="")
    print()