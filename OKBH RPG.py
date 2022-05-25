from random import randint
from time import sleep
print ("A new Holotard roams around the Holoverse")
sleep(2)
print ("Confused, dazed and more than a little disoriented")
sleep(2)
print ("Do you know who he is?")
sleep(2)
print ("Of course you do, he is you")
sleep(2)
print ("You are RAIDER, the newest Holotard")
sleep(2)
player1=False
while player1==False:
    y1= input("Do you want to begin your journey?(Y/N)")
    if y1== "Y":
        player1=True
    else:
        player1=False
print("You move 50KM towards your destination")
sleep(2)
print("You come across KITSUNE")
sleep(2)
print("KITSUNE is a potential FRIEND")
sleep(2)
print("Friends help you in battles")
sleep(2)
print("If your HP falls below 50% friends provide you with either REGENERATION or CRITICAL MOVES")
sleep(2)
print("REGENERATION helps you regain anywhere between 25% to 50% of your HP")
sleep(2)
print("while CRITICAL MOVES are special moves specific to your enemy, which deal a lot of damage")
sleep(2)
print("Offering one of these items will make KITSUNE your FRIEND, so choose wisely")
sleep(2)
choice=int(input("Will you offer- 1)Cheesecake 2)Icecream (1/2)"))
x=randint(1,2)
if x==choice:
    print("Yay! KITSUNE is now your friend")
else:
    print("Sadly, yours wasn't the right choice")
sleep(1)
player2=False
while player2==False:
    y2= input("Do you want to continue your journey?(Y/N)")
    if y2=="Y":
        player2=True
    else:
        player2=False
