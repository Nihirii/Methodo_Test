import datetime

def salutation():
    heure_actuelle = datetime.datetime.now().hour

    if 6 <= heure_actuelle < 12:
        return "Bonjour"
    elif 12 <= heure_actuelle < 18:
        return "Bon après-midi"
    else:
        return "Bonsoir"

def est_palindrome(phrase):
    phrase = phrase.lower().replace(" ", "")  # Ignorer les espaces et mettre en minuscules
    return phrase == phrase[::-1]  # Vérifier si la phrase est égale à son inverse

def main():
    print("Bienvenue !")
    print(salutation())  # Affiche "Bonjour", "Bon après-midi" ou "Bonsoir"

    while True:
        message = input("Veuillez saisir un message ('exit' pour quitter) : ")
        
        if message.lower() == 'exit':
            print("Au revoir !")
            break
        
        moment_de_la_journee = salutation()
        print(f"{moment_de_la_journee}, vous avez saisi : {message}")

        # Vérification si c'est un palindrome
        if est_palindrome(message):
            print("Bien dit!")

if __name__ == "__main__":
    main()
