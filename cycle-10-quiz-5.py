#author CJP 03/23/2022
#define function
def items_and_prices(price_of_items, items):
#used nested for loop
    for rows in items: 
#enumerate list (finds values in list)
        for i, v in enumerate(rows): 
#creates proper format
            rows[i] = "{0} ${1}".format(v, price_of_items[0]) 
#deletes price so that the loop can run for each item
            del price_of_items[0] 

    return items

print(items_and_prices([30, 40, 25, 55, 60, 80, 65],[['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']])) 