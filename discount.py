import random
from next_order import Ttl_price_delivery
new_price = 0
# Ttl_price_delivery = 0


def discount_game():
    global new_price
    game = input("\nDo you went to play a game and get discount for your price? y/n: ")
    if game == "yes" or game == "y":
        play1_value = random.randint(1, 9)
        play2_value = random.randint(1, 9)
        play_value = play1_value * play2_value
        print("Your game result is: ", play_value, "%")
        new_price = Ttl_price_delivery * (1 - (play_value / 100))
        print("\n\t\t\t\t\tyour final Price with discount game is", new_price, "$")
        print("\n\t\t\t\t\t\t\t\t 'BON APPETIT!!!' Enjoy your Pizza!!! \n\t\t\t\t\t\t\tHave a nice day!!!")

    else:
        print("\n\t\t\t\tThe total price with delivery for your order will be: ", Ttl_price_delivery, "$")

