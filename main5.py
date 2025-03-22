def get_days_week(num_day):
    day = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Вокресенье"
    ]

    if 1 < num_day <=7:
        return day[num_day - 1]
    
get_days_week(5)