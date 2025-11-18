def is_year_leap(year):
    return True if year % 4 == 0 else False


num_year = 2026
result = is_year_leap(num_year)

print(f"год {num_year}: {result}")
