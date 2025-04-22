import mysql.connector
import random

# Connexion à la base
def get_db_connection():
    return mysql.connector.connect(
        host='0504-srv-sig',
        database='nsi_eleve8',
        user='nsi_eleve8',
        password='eleve8'
    )

class Carte:
    def __init__(self, id, nom, type, degats, protection, cout_energy):
        self.id = id
        self.nom = nom
        self.type = type
        self.degats = degats
        self.protection = protection
        self.cout_energy = cout_energy

    def __str__(self):
        return f"{self.nom} ({self.type}) - Dégâts: {self.degats}, Protection: {self.protection}, Coût: {self.cout_energy}"


class Joueur:
    def __init__(self, id, pseudo, deck, batiments):
        self.id = id
        self.pseudo = pseudo
        self.deck = [Carte(**c) for c in deck]
        self.batiments = batiments
        self.main = []
        self.energie = 10
        self.score = 0

    def piocher(self):
        if self.deck:
            carte = self.deck.pop(0)
            self.main.append(carte)
            print(f"{self.pseudo} pioche : {carte.nom}")
        else:
            print(f"{self.pseudo} n'a plus de cartes à piocher.")

    def jouer_carte(self):
        for i, carte in enumerate(self.main):
            if carte.cout_energy <= self.energie:
                self.energie -= carte.cout_energy
                print(f"{self.pseudo} joue {carte.nom} (énergie restante : {self.energie})")
                return self.main.pop(i)
        print(f"{self.pseudo} ne peut jouer aucune carte.")
        return None

    def regenerer_energie(self, montant=5):
        self.energie += montant
        print(f"{self.pseudo} regagne {montant} énergie (total: {self.energie}).")

def charger_joueur(pseudo):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Joueur
    cursor.execute("SELECT * FROM Joueurs WHERE pseudo = %s", (pseudo,))
    joueur = cursor.fetchone()
    if not joueur:
        raise Exception("Joueur introuvable")

    joueur_id = joueur["id"]

    # Deck
    cursor.execute("""
        SELECT Cartes.*
        FROM Decks
        JOIN Cartes ON Decks.carte_id = Cartes.id
        WHERE Decks.joueur_id = %s
    """, (joueur_id,))
    cartes = cursor.fetchall()
    random.shuffle(cartes)

    # Bâtiments
    cursor.execute("""
        SELECT Batiments.nom, Batiments_Joueurs.points_de_vie_restants
        FROM Batiments_Joueurs
        JOIN Batiments ON Batiments_Joueurs.batiment_id = Batiments.id
        WHERE Batiments_Joueurs.joueur_id = %s
    """, (joueur_id,))
    batiments = cursor.fetchall()

    conn.close()

    return Joueur(id=joueur_id, pseudo=joueur["pseudo"], deck=cartes, batiments=batiments)


# Combat

def simuler_combat(carte1, carte2):
    print(f"{carte1.nom} VS {carte2.nom}")
    if carte1.degats > carte2.protection and carte2.degats < carte1.protection:
        print(f"→ {carte1.nom} gagne")
        return 1
    elif carte2.degats > carte1.protection and carte1.degats < carte2.protection:
        print(f"→ {carte2.nom} gagne")
        return 2
    else:
        print("→ Égalité, les deux cartes sont détruites")
        return 0


def jouer_tour(j1, j2):
    print("\n===== Nouveau Tour =====")
    j1.piocher()
    j2.piocher()
    j1.regenerer_energie()
    j2.regenerer_energie()

    carte1 = j1.jouer_carte()
    carte2 = j2.jouer_carte()

    if carte1 and carte2:
        resultat = simuler_combat(carte1, carte2)
        if resultat == 1:
            j1.score += 1
        elif resultat == 2:
            j2.score += 1
    else:
        print("Un des joueurs n'a pas pu jouer.")

def lancer_partie(pseudo1, pseudo2):
    print(f"Lancement de la partie entre {pseudo1} et {pseudo2}")

    joueur1 = charger_joueur(pseudo1)
    joueur2 = charger_joueur(pseudo2)

    nb_tours = 5
    for _ in range(nb_tours):
        jouer_tour(joueur1, joueur2)

    print("Résultat final")
    print(f"{joueur1.pseudo}: {joueur1.score} | {joueur2.pseudo}: {joueur2.score}")

    if joueur1.score > joueur2.score:
        print(f"{joueur1.pseudo} gagne !")
    elif joueur2.score > joueur1.score:
        print(f"{joueur2.pseudo} gagne !")
    else:
        print("Match nul !")

if __name__ == "__main__":
    lancer_partie("Alpha", "Bravo")
