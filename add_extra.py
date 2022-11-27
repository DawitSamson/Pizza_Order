extra_cheese = 0
extra = 2
net_price = 0


def add_extra_menu():
    global extra_cheese
    from piizza_order import net_price
    from piizza_order import total_price
    add_extra = input("\nWould you like an extra cheese? yes/no: ")
    if add_extra == "yes" or add_extra == "y":
        qty_extra = int(input("How many extra cheese you need? "))
        extra_cheese = extra_cheese + (extra * qty_extra)
        total_price = net_price + extra_cheese
        print("The current price is  ", total_price, "$")
