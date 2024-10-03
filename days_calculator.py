from datetime import datetime, timedelta

"""
Acest program calculează cate zile de weekend sunt într-un anumit interval de timp
"""


def calculate_days_and_weekends(start_date, end_date):
    # Calculăm intervalul de zile
    total_days = (end_date - start_date).days + 1  # +1 pentru a include ziua de sfârșit
    weekend_days = 0  # Counter pentru zilele de weekend

    # Verificăm fiecare zi din interval
    for i in range(total_days):
        current_day = start_date + timedelta(days=i)
        # Verificăm dacă ziua curentă este sâmbătă sau duminică
        if current_day.weekday() in (5, 6):  # 5 = sâmbătă, 6 = duminică
            weekend_days += 1

    return total_days, weekend_days


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

    # Calculăm zilele și weekend-urile
    total_days, weekend_days = calculate_days_and_weekends(start_date, end_date)

    # Afișăm rezultatele
    print(f"\nÎn intervalul de la {start_date.strftime('%d-%m-%Y')} la {end_date.strftime('%d-%m-%Y')}:")
    print(f"Numărul total de zile: {total_days}")
    print(f"Numărul de zile de weekend: {weekend_days}")


if __name__ == "__main__":
    main()
