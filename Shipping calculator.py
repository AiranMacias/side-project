weight_input = input("What is the weight(In pounds) of your package? ")

shipping_option = input("input what shipping option you want('Ground', 'Ground Premium', 'Drone')")

price = 1

#ground Shipping price calculate
def ground_rate():
    if float(weight_input) >10:
        price = 4.75
    elif float(weight_input) >6 :
        price = 4.0
    elif float(weight_input) >2 :
        price = 3.0 
    elif float(weight_input) <2:
        price = 1.50 
    print("Total Price: $"+ str(float(weight_input) * price +20))

# if drone shipping option is selected use this
def drone_rate():
    if float(weight_input) >10:
        price = 14.25
    elif float(weight_input) >6:
        price = 12.0
    elif float(weight_input) >2:
        price = 9.0
    elif float(weight_input) <2:
        price = 4.5
    print("Total Price: $"+ str(float(weight_input) * price))

# if ground premium is selected use this
def ground_premium():
    print("Total Price: $"+str(125))

# a function to select what to do if 
def shipping_option_selector():
    if shipping_option == "Ground":
        ground_rate()
    if shipping_option == "Drone":
        drone_rate()
    if shipping_option == "Ground Premium":
        ground_premium()
    

shipping_option_selector()
vscode-pets.start

