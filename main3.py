def sum_number(ticket):
    if ticket == 500:
        return "Вы получите 0 рублей сдачи"
    
    if ticket != 500:
        return "У вас не хватает",  ticket - 500, "рублей"
    
    
sum_number(500)