class Carte:
    def __init__(self, nom, type_carte, attaque, defense, energie):
        self.nom = nom
        self.type = type_carte
        self.attaque = attaque
        self.defense = defense
        self.energie = energie

    def __str__(self):
        return f"{self.nom} ({self.type}) - ATQ: {self.attaque}, DEF: {self.defense}, Énergie: {self.energie}"


class Joueur:
    def __init__(self, nom, deck):
        self.nom = nom
        self.deck = deck[:]  # Copie du deck
        self.main = []
        self.energie = 10
        self.score = 0
        self.cimetiere = []

    def piocher(self):
        if self.deck:
            carte = self.deck.pop(0)
            self.main.append(carte)
            print(f"{self.nom} pioche une carte : {carte.nom}")
        else:
            print(f"{self.nom} n'a plus de cartes à piocher !")

    def jouer_carte(self, index):
        if index < len(self.main):
            carte = self.main[index]
            if self.energie >= carte.energie:
                self.energie -= carte.energie
                print(f"{self.nom} joue {carte.nom} pour {carte.energie} énergie.")
                return self.main.pop(index)
            else:
                print(f"Pas assez d'énergie pour jouer {carte.nom}.")
        return None

    def regenerer_energie(self, montant=5):
        self.energie += montant
        print(f"{self.nom} regagne {montant} énergie (total: {self.energie}).")


def resoudre_combat(carte1, carte2):
    print(f"Combat entre {carte1.nom} et {carte2.nom}")
    if carte1.attaque > carte2.defense and carte2.attaque < carte1.defense:
        print(f"{carte1.nom} gagne le duel.")
        return 1
    elif carte2.attaque > carte1.defense and carte1.attaque < carte2.defense:
        print(f"{carte2.nom} gagne le duel.")
        return 2
    else:
        print("Égalité, les deux cartes sont détruites.")
        return 0


def jouer_tour(joueur1, joueur2):
    print("\n====== Nouveau tour ======")
    joueur1.piocher()
    joueur2.piocher()
    joueur1.regenerer_energie()
    joueur2.regenerer_energie()

    # Sélection automatique de la première carte jouable
    carte1 = next((joueur1.jouer_carte(i) for i in range(len(joueur1.main)) if joueur1.main[i].energie <= joueur1.energie), None)
    carte2 = next((joueur2.jouer_carte(i) for i in range(len(joueur2.main)) if joueur2.main[i].energie <= joueur2.energie), None)

    if carte1 and carte2:
        result = resoudre_combat(carte1, carte2)
        if result == 1:
            joueur1.score += 1
            joueur2.cimetiere.append(carte2)
        elif result == 2:
            joueur2.score += 1
            joueur1.cimetiere.append(carte1)
        else:
            joueur1.cimetiere.append(carte1)
            joueur2.cimetiere.append(carte2)
    else:
        print("Un des joueurs ne peut pas jouer de carte.")

    print(f"Score - {joueur1.nom}: {joueur1.score}, {joueur2.nom}: {joueur2.score}")
