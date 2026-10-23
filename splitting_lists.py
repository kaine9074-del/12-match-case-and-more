import random
import time
mystr = "This is a sentence about the hobgoblin Jace"
list_of_words = mystr.split() #if we specify nothing, it will split on " "
print(list_of_words)
list_of_words[-1] = "Mykita"
print(list_of_words)
mystr = " ".join(list_of_words)
print(mystr)
#simulated csv (comma seperated values)
str2 = "name,type,strength,health"
p1 ="zach,orc,5,10"
p2 ="isaac, lootgoblin,2,6"
headers = str2.split(",")
p1list = p1.split(",")
p2list = p2.split(",")

#iterate through p1list with index and value(with enumerate)
for idx, val in enumerate(p1list):
    print(f"{headers[idx]}: {val}")

for idx, val in enumerate(p2list):
    print(f"{headers[idx]}: {val}")
playerlists = [p1list, p2list]
wins = [0,0]
print(f"Its the big battle of {p1list[0]} vs {p2list[0]}") 
input("press enter to continue!")
for i in range(5):
    print(f"Round {i+1}")
    choice = random.randint(0,2)
    outcome = []
    if choice < 2:
        attacker = playerlists[choice]
        defender = playerlists[1-choice]
        outcome.append(attacker[0])
        playerlists[choice][-1] += 0
        print(f"{attacker[0]} delivered {attacker[2]} damage to {defender[0]} and defeated him/her")
    else:
        outcome.append("tie")
        print("It was a tie")
    time.sleep(2)

print(f"{p1list[0]} won {p1list[-1]} rounds")
print(f"{p1list[0]} won {p1list[-1]} rounds")
if p1list[-1] > p2list[-1]:
    print(p1list[0], "won!")
elif p1list[-1] < p2list[-1]:
    