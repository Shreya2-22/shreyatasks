print("BPP Pizza Price Calculator")
print("==========================")

def user_input():

    while True:

        try:
            user_pizza_number = int(input("How many pizzas ordered? "))
            if user_pizza_number > 0:
                break
            else:
                print("Please enter a positive integer!")
        except ValueError or TypeError:
            print("Please enter a number!")

    while True:

        try:
            user_delivery = input("Is delivery required? (Y/N): ").upper()
            if user_delivery in ['Y','N']:
                break
            else:
                print('Please answer "Y" or "N".')
        except ValueError:
            print('Please answer "Y" or "N".')

    while True:

        try:
            user_tuesday_discount = input("Is it Tuesday? (Y/N): ").upper()
            if user_tuesday_discount in ['Y','N']:
                break
            else:
                print('Please answer "Y" or "N".')
        except ValueError:
            print('Please answer "Y" or "N".')

    while True:

        try:
            user_app = input("Did the customer use the app? (Y/N): ").upper()
            if user_app in ['Y','N']:
                break
            else:
                print('Please answer "Y" or "N".')
        except ValueError:
            print('Please answer "Y" or "N".')

    return user_pizza_number, user_delivery, user_tuesday_discount, user_app

num_pizza, delivery, tuesday_discount, app_discount = user_input()

def with_app(pizza_number, delivery_charge, tuesday):

    if tuesday == "Y" and pizza_number >= 5:
        pizza_price =((num_pizza*12) * 0.50) * (1-0.25)
        return pizza_price

    elif tuesday == "Y" and pizza_number < 5:

        if delivery_charge == "Y":
            pizza_price = ((num_pizza*12+2.50) * 0.50) * (1-0.25)
            return pizza_price
        else:
            pizza_price = ((num_pizza*12) * 0.50) * (1-0.25)
            return pizza_price

    elif tuesday == "N" and pizza_number >= 5:
        pizza_price = (num_pizza*12)*(1-0.25)
        return pizza_price

    elif tuesday == "N" and pizza_number < 5:

        if delivery_charge == "Y":
            pizza_price = (num_pizza*12+2.50) * (1-0.25)
            return pizza_price
        else:
            pizza_price = (num_pizza*12) * (1-0.25)
            return pizza_price

def without_app(pizza_number, delivery_charge, tuesday):

    if tuesday == "Y" and pizza_number >= 5:
        pizza_price =((num_pizza*12) * 0.50)
        return pizza_price

    elif tuesday == "Y" and pizza_number < 5:

        if delivery_charge == "Y":
            pizza_price = ((num_pizza*12+2.50) * 0.50)
            return pizza_price
        else:
            pizza_price = ((num_pizza*12) * 0.50)
            return pizza_price

    elif tuesday == "N" and pizza_number >= 5:
        pizza_price = (num_pizza*12)
        return pizza_price

    elif tuesday == "N" and pizza_number < 5:

        if delivery_charge == "Y":
            pizza_price = (num_pizza*12+2.50)
            return pizza_price
        else:
            pizza_price = (num_pizza*12)
            return pizza_price

def total_price(using_app):

    if using_app == "Y":
        total_pizza_price = with_app(num_pizza, delivery, tuesday_discount)
    else:
        total_pizza_price = without_app(num_pizza, delivery, tuesday_discount)

    final_pizza_price(round(total_pizza_price, 2))

def final_pizza_price(final_total_pizza_price):
    print(f"Total Price: £{final_total_pizza_price: .2f}.")

total_price(app_discount)












