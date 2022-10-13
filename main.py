#BMI CAlculator With Interprete Message

# print("BIM Calculator")
# weight = float(input("Enter Your Weight:\t"))
# height = float(input("Enter Your Height:\t"))
# result = round(float(weight / height **2))
# if result <= 18.5:
#     print(f'Your BMI Is {result}'+"You Are Under Weight")
# elif result <= 25.0:
#     print(f'Your BMI is {result}'"+You Have A Normal Weight")
# elif result <= 30:
#     print(f'Your BMI is {result}'+"You Are Slightly obese")
# elif result <= 35:
#     print(f"Your Bmi is {result}" + 'You Are Obese')
# else:
#     print(f'Your BMI Is {result}'"You Are Clinically Obese")
#python Pizza Delivery

# print("Welcome To Python Pizza")
# pizza_size = input("Enter Which Pizza you Would like to order S, M or L:\t")
# peppeoni = input("Do You Want To add Peppeoni Y/N ?:\t")
# cheese = input("DO You want To Add some Cheese Y/N ? \t")
# bill = 0
#
#
# if pizza_size =="S":
#     bill += 15
# elif pizza_size =="M":
#     bill += 20
# else:
#     bill += 25
# if peppeoni=="Y":
#     if peppeoni=="S":
#         bill += 2
#     else:
#         bill += 3
# if cheese=="Y":
#     bill += 1
#
# print(f"your final bill amount is {bill}")

# LOve Calculator
# print("Welcome to Love Calculator")
# name1 = (input("Enter The Boy Name:\t"))
# name2 = input("Enter The girl name:")
# combine_name = name1 + name2
# lower_name = combine_name.lower()
# t = lower_name.count("t")
# r = lower_name.count("r")
# u = lower_name.count("u")
# e = lower_name.count("e")
# first_digit = t + r + u + e
# l = lower_name.count("l")
# o = lower_name.count("o")
# v = lower_name.count("v")
# e = lower_name.count("e")
# second_digit = l+o+v+e
# love_resul = int(str(first_digit)+str(second_digit))
# print(love_resul)
# if love_resul<=10 or love_resul>90:
#     print(f"Your Score is {love_resul},"+'you go together like coke and mentos')
# if love_resul<=50 or love_resul>=40:
#     print(f"Your Score is {love_resul}, " + 'you are alright together')


# Small game 
print("Welcome To Treasure Island")
print("Your Mission is to find the treasure")
choice1 = input("You're at a cross road. Where do you want to go? Left or Right").lower()
if choice1=="left":
    print("!!! GAME OVER !!! You got hit by bus")
else:
    choice2 = input("YOu come to a lake. There is an island in the miiddle of the lake.Type wait to wait for a boat or Type swim to swimm across").lower()
if choice2 =="swim":
    print("!!! GAME OVER !!! You were eaten alive by crocodile")
else:
    choice3 = input("Damn!!! You arrived At the treasure Island . There is a house with 3 doors which is red, blue amd blue. Which one you want to use?").lower()
if choice3 == "yellow":
    print("!!! HURRY  !!! You WIN The GAME And Won 100k")
elif choice3 == "blue":
    print("!!! GAME OVER !!! You got into room having anoconda")
elif choice3 == "red":
    print("!!! GAME OVER !!! You got into fire")
else:
    print("the dooor doesnot exit")

