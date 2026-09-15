guess = 0
neg_number = False
x = int(input("enter the number which is suspected to be a perfect square "))
if x <0:
    neg_number= True
while guess**2< x :
    guess = guess +1
if guess**2== x:
    print ("squareroot of ",x,'is',guess  )
else :
    print(x,"is not a perfect square")
    if neg_number:
        print("just checking .. did you mean ",-x,"?")



secret_number = 9
guess = 0
while guess != secret_number:
    guess = int(input("enter your guess"))
    if guess < secret_number:
        print("guess is too low ")
    elif guess > secret_number:
        print("guess is too high ")
print("you guessed it right")




secret=5 
for i in range (1,19):
    if i == secret:
        print("you guessed it right ")
        found= 1
if not found:
    print("not the right number")
else :
    print("you guessed it right")
