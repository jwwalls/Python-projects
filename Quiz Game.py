print("Welcome To my computer Quiz")

playing = input("Do you want to play? ")

if playing != "yes":
    quit() 

score = 0

print("okay lets play")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("correct")
    score +=1
else: 
    print("Incorrect")

answer2 = input("What is your favorite color ")
if answer2 == "red":
    print("correct")
    score +=1
else:
    print("incorrect")

answer3 = input("What is your worst food ")
if answer3 == "dragons":
    print("correct")
    score +=1
else:
    print("incorrect")

answer4 = input("What 9 + 1 ")
if answer4 == "10":
    print("correct")
    score +=1
else:
    print("incorrect")

print(f"Final score {score/4 * 100}")