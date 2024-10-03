from datetime import datetime, timedelta


def calculate_days_and_weekends(start_date, end_date):
    # Calculăm intervalul de zile
    total_days = (end_date - start_date).days + 1  # +1 pentru a include ziua de sfârșit
    weekend_days = 0  # Counter pentru zilele de weekend
    weekdays_count = {
        "Luni": 0,
        "Marți": 0,
        "Miercuri": 0,
        "Joi": 0,
        "Vineri": 0,
        "Sâmbătă": 0,
        "Duminică": 0
    }

    # Verificăm fiecare zi din interval
    for i in range(total_days):
        current_day = start_date + timedelta(days=i)
        # Verificăm dacă ziua curentă este sâmbătă sau duminică
        if current_day.weekday() in (5, 6):  # 5 = sâmbătă, 6 = duminică
            weekend_days += 1

        # Incrementăm contorul pentru ziua corespunzătoare
        if current_day.weekday() == 0:
            weekdays_count["Luni"] += 1
        elif current_day.weekday() == 1:
            weekdays_count["Marți"] += 1
        elif current_day.weekday() == 2:
            weekdays_count["Miercuri"] += 1
        elif current_day.weekday() == 3:
            weekdays_count["Joi"] += 1
        elif current_day.weekday() == 4:
            weekdays_count["Vineri"] += 1
        elif current_day.weekday() == 5:
            weekdays_count["Sâmbătă"] += 1
        elif current_day.weekday() == 6:
            weekdays_count["Duminică"] += 1

    return total_days, weekend_days, weekdays_count


def main():
    # Introducerea datelor de la utilizator pe o singură linie
    input_dates = input("Introdu datele de început și sfârșit (format: dd.mm.yyyy - dd.mm.yyyy): ")

    # Separăm datele de început și sfârșit
    start_str, end_str = input_dates.split(" - ")

    # Parsează datele în obiecte datetime
    start_date = datetime.strptime(start_str, '%d.%m.%Y')
    end_date = datetime.strptime(end_str, '%d.%m.%Y')

    # Verificăm dacă data de început este mai mică decât data de sfârșit
    if start_date > end_date:
        print("Data de început trebuie să fie înainte de data de sfârșit.")
        return

    # Calculăm zilele, weekend-urile și numărul de zile pe fiecare zi a săptămânii
    total_days, weekend_days, weekdays_count = calculate_days_and_weekends(start_date, end_date)

    # Calculăm numărul de săptămâni (zile totale împărțite la 7)
    total_weeks = total_days // 7

    # Afișăm rezultatele
    print(f"\nÎn intervalul de la {start_date.strftime('%d-%m-%Y')} la {end_date.strftime('%d-%m-%Y')}:")
    print(f"Numărul total de zile: {total_days}")
    print(f"Numărul de zile de weekend: {weekend_days}")
    print(f"Numărul de săptămâni: {total_weeks}")

    # Afișăm numărul de zile pentru fiecare zi a săptămânii
    for day, count in weekdays_count.items():
        print(f"Numărul de zile de {day}: {count}")


if __name__ == "__main__":
    main()
