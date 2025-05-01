name = input("please enter your name:")
print("Hello, " + name + "!")
prompt = "If you tell me which car do you want "
name = input(prompt)
budget = input(" Tell  me what is your budget, in dollars ")
budget = int(budget)
if budget >= 10000:
    print("\nYou're enough to afford luxury car!")
else:
    print("\nOther wise we will give you another option.")  
number = input("Enter your contact number , we will give you further details:")
#DO NOT COVERT TO INT- JUST WORK WITH STRING
if number.startswith("+1"):
    print("\nThe contact number: " + number)
else:
    print("\nThe number is out of  our judiciary: " + number)    

