for i in range(0, 100, 1):

    if (i+1) % 3 == 0 and (i+1) % 5 == 0:
        print(str(i+1) + " N3N5")

    elif (i+1) % 3 == 0:
        print(str(i+1) + " N3")

    elif (i+1) % 5 == 0:
        print(str(i+1) + " N5")

    else:
        print(i+1)