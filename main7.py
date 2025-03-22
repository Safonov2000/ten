def get_day_of_week(num_day):
    days = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье"
    ]

    if 1 <= num_day <=7:
        return days[num_day - 1]

    else:
        return "Ошибка"

get_day_of_week(5)