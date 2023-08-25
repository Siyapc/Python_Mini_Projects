print("Welcome to my computer Quiz!!")

playing = input("Do you want to play?  ")

if playing.lower() != "yes" :
    quit()

count = 0

print("Okay!! Lets play:) ")

answer= input("1)Coded entries which are used to gain access to a computer system are called? ")
if answer.lower() == "passwords":
    print('Correct')
    count=count+1
else:
    print("Incorrect")

answer= input("2)……….is a combination of hardware and software that facilitates the sharing of information between computing devices? ")
if answer.lower() == "network":
    print('Correct')
    count=count+1
else:
    print("Incorrect")

answer= input("3)What does ALU stands for? ")
if answer.lower() == "arithmetic logic unit":
    print('Correct')
    count=count+1
else:
    print("Incorrect")

answer= input("4)First page of Website is termed as? ")
if answer.lower() == "homepage":
    print('Correct')
    count=count+1
else:
    print("Incorrect")

answer= input("5)Where are data and programme stored when the processor uses them? ")
if answer.lower() == "main memory":
    print('Correct')
    count=count+1
else:
    print("Incorrect")

print("Quiz is Complete!!!!!!!")
print(" Your total score is: "+ str(count))
print(" Your got: "+ str((count/5)*100)+ "% ")