from datetime import date


## ---- DANE ODNOŚNIE LIMITÓW PRĘDKOŚCI W POSZCZEGÓLNYCH OBSZARACH I WYSOKOŚCI MANDATÓW ---- ##

obszary_osobówka = {
    1 : 20,
    2 : 50,
    3 : 90,
    4 : 100,
    5 : 120,
    6 : 140
}

obszary_ciężarówka = {
    1 : 20,
    2 : 50,
    3 : 70,
    4 : 80
}

mandaty = {      ##pierwszy element listy dołączonej do klucza wskazuje wysokość mandatu, drugi element to ilość punktów karnych
    1 : [50, 1], ## przy przekroczeniu prędkości do 10 km/h, 
    2 : [100, 2], ## przy przekroczeniu prędkości o 11-15 km/h
    3 : [200, 3], ## przy przekroczeniu prędkości o 16-20 km/h
    4 : [300, 5], ## przy przekroczeniu prędkości o 21-25 km/h
    5 : [400, 7], ## przy przekroczeniu prędkości o 26-30 km/h
    6 : [800, 9], ## przy przekroczeniu prędkości o 31-40 km/h, w przypadku recydywy trzeba wprowadzić funkcjonalność, która będzie mnożyć wysokość mandatu razy 2
    7 : [1000, 11], ## przy przekroczeniu prędkości o 41-50 km/h, w przypadku recydywy trzeba wprowadzić funkcjonalność, która będzie mnożyć wysokość mandatu razy 2
    8 : [1500, 13], ## przy przekroczeniu prędkości o 51-60 km/h, w przypadku recydywy trzeba wprowadzić funkcjonalność, która będzie mnożyć wysokość mandatu razy 2
    9 : [2000, 14], ## przy przekroczeniu prędkości o 61-70 km/h, w przypadku recydywy trzeba wprowadzić funkcjonalność, która będzie mnożyć wysokość mandatu razy 2
    10 : [2500, 15] ## przy przekroczeniu prędkości powyżej 71 km/h, w przypadku recydywy trzeba wprowadzić funkcjonalność, która będzie mnożyć wysokość mandatu razy 2
}


## ---- FUNKCJE ---- ##

def obliczanie_kary_osobówka(v, obszar, obszary_osobówka, mandaty):

    różnica_osobówka = v - obszary_osobówka[obszar]

    if różnica_osobówka <= 0:
        return 0, 0, różnica_osobówka, 0
    elif różnica_osobówka > 0 and różnica_osobówka <= 10:
        return mandaty[1][0], mandaty[1][1], różnica_osobówka, 1
    elif różnica_osobówka >= 11 and różnica_osobówka <= 15:
        return mandaty[2][0], mandaty[2][1], różnica_osobówka, 2
    elif różnica_osobówka >= 16 and różnica_osobówka <= 20:
        return mandaty[3][0], mandaty[3][1], różnica_osobówka, 3
    elif różnica_osobówka >= 21 and różnica_osobówka <= 25:
        return mandaty[4][0], mandaty[4][1], różnica_osobówka, 4
    elif różnica_osobówka >= 26 and różnica_osobówka <= 30:
        return mandaty[5][0], mandaty[5][1], różnica_osobówka, 5
    elif różnica_osobówka >= 31 and różnica_osobówka <= 40:
        return mandaty[6][0], mandaty[6][1], różnica_osobówka, 6
    elif różnica_osobówka >= 41 and różnica_osobówka <= 50:
        return mandaty[7][0], mandaty[7][1], różnica_osobówka, 7
    elif różnica_osobówka >= 41 and różnica_osobówka <= 50:
        return mandaty[8][0], mandaty[8][1], różnica_osobówka, 8
    elif różnica_osobówka >= 61 and różnica_osobówka <= 70:
        return mandaty[9][0], mandaty[9][1], różnica_osobówka, 9
    else:
        return mandaty[10][0], mandaty[10][1], różnica_osobówka, 10


