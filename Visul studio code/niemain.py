print("a - plaskie b - bryły")
inp = input("a / b ?")
if "a" == inp:
   print('''
   a - pp kwadatu
   b - pp prostokata
   ...


   ''')
elif "b" == inp:
   print('''
   a - pp szescianu
   b - pp prostoadloscianu
   ...


   ''')
   inp = input("?")
   if inp == "a":
       a = float(input("a = "))
       print(f"ppSzecianu dla a={a} = {a**2*6}")   


else:
   print("Nie ma takiej komendy")