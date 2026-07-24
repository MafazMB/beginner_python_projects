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
if u=="rock" and c=="paper":
    print("Your choice: ", u)
    print("Computer's choice: ", c)
    print("paper beats rock, you lose")
elif u=="paper" and c=="scissor":
    print("Your choice: ", u)
    print("Computer's choice: ", c)
    print("scissor beats paper, you lose")
elif u=="scissor" and c=="rock":
    print("Your choice: ", u)
    print("Computer's choice: ", c)
    print("rock beats scissor, you lose")
elif u=="rock" and  c=="scissor":
    print("Your choice: ", u)
    print("Computer's choice: ", c)
    print("rock beats scissor, you win ")
elif u=="paper" and c=="rock":
    print("Your choice: ", u)
    print("Computer's choice: ", c)
    print("paper beats rock, you win")
elif u=="scissor" and c=="paper":
    print("Your choice: ", u)
    print("Computer's choice: ", c)
    print("scissor beats paper, you win")
else:
    print("Wrong choice")