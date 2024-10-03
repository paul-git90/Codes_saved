import pytz
from datetime import datetime
import time

# Dicționar care asociază orașele cu fusurile lor orare
cities_timezones = {
    "București": "Europe/Bucharest",
    "New York": "America/New_York",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "Cairo": "Africa/Cairo",
    "São Paulo": "America/Sao_Paulo",
    "Moscova": "Europe/Moscow",
    "Londra": "Europe/London",
    "Mumbai": "Asia/Kolkata",
    "Mexic": "America/Mexico_City",
    "Berlin": "Europe/Berlin",
    "Beijing": "Asia/Shanghai",
    "Bangkok": "Asia/Bangkok",
    "Dubai": "Asia/Dubai",
    "Istanbul": "Asia/Istanbul",
    "Toronto": "America/Toronto",
    "Buenos Aires": "America/Argentina/Buenos_Aires",
    "Longyearbyen": 'Arctic/Longyearbyen',
    "South_Pole": "Antarctica/South_Pole"
}


def print_time_for_cities(bucharest_time):
    # Afișează data și ora în diferite orașe
    print("\nOra și data în diferite orașe comparativ cu București:")
    for city, timezone in cities_timezones.items():
        local_tz = pytz.timezone(timezone)
        city_time = bucharest_time.astimezone(local_tz)
        print(f"{city}: {city_time.strftime('%Y-%m-%d %H:%M:%S')} ({timezone})")


def main():
    # Obține ora și data curentă în București
    bucharest_tz = pytz.timezone("Europe/Bucharest")

    try:
        while True:  # Loop infinit pentru actualizare constantă
            bucharest_time = datetime.now(bucharest_tz)  # Obține timpul curent
            print_time_for_cities(bucharest_time)  # Afișează ora în orașe
            time.sleep(60)  # Așteaptă 60 secunde înainte de următoarea actualizare
    except KeyboardInterrupt:
        print("\nProgramul a fost oprit.")


if __name__ == "__main__":
    main()
