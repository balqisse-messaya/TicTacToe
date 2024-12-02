valeur1 = input("Entrez la première valeur : ")
valeur2 = input("Entrez la deuxième valeur : ")
if valeur1 == valeur2:
    print("valeur1 est égale à valeur2")
else:
    print("Les deux valeurs ne sont pas égales")

age = 15
if age >= 18 :
    print(" Tu peux voter ")
else :
    print(" Tu ne peux  pas voter ")

for i in range (101):
    if i not in[26, 37, 88]:
        print(i)
   


j = 0
while j < 100:
    if j % 3 == 0 and j % 5 == 0 :
        print("fizzBuzz")
    elif j % 3 == 0:
        print("fizz")
    elif j % 5 == 0:
        print("buzz")
    else:
        print(j)
    j += 1



for num in range(2, 1001):
    is_premier = True 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_premier = False
            break
    if is_premier:
        print(num)


nombre = int(input("Veuillez entrer un nombre pair : "))
if nombre % 2 == 0 :
    print(f"le nombre {nombre} est pair. ")
else:
    print(f"le nombre {nombre} est impair. ")














