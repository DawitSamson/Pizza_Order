total_price = 0
beersheva_delivery = 20
outside_delivery = 60
Ttl_price_delivery = 0

from discount import discount_game



def next_order_req():
    global Ttl_price_delivery, outside_delivery, beersheva_delivery
    next_order = input("Do you went to order another pizza yes/no: ")
    if next_order == "no" or next_order == "n":
        print("\nPlease conform your destination \n\t\t\t*for beersheva (b) or \n\t\t\t*for outside of the 'Negev "
              "Capital City' (o)")
        city = input("your delivery destination b/o: ")
        if city == "b" or city == "beersheva":
            Ttl_price_delivery = total_price + beersheva_delivery
            print("\n\t\t\t\tThe total price with delivery for your order will be: ", Ttl_price_delivery, "$")
            discount_game()
            exit()

        else:
            Ttl_price_delivery = total_price + outside_delivery
            print("\n\t\t\t\tThe total price with delivery for your order will be: ", Ttl_price_delivery, "$")
            discount_game()
            exit()


def pizza_list():
    print("\t\t\t\t\t\t size small (s) price 40"
          "\n\t\t\t\t\t\t size medium (m) price 50 "
          "\n\t\t\t\t\t\t size large (L) price 60"
          "\n\t\t\t\t\t\t size X-large (xl) price 75")
