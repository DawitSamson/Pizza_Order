# order pizza with discount whill playing dice game
from add_extra import add_extra_menu
from next_order import next_order_req
from exit_text import exit_message

pizza_size = {
    "s": 40,
    "m": 50,
    "l": 60,
    "xl": 75}
quantity = 0
qty_extra = 0
# extra = 2
net_price = 0
order_p = ""
total_price = 0
# extra_cheese = 0
beersheva_delivery = 20
outside_delivery = 60
Ttl_price_delivery = 0
next_order = "yes"
add_extra = "no"
new_price = 0


def customer_order():
    global next_order, new_price, net_price
    print("\n******************** 'Pizza.io' House of Pizza  ******************")
    age = int(input("\n To continue your order Please enter your age: "))
    print("\n\t\t\tWelcome to 'Pizza.io' House of pizza!!! Please Make your order.")
    while age < 18:
        exit_message()
        break
    else:
        while next_order == "yes" or next_order == "y":
            global quantity
            # Ordering a pizza size
            from next_order import pizza_list
            pizza_list()
            choice_size = input("\n Please choose pizza size s/m/l/xl: ")
            quantity = int(input("\t\t\t\tHow much you need?  "))
            net_price += pizza_size[choice_size] * quantity  # --------------------- using dictionary
            # Asking for extra cheese
            add_extra_menu()
            # Asking to order another using function
            next_order_req()
