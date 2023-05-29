import random

def generálás(db, fix):
    place = random.randint(1, db)
    for i in range(place-1):
        rand = random.randint(1,99)
        if rand != fix:
            print(rand,end=" ")
        else:
            rand = random.randint(1,99)
            print(rand,end=" ")
    print(fix,end=" ")
    if db-place > 0:
        for i in range(db-place):
            rand = random.randint(1,99)
            if rand != fix:
                print(rand,end=" ")
            else:
                rand = random.randint(1,99)
                print(rand,end=" ")
    print("")
    


n = int(input("Dobble: "))
x = random.randint(1, 99)

for i in range(10):
    x = random.randint(1, 99)

    for i in range(2):
        generálás(n, x)
    
