#### Describe each datatype below:(4 marks)

## 4         = integer
## 5.7       = float
## True      = boolean
## Good Luck = string

#### Which datatype would be useful for storing someone's height? (1 mark)
## Answer: FLOAT

#### Which datatype would be useful for storing someone's hair colour?(1 mark)
## Answer: STRING


####Create a variable tha will store the users name.(1 mark)
name=input("Enter your name: ")

####Create a print statement that will print the first 4 characters of the person's name.(3 marks)
print(name[0:4])

####Convert the user's name to all uppercase characters and print the result
name=name.upper()
print(name)

####Find out how many times the letter A occurs in the user's name
print(name.count("A"))

#### Create a conditional statement to ask a user to enter their age. If they are older than 18 they receive a message saying they can enter the competition, if they are under 18, they receive a message saying they cannot enter the competition.
age=int(input("enter your age:"))
if age > 18:
  print("You can join the competition")
else:
  print("You can not enter the competition")


#### Create an empty list called squareNumbers (3 marks)
squareNumbers=[]

#### Square numbers are the solutions to a number being multiplied by itself( example 1 is a square number because 1 X 1 = 1, 4 is a square number because 2 X 2 = 4 ). 
###Calculate the first 20 square numbers and put them in the list called squareNumbers. (With loop and .append 10 marks, without, Max 6 marks).
squareNumbers.append(1)
squareNumbers.append(2*2)
squareNumbers.append(3*3)
squareNumbers.append(4*4)
squareNumbers.append(5*5)
squareNumbers.append(6*6)
squareNumbers.append(7*7)
squareNumbers.append(8*8)
squareNumbers.append(9*9)
squareNumbers.append(10*10)
squareNumbers.append(11*11)
squareNumbers.append(12*12)
squareNumbers.append(13*13)
squareNumbers.append(14*14)
squareNumbers.append(15*15)
squareNumbers.append(16*16)
squareNumbers.append(17*17)
squareNumbers.append(18*18)
squareNumbers.append(19*19)
squareNumbers.append(20*20)

####Print your list (1 mark)
print(squareNumbers)

####Create a variable called userSquare that asks the user for their favourite square number
userSquare=int(input("Enter your favourite square number: "))

#### Add this variable to the end of your list called SquareNumbers
squareNumbers.append(userSquare)
print(squareNumbers)

### Create a variable called choice. This variable should choose a random element from your list. Print the variable called choice.(3 marks)
import random
choice=squareNumbers[random.randint(0,20)]
if choice in squareNumbers:
  print(choice)

####Create another print statement that prints tha following output: The random square number is: XX, where XX is where the random square number chosen by the computer.(4 marks)
print("The random square number is",choice)