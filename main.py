def calc_delivery_cost(weight):
    if weight <=2:
        return 300
        
    
    elif 2 < weight <=5:
        return 500
    
    elif 5 < weight <=10:
        return 800
    
    else:
        return 1200
    
calc_delivery_cost(4)
# TEN

def mass(rost, ves, num):
    if ves / rost * num:
        return "Будет" , {ves / rost * num}

mass(160, 57 , 2)
