#Code written by Sanidhya (Sunny) Sharma, on 16/11/24 and 17/11/24
from time import sleep

#defining the text art
head = """           /\    /\.
         |   º  º  |
         |≡  _T_  ≡|"""
neck_G = "             |  |"
torso = """           __|  |__
      |  |         |  |
      |  |         |  |
      |  |         |  |"""
torso_G = "      |  |         |  |"
hands = "       WW |   |   | WW"
legs = """          |   |   |
          |   |   |"""
legs_G = "          |   |   |"
feet = "           UUU UUU"

#defining variables
n_count = 0
t_count = 0
l_count = 0
ex = 0
skip = 0

#intro message
print("This is growthcat, he is a cat who you can grow, you can grow his legs, his torso, and his neck. This is a game that has 5 endings, based on your actions, please enjoy.")
print(head)
print(torso)
print(hands)
print(legs)
print(feet)

#pause
sleep(1.5)

#input processing
while ex < 1:
    q_flag = 1
    while q_flag > 0:
        letter = str(input("what part of growthcat do you want to grow? Legs, torso or neck?(L, T, N) (or 'ex' to end the game)"))
        if letter == "L" :
            l_count = l_count + 1
            q_flag = 0
            print("l")
        elif letter == "l" :
            l_count = l_count + 1
            q_flag = 0
            print("l")
        elif letter == "T":
            t_count = t_count + 1
            q_flag = 0
            print("t")
        elif letter == "t":
            t_count = t_count + 1
            q_flag = 0
            print("t")
        elif letter == "N":
            n_count = n_count + 1
            q_flag = 0
            print("n")
        elif letter == "n":
            n_count = n_count + 1
            q_flag = 0
            print("n")
        elif letter == "ex":
            ex = 1
            print("sad to see you go, here is a goodbye from growthcat")
            break
        else:
            print("please use one of the specified responses")
            skip = skip + 1
            if skip == 10:
                if l_count == 0:
                    if t_count == 0:
                        if n_count == 0:
                            print("You have reached the true ending. You went agaist what the system wanted you to do, and didn't change anything, because growth cat is perfect as he is, you are the true winner of this game, thank you, for playing.")
                            ex = 1
                            break
#making more growthcats, based on user input
    l_temp = l_count
    t_temp = t_count
    n_temp = n_count
    print(head)
    while n_temp > 0:
        print(neck_G)
        n_temp = n_temp - 1
    print(torso)
    while t_temp > 0:
        print(torso_G)
        t_temp = t_temp - 1
    print(hands)
    print(legs)
    while l_temp > 0:
        print(legs_G)
        l_temp = l_temp - 1
    print(feet)
#ending criteria
    if l_count == 10:
        print("Congratulations! You reached the 'Daddy-long-legs cat' ending! (1/5), thank you for playing!")
        ex = 1
        break
    if n_count == 10:
        print("Congratulations! You reached the 'Girraffe cat' ending! (2/5), thank you for playing!")
        ex = 1
        break
    if t_count == 10:
        print("Congratulations! You reached the 'Alligator cat' ending! (3/5), thank you for playing!")
        ex = 1
        break
    if l_count == 9:
        if n_count == 9:
            if l_count == 9:
                print("CONGRATULATIONS!!! You reached the super secret 'Proportionately-tall cat' ending (4/5), thank you for playing!")
                ex = 1
                break
