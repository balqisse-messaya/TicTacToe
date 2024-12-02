
def my_print_hello():
    print("Hello world")
my_print_hello()



name= "balqisse"
def My_print_name(nom) :
    print(nom)
My_print_name(name)



def Add( v1 , v2 ):
    somme = v1 + v2
    print("la somme de", v1, "et", v2, "est : ", somme)
Add( 2, 5)




def GetHello():
    print("Hello la Plateforme")
GetHello()




def calcule(num1, operator, num2):
    if operator == '+':
        return print(num1 + num2)
    elif operator == '-':
        return print(num1 - num2)
    elif operator == '*':
        return print(num1 * num2)
    elif  operator == '/' :
        return print(num1 / num2)
    elif operator == '%' : 
        return print(num1 % num2)

calcule(2, '+', 5) 
calcule(2, '-', 5)
calcule(2, '*', 5)
calcule(2, '/', 5)
calcule(2, '%', 5)



def verifier_nombre(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print ("negatif")

verifier_nombre(2)
verifier_nombre(-4)



def identifier(langage):
    if langage == "JavaScript":
        print("tu es un developpeur web")
    elif langage == "Python":
         print("tu est un developpeur IA")
    elif langage == "java":
        print("tu est un developpeur logiciel")
    elif langage == " reactjs":
         print("tu es un developpeur mobile")
    else:
        print("un jour, je serai le meilleur développeur")

identifier("JavaScript")
identifier("Python")
identifier("java")
identifier("reactjs")




    
note1 = int(input("Entrez la première note : "))
note2 = int(input("Entrez la deuxième note : "))
note3 = int(input("Entrez la troisième note : "))

def moyenne(note1, note2, note3):
    moyenne_etudiant = note1 + note2 + note3 /3

    if moyenne_etudiant <=20 and moyenne_etudiant >=15:
        print("très bon élève")
    elif moyenne_etudiant <=14 and moyenne_etudiant >=11:
        print("bon élève")
    elif moyenne_etudiant <=11 and moyenne_etudiant >=8:
        print("élève moyen")
    elif moyenne_etudiant <=7 and moyenne_etudiant >=0:
        print("élève devant faire des efforts")
    else:
        ("les notes saisies sont invalides")


    
def verifier_nombre(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print ("negatif")

verifier_nombre(2)
verifier_nombre(-5)

 


        



                                                                                     