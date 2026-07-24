import random
def random_list():  #random list generator of variable length
   y=range(0,10)
   n=int(input("input number of items:"))
   i=0
   l1 = []
   while i<n:
        x = random.choice(y)
        l1.append(x)
        i=i+1
   return l1


def sort_list():   #generates a random sorted list
    l = random_list()
    l2=[]
    print(l) #remove later
    while len(l)>0:
        small = l[0]
        for i in l:
            if small>i:
                small=i
        l2.append(small)
        l.remove(small)
    print(l2)
    return l2

sort_list()