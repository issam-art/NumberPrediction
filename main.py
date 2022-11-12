from random import randint

bonne_reponse = randint(1, 10)

while True:
    tentative = int(input("Pour combien tu sors de cette boucle ? "))

    if tentative == bonne_reponse:
        print(f"Un... Deux... Trois: {tentative} ! Bravo, je te libère.")
        break

    elif tentative < bonne_reponse:
        print(f"Un... Deux... Trois: {tentative} ! Trop bas")

    elif tentative > bonne_reponse:
        print(f"Un... Deux... Trois: {tentative} ! Trop haut")