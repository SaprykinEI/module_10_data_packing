guests = {
    "Sergey": 1600,
    "Andrey": 2200,
    "Dmitriy": 1800,
    "Diana": 2300,
    "Alexander": 2500,
    }

total = 0

guests_names = ', '.join(guests.keys()  )

for check_value in guests.values():
    total += check_value

print(f"В кафе были {guests_names}")
print(f"Общий чек {total}")
print(f"Каждый платит {total / len(guests)} ")