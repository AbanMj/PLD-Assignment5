#Program 3: Life stages
#Create a program that ask for an age of a person
#Display the life stage of the person

def inputage():
    agef = int(input("Enter your age: "))
    return agef

Age = inputage()

if Age == 0 and Age <= 12:
    print("According to your age, your life stage is Kid. ")
else:#0 - 12 : Kid
    if Age >= 13 and Age <= 17:
        print("According to your age, your life stage is Teen")
    else:#13 - 17 : Teen
        if Age == 18:
            print("According to your age, your life stage is Debut")
        else:#18 : Debut
            if Age >= 19:
                print("According to your age, your life stage is Adult")
            else: #19 above : Adult
                pass

