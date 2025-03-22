def can_get_credit(age, salary):
    if salary > 50000:
        age_limit = 18

    else:
        age_limit = 21

    if age >= age_limit and salary >= 30000:
        
        return "Вы можете получить кредит"
    
    else:
        return "Вы можете получить кредит"
    
user = {
    "name": "Kristifer Alexander",
    "age" : 21,
    "salary" : 51000
}

can_get_credit(user["age"] , user["salary"]) 
