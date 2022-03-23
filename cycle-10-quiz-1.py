#author CJP 03/23/2022
#define function
def avg(price_of_items):
#counter is used
    x = 0
# enumerate lists
    for i, v in enumerate(price_of_items): 
#adds each value in list to total value
        x += v 
#finds the number of items in list   
    ans = len(price_of_items) 
#divides total by number of items in list
    final_average = x / ans 

    return final_average   

print(avg([30, 40, 25, 55, 60, 80, 65]))