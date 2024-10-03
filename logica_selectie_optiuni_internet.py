import webbrowser

while True:
    Produs = int(input(f"Selectati produsul:\n1. Monitoare \n2. Placi Video \n3. Placi de baza \n4. Procesoare \n"))
    if Produs == 1:
        print("Ai ales Monitoare.\n")
        webbrowser.open("https://www.emag.ro/monitoare-lcd-led/c?ref=hp_menu_quick-nav_23_3&type=category")
        continue
    if Produs == 2:
        print("Ai ales Placi Video.\n")
        webbrowser.open("https://www.emag.ro/placi_video/c?ref=hp_menu_quick-nav_23_7&type=category")
        continue
    if Produs == 3:
        print("Ai ales Placi de baza.\n")
        webbrowser.open("https://www.emag.ro/placi_baza/c?ref=hp_menu_quick-nav_23_8&type=category")
        continue
    if Produs == 4:
        print("Ai ales Procesoare.\n")
        webbrowser.open("https://www.emag.ro/procesoare/c?ref=hp_menu_quick-nav_23_9&type=category")
        continue
    if Produs not in range(4):
        print("Ai selectat o optiune inexistenta, vei fi redirectionat in meniul principal.\n")
        webbrowser.open("https://www.emag.ro/")
        break
    else:
        print("Daca mai doriti si altceva \n")
        continue