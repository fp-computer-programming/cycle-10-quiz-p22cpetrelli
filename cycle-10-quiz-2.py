#author CJP 03/23/2022
#define function
def five_less(price_of_items):

# enumerate lists    
    for i, v in enumerate(price_of_items):
#subtracts five from each value then returns new value
        price_of_items[i] = v - 5 

    return price_of_items

print(five_less([30, 40, 25, 55, 60, 80, 65]))