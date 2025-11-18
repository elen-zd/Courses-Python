def month_to_season(month):
    if (month <= 2) or (month == 12):
        return ("Зима")
    elif (month > 2) and (month <= 5):
        return ("Весна")
    elif (month > 5) and (month <= 8):
        return ("Лето")
    elif (month > 8) and (month < 12):
        return ("Осень")
    else:
        return ("Некорректный месяц!")


print(month_to_season(12))
