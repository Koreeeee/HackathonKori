import random

xcor = random.randint(1,58)

ycor = random.randint(1,29)

while True:

    if ycor != 0 and ycor != 30:
        print("............................................................")
        for i in range(ycor-1):
            print(".                                                          .")
        if xcor == 0:
            print("@                                                          .")
        elif xcor == 59:
            print(".                                                          @")
        elif xcor != 0:
            print(".",end="")
            for i in range(xcor-1):
                print(" ",end="")
            print("@",end="")
            for i in range(58-xcor):
                print(" ",end="")
            print(".")
        for i in range(29-ycor):
            print(".                                                          .")
        print("............................................................")
    
    elif ycor == 0:
        for i in range(xcor):
            print(".",end="")
        print("@",end="")
        for i in range(59-xcor):
            print(".",end="")
        print("")
        for i in range(28):
            print(".                                                          .")
        print("............................................................")
    
    elif ycor == 30:
        print("............................................................")
        for i in range(28):
            print(".                                                          .")
        print(".",end="")
        for i in range(xcor-1):
            print(".",end="")
        print("@",end="")
        for i in range(59-xcor):
            print(".",end="")
        print("")
    

    print("Hova?")
    if ycor == 0 or ycor == 30 or xcor == 0 or xcor == 59:
        print("Most ennycori volt, szép napot!")
        break
    else:
        iranycor = input("")
    


    if iranycor == "jobbra":
        xcor = xcor + 1
    elif iranycor == "balra":
        xcor = xcor - 1
    elif iranycor == "le":
        ycor = ycor + 1
    elif iranycor == "fel":
        ycor = ycor - 1
    elif iranycor == "meguntam":
        print("Akkor további szép napot!")
        break