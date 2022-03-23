#author CJP 03/23/2022
#define function
def prep_pride_store(price_of_items, sales):
#created counter for money made by store(money) and the amount of items sold(x)
    x = 0
    money = 0
#enumerate list
    for i, v in enumerate(price_of_items):
#this will multiply the amount of sales of the item by the value of that item
        x = v * sales[0] 
#adds the amount that each item makes to the total
        money += x 
#alows the for loop to run for every item  
        del sales[0]
        
    return money

print(prep_pride_store([30, 40, 25, 55, 60, 80, 65],[1, 3, 2, 5, 2, 1, 2]))