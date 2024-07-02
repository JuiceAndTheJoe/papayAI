from sklearn import tree
from matplotlib import pyplot as plt
from time import sleep

# features: [weight (g), 
#            texture (0 = hairy, 1 = smooth), 
#            color (7 = brown, 8 = purple, 9 = green)] 
# for each line

def readToList(a):
    a_file = open(a, "r")
    list_of_lists = []

    for line in a_file:
      stripped_line = line.strip()
      line_list = stripped_line.split()
      list_of_lists.append(line_list)
    a_file.close()

    return list_of_lists

#readToList läser en fil och returnar en lista av listor.

while True:

    #programmet körs i all oändlighet, här nedan kommer menyn och listan av val.

    print("********************")
    print("Fruktanalizator 3000")
    print()
    print("Alternativ:")
    print("1. Importera data & träna AI:t")
    print("2. Klassificera data")
    print("3. Skriv ut resultaten")
    print("4. Visa beslutsträdet")
    print("5. Avsluta programmet")
    print("")

    #frågar efter ett val, kör sedan koden för det alternativet.
    while True:
        try:
            val = int(input("Vad vill du göra? \n~ "))
            print()
            break
        except ValueError:
            print("xxxxxxxxxxxxxxx")
            print()
            print("Skriv en siffra")
            print()

    if val == 1:

        #frågar efter filnamnet för features, läser filen och visar värden.
        while True:
            try:
                feat = input("Var ligger dina features?\n~ ")
                retFeat = readToList(feat)
                break
            except FileNotFoundError:
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
                print("Se till att skriva ett filnamn")
                print()
        print(".")
        print(".")
        sleep(0.8)
        print("I", feat, "finns följande värden:")
        sleep(1.5)
        print(retFeat)
        print()

        #frågar efter filnamnet för labels, läser filen och visar värden.
        while True:
            try:
                lab = input("Var ligger dina labels?\n~ ")
                retLab = readToList(lab)
                break
            except FileNotFoundError:
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
                print("Se till att skriva ett filnamn")
                print()
        print(".")
        print(".")
        sleep(0.8)
        print("I", lab, "finns följande värden:")
        sleep(1.5)
        print(retLab)
        print()

        #användaren kan dubbelkolla om värdena stämmer, och valet görs om den vill träna AI:t med de importerade värdena.

        yn = input("Vill du träna AI:t med dessa värden? (ja/nej)\n~ ").lower()

        if yn == "ja":

            #om allt är OK från användarens sida, så skapas det ett träd och den tränas sedan med fit-funktionen.

            print()
            print("Tränar AI:t...")
            dtc = tree.DecisionTreeClassifier()
            trainedTree = dtc.fit(retFeat, retLab)

            #här används sleep för att markera att trädet har skapats och tränats utan problem.

            print(".")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            sleep(1)
            print("Klar.\n")
            print()
            sleep(1)

        else:
            print()
            print("Återvänder...")
            print()
            sleep(1)

    elif val == 2:

        #frågar efter filnamnet för filen som ska klassificeras, läser den och använder .predict() för att klassificera utifrån träningen
        while True:
            try:
                klass = input("Vad heter filen?\n~ ")
                retKlass = readToList(klass)
                print()
                sleep(1)
                print("Klassificerade resultat tagna utifrån", klass, ":")
                print()
                sleep(1)
                komp = str(trainedTree.predict(retKlass))
                print(trainedTree.predict(retKlass))
                print()
                break
            except FileNotFoundError:
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
                print("Se till att skriva ett filnamn")
                print()
                break
            except NameError:
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
                print("Se till att ha tränat AI:t först")
                print()
                break

    elif val == 3:

        #frågar efter filen att skriva resultaten på, skriver dem och deklarerar att allt är klart.
        while True:
            try:
                namn = input("Vart vill du skriva resultaten? (ex. \"xyz.txt\")\n~ ")
                print()
                sleep(1)
                print("Vill du skriva", komp, "i", namn, "?")
                janej = input("~").lower()

                if janej == "ja":
                    file = open(namn, 'a')
                    file.write(komp)
                    file.close()
                    print()
                    print("Dina resultat ligger nu sparade i", namn)
                    print()
                    sleep(1)
                    break
                elif janej == "nej":
                    print()
                    print("Återvänder...")
                    print()
                    sleep(1)
                    break
            except NameError:
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
                print("Du måste göra stegen i ordning, träna AI:t och klassificera data först.")
                print()
                sleep(2)
                break

    elif val == 4:
        while True:
            try:
                tree.plot_tree(trainedTree, rounded=True, filled=True)
                plt.show()
                break
            except NameError:
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
                print("Du måste göra stegen i ordning, träna AI:t och klassificera data först.")
                print()
                sleep(2)
                break

    elif val == 5:
        break
