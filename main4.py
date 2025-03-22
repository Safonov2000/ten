def sum(cet, otr):
    if cet % 2 == 0:
        return "Число четное"
    elif cet !=2:
        return("Число не четное")
    
    if otr > 0:
        return "Число положительное"
    elif otr < 0:
        return "Число отрицательное"
    
sum(6,6)