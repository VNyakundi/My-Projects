name = input("enter your name: ")

print("welcome", name, "to this adventure!")

answer = input("you are on a dirt road, you can go left , right or back(left/right/back) which way do you wanna go?  ")

if answer == " back":
    answer = input("you have decided to go back to the scary road you came from, do you wanna face the zoombies or the vampires(zoombies/vampired)? ")
    if answer == "zoombies":
        print("there are thousands of zoombies, they ate you, you loose!")
    elif answer == "vampires":
        print("you were eaten by vampires and got transformed into a hybrid vampire, you get to live forver, You Win!")
    else:
         print("not a valid option, you loose!")

if answer == "left":

    answer = input("youve come to a river, you can walk around it or swim accross, which option do you wanna choose from? ")

    if answer =="swim":
        print("you swam across and was eaten by an alligator, you loose")
    elif answer =="walk":
        print("you walked for many miles and ran ou tof water, you lost the game")
    else:
        print("not a valid option, you loose!")

elif answer == "right":
    answer = input("you have come to a bridge, and it is wobbly, do you wanna cross it or head back?(cross/back)? ")

    if answer =="back":
        answer = input("you went back to the highway, do you wanna board a bus or ask for an uber(bus/uber)? ")
        if answer == "bus":
            print("you went back into the city, and found a ghost city of the walking dead, you loose!")
        elif answer == "uber":
            print("uber driver was a serial killer so he killed you, you loose")
        else:
             print("not a valid option, you loose!")

    elif answer =="cross":
         answer=input ("you crossed the bridge and met a stranger, do you talk to them(yes/no)? ")
        
         if answer == "yes":
             print("you talked to the stranger an dthey gave you GOLD, you win!")
         elif answer == "no":
             print("you ignored the stranger and they were offended, you loose!")
         else:
             print("not a valid option, you loose!")      
    else:
        print("not a valid option, you loose!")
   
else:
    print("not a valid option, you loose")

print("thank you for trying", name)