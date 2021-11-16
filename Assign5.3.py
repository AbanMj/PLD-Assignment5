#Program 3: Life stages
#Create a program that ask for an age of a person
#Display the life stage of the person

def inputage():
    agef = int(input("Enter your age: "))
    return agef

Age = inputage()

if Age == 0 and Age <= 12:
    print("Kid")
else:#0 - 12 : Kid
    if Age >= 13 and Age <= 17:
        print("Teen")
    else:#13 - 17 : Teen
        if Age == 18:
            print("Debut")
        else:#18 : Debut
            if Age >= 19:
                print("Adult")
            else: #19 above : Adult
                pass