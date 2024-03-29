weight_input = 1.0
shipping_option = ""
shipping_options = ['Ground', 'Ground Premium', 'Drone']
price = 1
re_order_option = ["Yes", "No"]
re_order_options = ""

def weight_checker():
    global weight_input
    try:
        weight_input = float(input("What is the weight(In pounds) of your package? "))
    except ValueError:
        print("Pls put valid input")
        return weight_checker()

def shipping_option_checker():
    global shipping_option
    shipping_option = input("input what shipping option you want('Ground', 'Ground Premium', 'Drone')")
    if not shipping_option in shipping_options:
        print("Please put valid input")
        shipping_option_checker()

# ground Shipping price calculate
def ground_rate():
    if float(weight_input) > 10:
        price = 4.75
    elif float(weight_input) > 6:
        price = 4.0
    elif float(weight_input) > 2:
        price = 3.0
    elif float(weight_input) < 2:
        price = 1.50
    print("Total Price: $" + str(float(weight_input) * price + 20))


# if drone shipping option is selected use this
def drone_rate():
    if float(weight_input) > 10:
        price = 14.25
    elif float(weight_input) > 6:
        price = 12.0
    elif float(weight_input) > 2:
        price = 9.0
    elif float(weight_input) < 2:
        price = 4.5
    print("Total Price: $" + str(float(weight_input) * price))


# if ground premium is selected use this
def ground_premium():
    print("Total Price: $" + str(125))

# a function to select what to do if
def shipping_option_selector():
    if shipping_option == "Ground":
        ground_rate()
    if shipping_option == "Drone":
        drone_rate()
    if shipping_option == "Ground Premium":
        ground_premium()

def re_order():
    global re_order_options
    re_order_options = input("Do you want to order again?")
    if re_order_options == "Yes":
        re_do()
    if re_order_options == "No":
        finished()
    if not re_order_options in re_order_option:
        print("Please put valid input")
        re_order()

def re_do():
    weight_checker()
    shipping_option_checker()
    shipping_option_selector()
    re_order()
    re_do()

def finished():
    print("Thank You For Shopping!, Come again!")
    input("Press any key to exit, Thank you")
    exit()
## made changes
weight_checker()
shipping_option_checker()
shipping_option_selector()
re_order()
re_do()
input("press any key to exit")
