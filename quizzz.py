print ("Welcome to my TWICE quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay, let's see if you're a TWICE fan!")
score = 0

answer = input("How many members are in TWICE ")
if answer.lower() == "nine":
    print("Correct!")
    score += 1
else:
    print("Wrong")

answer = input("How many members are from japan? ")
if answer.lower() == "three":
    print("Correct!")
    score += 1
else:
    print("Wrong")

answer = input("Who is the shortest member? ")
if answer.lower() == "chaeyoung":
    print("Correct!")
    score += 1
else:
    print("Its like you arent even trying smh")

answer = input("Who is the oldest TWICE member? ")
if answer.lower() == "nayeon":
    print("Correct!")
    score += 1
else:
    print("Dumbass")

answer = input("Which TWICE member was born in Texas? ")
if answer.lower() == "mina":
    print("Correct!")
    score += 1
else:
    print("Do you even listen?")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")