def obliczanie_kary_ciężarówka(v, obszar, obszary_ciężarówka, mandaty):

    różnica_ciężarówka = v - obszary_ciężarówka[obszar]
    
    if różnica_ciężarówka <= 0:
        return 0, 0, różnica_ciężarówka, 0
    elif różnica_ciężarówka > 0 and różnica_ciężarówka <= 10:
        return mandaty[1][0], mandaty[1][1], różnica_ciężarówka, 1
    elif różnica_ciężarówka >= 11 and różnica_ciężarówka <= 15:
        return mandaty[2][0], mandaty[2][1], różnica_ciężarówka, 2
    elif różnica_ciężarówka >= 16 and różnica_ciężarówka <= 20:
        return mandaty[3][0], mandaty[3][1], różnica_ciężarówka, 3
    elif różnica_ciężarówka >= 21 and różnica_ciężarówka <= 25:
        return mandaty[4][0], mandaty[4][1], różnica_ciężarówka, 4
    elif różnica_ciężarówka >= 26 and różnica_ciężarówka <= 30:
        return mandaty[5][0], mandaty[5][1], różnica_ciężarówka, 5
    elif różnica_ciężarówka >= 31 and różnica_ciężarówka <= 40:
        return mandaty[6][0], mandaty[6][1], różnica_ciężarówka, 6
    elif różnica_ciężarówka >= 41 and różnica_ciężarówka <= 50:
        return mandaty[7][0], mandaty[7][1], różnica_ciężarówka, 7
    elif różnica_ciężarówka >= 41 and różnica_ciężarówka <= 50:
        return mandaty[8][0], mandaty[8][1], różnica_ciężarówka, 8
    elif różnica_ciężarówka >= 61 and różnica_ciężarówka <= 70:
        return mandaty[9][0], mandaty[9][1], różnica_ciężarówka, 9
    else:
        return mandaty[10][0], mandaty[10][1], różnica_ciężarówka, 10


def czy_recydywa(wykroczenie, kara):

    numery = [6, 7, 8, 9, 10] ## Numery wykroczeń ze słownika "mandaty", za które mandat jest naliczany podwójnie w przypadku recydywy.

    if wykroczenie in numery:
        return kara * 2


def oc(rok, miesiąc, dzień, typ_pojazdu): 
    ## Funkcja potrzebna do obliczenia czy został przekroczony termin OC. 
    ## W przypadku jego przekroczenia musimy doliczyć wartość kary za brak OC do łącznej wysokości mandatu.
    ## Funkcja zwraca tuple składający się z wartości bezwględnej różnicy, która w przypadku braku OC będzie ujemna. 
    ## Musimy więc za pomocą funkcji abs zwrócić różnicę w formie dodatniej przez podanie wartości bezwględnej różnicy.
    ## Będzie to potrzebne do wyświetlenia komunikatu odnośnie tego o ile wysokość mandatu została podniesiona w przypadku braku OC. 
    
    today = date.today()

    oc_termin = date(rok, miesiąc, dzień)

    różnica_dat = oc_termin - today

    if różnica_dat.days >= 0:
        return różnica_dat.days, 0
    elif różnica_dat.days < 0 and różnica_dat.days >= -3:
        if typ_pojazdu == 1:
            return różnica_dat.days, 1200
        elif typ_pojazdu == 2:
            return różnica_dat.days, 1810
    elif różnica_dat.days <= -4 and różnica_dat.days > -14:
        if typ_pojazdu == 1:
            return różnica_dat.days, 3010
        elif typ_pojazdu == 2:
            return różnica_dat.days, 4520
    else:
        if typ_pojazdu == 1:
            return różnica_dat.days, 6020
        elif typ_pojazdu == 2:
            return różnica_dat.days, 9030


## ---- WŁAŚCIWY PROGRAM ---- ##

total = 0 ## Łączna wartość mandatu
punkty = 0 ##Łączna liczba punktów karnych
start = True ## Potrzebny do zrobienia pętli służącej do uruchomienia programu

