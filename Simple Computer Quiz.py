print("Welcome to my computer game")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay lets play")
score = 0

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect answer")

answer = input("Which is the best programming language ")
if answer == "python":
    print("Correct!")
    score += 1
else:
    print("Incorrect answer")

answer = input("What does a server do? ")
if answer == "computer device that manages network resources":
    print("Correct!")
    score += 1
else:
    print("Incorrect answer")

answer = input("Which is the largest server in the world ")
if answer == "mega server":
    print("Correct!")
    score += 1
else:
    print("Incorrect answer")

answer = input("What is a database? ")
if answer == "structured collection of data stored elecronically":
    print("Correct!")
    score += 1
else:
    print("Incorrect answer")

answer = input("What does SQL stand for? ")
if answer == "structured Querry language":
    print("Correct!")
    score += 1
else:
    print("Incorrect answer")

answer = input("What is the best SQL tool to use? ")
if answer == "mySql":
    print("Correct!")
    score += 1
else:
    print("Incorrect answer")

print("You got " + str(score) +  "questions correct!")
print("You got " + str((score / 7) * 100) +  "%")

