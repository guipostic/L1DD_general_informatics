
import sys

sequence = sys.argv[1] # chaîne de caractère donnée au programme ; par exemple : "############1111########"
ruban = list(sequence) # convertir la chaîne de caractères en liste
position = ''.join(ruban).rindex('1') # trouver la position du 1 le plus à droite
state = "S3" # définition de l'état de début

print("Initial  ", end='')
print(''.join(ruban), position)

while state != "Halt":
    if state == "S1":
        if ruban[position] == "1":
            print("Règle 10 ", end='')
            ruban[position] = "0" # Erreur : 0 pas 1
            position-=1
            state = "S1"
        elif ruban[position] == "0":
            print("Règle 11 ", end='')
            ruban[position] = "1"
            position+=1
            state = "S5"
        elif ruban[position] == "#":
            print("Règle 12 ", end='')
            ruban[position] = "1"
            position+=1
            state = "S5"


    elif state == "S2":
        if ruban[position] == "#":
            print("Règle 04 ", end='')
            ruban[position] = "#"
            position-=1
            state = "S3"
        elif ruban[position] == "1":
            print("Règle 05 ", end='')
            ruban[position] = "1"
            position+=1
            state = "S2"


    elif state == "S3":
        if ruban[position] == "1":
            print("Règle 06 ", end='')
            ruban[position] = "#"
            position-=1
            state = "S4"
        elif ruban[position] == "#":
            print("Règle 09 ", end='')
            ruban[position] = "#"
            position+=1
            state = "Halt"


    elif state == "S4":
        if ruban[position] == "1":
            print("Règle 07 ", end='')
            ruban[position] = "1"
            position-=1
            state = "S4"
        elif ruban[position] == "#":
            print("Règle 08 ", end='')
            ruban[position] = "#"
            position-=1
            state = "S1"


    elif state == "S5":
        if ruban[position] == "1":
            print("Règle 01 ", end='')
            ruban[position] = "1"
            position+=1
            state = "S5"
        elif ruban[position] == "0":
            print("Règle 02 ", end='')
            ruban[position] = "0"
            position+=1
            state = "S5"
        elif ruban[position] == "#":
            print("Règle 03 ", end='')
            ruban[position] = "#"
            position+=1
            state = "S2"

    print(''.join(ruban), position)
        