while start:
    print("Witaj w Nowym Taryfikatorze Mandatów.\nPomożemy Ci sprawdzić wysokość mandatu.")

    try:
        v = int(input("\nPodaj prędkość z jaką jechałeś: "))
    except:
        print("Podaj wartość używając tylko liczb.")

    print("Określ typ samochodu jakim się poruszałeś. Wybierz jedną z dostępnych opcji:")

    sprawdzenie_pojazdu = True

    while sprawdzenie_pojazdu:
        try:
            typ_pojazdu = int(input("\n1. Pojazd o masie do 3.5 tony (wpisz 1)\n2. Pojazd o masie powyżej 3.5 tony (wpisz 2)\n"))
            if typ_pojazdu >=3 or typ_pojazdu <= 0:
                print("\nNieprawidłowa wartość! Wpisz 1 lub 2.")
                sprawdzenie_pojazdu
            else:
                sprawdzenie_pojazdu = False
        except:
            print("Nieprawidłowa wartość! Podaj wartość używając tylko liczb.")

    print("\nW jakim obszarze się poruszałeś? Wybierz jedną z dostępnych opcji:")
    
    sprawdzenie_obszaru = True
    wykroczenie = False
    while sprawdzenie_obszaru:
        if typ_pojazdu == 1:
            try:
                obszar = int(input("\n1. Strefa zamieszkania (wpisz 1)\n2. Obszar zabudowany (wpisz 2)\n3. Pozostałe drogi (wpisz 3)\n4. Droga ekspresowa jednojezdniowa lub drogra dwujezdniowa z co najmniej dwoma pasami ruchu przeznaczonymi do jazdy dla każdego kierunku (wpisz 4)\n5. Droga ekspresowa dwujezdniowa (wpisz 5)\n6. Autostrada (wpisz 6)\n"))
                if obszar > 6 or obszar <= 0:
                    print("Nieprawidłowa wartość! Podaj wartość odpowiadającą jednej z podanych liczb.")
                    sprawdzenie_obszaru
                else:
                    ## ---- SPRAWDZENIE WYSOKOŚCI MANDATU DLA SAMOCHODU OSOBOWEGO ---- ##
                    kara_osobówka = obliczanie_kary_osobówka(v, obszar, obszary_osobówka, mandaty)
                    if kara_osobówka[2] <= 0:
                        print("Nie popełniono wykroczenia.")
                    else:
                        wykroczenie = True
                        total += kara_osobówka[0]
                        punkty += kara_osobówka[1]
                        print(f"\nPrzekroczono prędkość o {kara_osobówka[2]}km/h. Obecna wartość mandatu: {total} PLN. Naliczono {punkty} punktów karnych.")  
                    sprawdzenie_obszaru = False
            except:
                print("Nieprawidłowa wartość! Podaj wartość używając tylko liczb.")
        else:
            try: 
                obszar = int(input("\n1. Strefa zamieszkania (wpisz 1)\n2. Obszar zabudowany (wpisz 2)\n3. Pozostałe drogi (wpisz 3)\n4. Droga dwujezdniowa z 2 pasami w każdą stronę, droga ekspresowa jedno- lub dwujezdniowa, autostrada (wpisz 4)\n"))
                if obszar > 4 or obszar <= 0:
                    print("Nieprawidłowa wartość! Podaj wartość odpowiadającą jednej z podanych liczb.")
                    sprawdzenie_obszaru
                else:
                    ## ---- SPRAWDZENIE WYSOKOŚCI MANDATU DLA SAMOCHODU CIĘŻAROWEGO ---- ##
                    kara_ciężarówka = obliczanie_kary_ciężarówka(v, obszar, obszary_ciężarówka, mandaty)
                    if kara_ciężarówka[2] <= 0:
                        print("Nie popełniono wykroczenia.")
                    else:
                        wykroczenie = True
                        total += kara_ciężarówka[0]
                        punkty += kara_ciężarówka[1]
                        print(f"\nPrzekroczono prędkość o {kara_ciężarówka[2]}km/h. Obecna wartość mandatu: {total} PLN. Naliczono {punkty} punktów karnych.")
                    sprawdzenie_obszaru = False
            except:
                print("Nieprawidłowa wartość! Podaj wartość używając tylko liczb.")
        

    ## ---- SPRAWDZENIE RECYDYWY TYLKO W PRZYPADKU GDY NASTĄPIŁO WYKROCZENIE---- ##

    if wykroczenie == True:
        print("Czy popełniłeś to wykroczenie wcześniej?")
        sprawdzenie_recydywy = True
        while sprawdzenie_recydywy:
            try:
                recydywa = int(input("\nTAK (wpisz 1)\nNIE (wpisz 2)\n"))
                if recydywa > 2 or recydywa <= 0:
                    print("Nieprawidłowa wartość! Wpisz 1 lub 2.")
                    sprawdzenie_recydywy
                else:
                    if recydywa == 1 and typ_pojazdu == 1:
                        dodatkowa_należność = czy_recydywa(kara_osobówka[3], total)
                        if dodatkowa_należność != None:
                            total = dodatkowa_należność
                            print(f"W związku z recydywą naliczono dodatkowe opłaty. Obecna wysokość mandatu wynosi {total}. Naliczono {punkty} punktów karnych.")
                            sprawdzenie_recydywy = False
                        else:
                            sprawdzenie_recydywy = False
                    elif recydywa == 1 and typ_pojazdu == 2:
                        dodatkowa_należność = czy_recydywa(kara_ciężarówka[3], total)
                        print(dodatkowa_należność)
                        if dodatkowa_należność != None:
                            total = dodatkowa_należność
                            print(f"W związku z recydywą naliczono dodatkowe opłaty. Obecna wysokość mandatu wynosi {total}. Naliczono {punkty} punktów karnych.")
                            sprawdzenie_recydywy = False
                        else:
                            sprawdzenie_recydywy = False
                    else:
                        sprawdzenie_recydywy = False
            except:
                print("Nieprawidłowa wartość! Podaj wartość używając tylko liczb.")

    ## ---- SPRAWDZENIE OC ---- ##

    print("\nTo już prawie koniec. ;)\nTeraz przystąpimy do sprawdzenia ważności twojej polisy OC, gdyż może to mieć wpływ na wysokość mandatu.")

    sprawdzenie_roku = True

    while sprawdzenie_roku:
        try:
            rok = int(input("\nWpisz rok ważności polisy: "))
            if len(str(rok)) != 4 :
                print("Nieprawidłowa wartość! Podaj poprawny rok.")
                sprawdzenie_roku
            else:
                sprawdzenie_roku = False
        except:
            print("Nieprawidłowa wartość! Podaj wartość używając tylko liczb.")

    sprawdzenie_miesiąca = True
    while sprawdzenie_miesiąca:
        try:
            miesiąc = int(input("\nWpisz miesiąc ważności polisy: "))
            if  miesiąc >= 13 or miesiąc <= 0:
                print("Nieprawidłowa wartość! Podaj poprawny miesiąc.")
                sprawdzenie_miesiąca
            else:
                sprawdzenie_miesiąca = False
        except:
            print("Nieprawidłowa wartość! Podaj wartość używając tylko liczb.")
            
    sprawdzenie_dnia = True
    while sprawdzenie_dnia:
        try:
            dzień = int(input("\nWpisz dzień ważności polisy: "))
            if dzień > 31 or dzień < 1:
                print("Nieprawidłowa wartość! Podaj poprawny dzień.")
                sprawdzenie_dnia
                if miesiąc == 2 and dzień > 29 or dzień < 1:
                    print("Wprowadź poprawną ilość dni dla miesiąca 'luty'.")
                    sprawdzenie_dnia
            else:
                sprawdzenie_dnia = False
        except:
            print("Nieprawidłowa wartość! Podaj wartość używając tylko liczb.")

    oc_wynik = oc(rok, miesiąc, dzień, typ_pojazdu)

    ## Jeżeli różnica_oc w funkcji oc() jest mniejsza od 0 to jest to równoważne z tym, że total musi być powiększony o wartość kary za brak OC.
    ## Za pomocą poniższej instrukcji warunkowej możemy poinformować użytkownika o ile wysokość mandatu została zwiększona.
    if oc_wynik[0] >= 0:
        print("Posiadasz ważne OC.")
        sprawdzenie_dnia = False
    else: 
        total += oc_wynik[1]
        if oc_wynik[0] == -1:
            print(f"Wysokość mandatu została powiększona o {oc_wynik[1]}, gdyż ważność OC upłynęła wczoraj.")
        elif oc_wynik[0] <= -2:
            print(f"Wysokość mandatu została powiększona o {oc_wynik[1]}, gdyż ważność OC upłynęła {abs(oc_wynik[0])} dni temu.")

## ---- PODSUMOWANIE ---- ##

    if total == 0:
        print("Nie naliczono żadnych należności. Jechałeś poprawnie.")
        print("Czy chcesz obliczyć ponownie?")
        wybór = int(input("\nTAK (wpisz 1)\nNIE (wpisz 2)"))
        if wybór == 1:
            start
        else:
            start = False
    elif total > 0 and typ_pojazdu == 1:
        print(f"Łączna wysokość mandatu wynosi {total} PLN. Naliczono {punkty} punktów karnych.")
        print("Czy chcesz obliczyć ponownie?")
        wybór = int(input("\nTAK (wpisz 1)\nNIE (wpisz 2)\n"))
        if wybór == 1:
            start
        else:
            start = False
    else:
        print(f"Łączna wysokość mandatu wynosi {total} PLN. Naliczono {punkty} punktów karnych.")
        print("Czy chcesz obliczyć ponownie?")
        wybór = int(input("\nTAK (wpisz 1)\nNIE (wpisz 2)\n"))
        if wybór == 1:
            start
        else:
            start = False