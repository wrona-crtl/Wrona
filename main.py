import time
import random

hp_gracza = 10

while True:
    print('''
          
          
     !START       GRY!
       (menu glowne)
          
          
          ''')
    
    time.sleep(1)
    
    inp = input('''
    1. Walka
    2. Szukanie pozywienia
                
    ''')

    


    if inp == "1":
        while True:
            dmg_bossa = random.randint(1,8)
            hp_gracza -= dmg_bossa
            print("Przechodzisz do ataku")
            time.sleep(1)
            if hp_gracza < 0:
                print("Twoje hp spadlo ponizej 0, przegrales.")
                time.sleep(1)
                inp = input('''
                1. Zacznij gre od nowa.   
                            ''')
                if inp == "1":
                    hp_gracza = 10
                    break
                else:
                    print("blad, wracasz do menu")
                    break
                
            else:
                print(f"Brawo! Pokonales bossa, ale zadal ci on {dmg_bossa} hp i masz teraz {hp_gracza} hp ")
        
                inp = input('''
                    1. Atakuj Dalej
                    2. Powrot do menu


                ''')
                if inp == "1":
                    continue
                elif inp == "2":
                    break

    elif inp == "2":
        while True:
            print("Poszedles szukac pozywienia...")
            time.sleep(1)
            wynik_szukania = random.choices([True, False], weights=[65,35], k=1)[0]
            if wynik_szukania == True:
                leczenie = random.randint(1,3)
                hp_gracza += leczenie
                if hp_gracza > 10:
                    hp_gracza = 10
                print(f"Udalo ci sie znalesc pozywnienie i odzyskujesz {leczenie} hp ")
                time.sleep(2)
                print(f"Masz teraz {hp_gracza} hp")
                inp = input('''
                    1. Idz walczyc
                    ''')
                if inp == "1" :
                    dmg_bossa = random.randint(1,8)
                    hp_gracza -= dmg_bossa
                    print("Przechodzisz do ataku!")
                    time.sleep(1)
                    if hp_gracza < 0:
                        print("Masz 0 hp, przegrales.")
                        time.sleep(1)
                        inp = input('''
                            1. Zacznij gre od nowa.        
                                    ''')
                        if inp == 1:
                            hp_gracza = 10
                            break
                        else:
                            print("Blad, wracasz do menu")
                        
                        break
                    else:
                        print(f"Brawo! Pokonales bossa,ale zadal ci on {dmg_bossa}hp i masz teraz {hp_gracza}hp")

                        inp = input('''
                            1. Atakuj dalej      
                                2. Powrot do menu
                                
                                    ''')
                        if inp == "1":
                            continue
                        elif inp == "2":
                            break
                    
                else:
                    print("blad")
                    
                
            else:
                print("Nie udalo ci sie znalesc pozywienia")
                inp == input('''
                1. Ponownie szukaj pozywienia
                2. Walcz             
                            
                            ''')
                if inp == "1":
                    continue

                elif inp == "2":
                    break
        
                

            
        

        else:
            print("nieznana komenda")