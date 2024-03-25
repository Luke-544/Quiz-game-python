print("Hello!! Welcome to my quiz game")

play =input("Do you wish to play? ")
score = 0

if play.lower() == "yes":
    print("Awesome! Let's begin")
    print("Good luck!!")
    print("Hope you enjoy my game!")
    
elif play.lower() == "no":
    print("Too bad!!!")
    print("Bye bye")
    quit()
   
else:
    print("Invalid answer")
    quit()

question = input("What is the full meaning of cpu? ")
if question.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("What does GPU mean? ")
if question.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("What does RAM stand for? ")
if question.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("What does PSU stand for? ")
if question.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You got "+str(score)+" questions correct")
print("You got "+str(score/4 * 100)+"% in your quiz")