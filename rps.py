import random

list =["rock","paper","scissor"]
u=""
c=""
while (u==c):
    u = input("Enter your option: Rock, paper or scissor: ")
    c = random.choice(list)
    if u==c:
        print("Your choice: ", u)
        print("Computer's choice: ", c)
        print("Same choice, pick again")
    if (u!=c):
        break
if u=="rock" and c=="paper" or u=="paper" and c=="scissor" or u=="scissor" and c=="rock":
    print("Your choice: ", u)
    print("Computer's choice: ", c)
    print(c," beats",u,", you lose")


elif u=="rock" and  c=="scissor" or u=="paper" and c=="rock" or u=="scissor" and c=="paper":
    print("Your choice: ", u)
    print("Computer's choice: ", c)
    print(u,"beats",c,",you win ")

else:
    print("Wrong choice")