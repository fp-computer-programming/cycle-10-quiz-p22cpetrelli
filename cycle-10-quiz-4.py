#author CJP 03/23/2022
#define function
def high_prices(price_of_items):
# enumerate lists 
    for i, v in enumerate(price_of_items):
#if used so that the function can find what values are greater than 40 
        if v > 40: 
#then if the functions are greater they are then reduced
            price_of_items[i] = v - 10
#returns value
    return price_of_items

print(high_prices([30, 40, 25, 55, 60, 80, 65]))