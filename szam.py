#A.	Generálj egy véletlen egész  számot az [1, 50] zárt intervallumban!  (2p)

def generaltszam():
    import random
    i = 0
    i = int(random.random() * 50)
    print(f"I/A: \n \t A generált szám: {i}")

    while ((i % 5) == 0) and ((i % 3) == 0):
        print(f"I/B: \n \t A szám öttel és hárommal is osztható!")

    if (i % 5) == 0:
        print(f"I/B: \n \t  A szám öttel osztható!")

    if (i % 3) ==0:
        print(f"I/B: \n \t A szám hárommal  osztható!")







