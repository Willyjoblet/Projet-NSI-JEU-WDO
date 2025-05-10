import mysql.connector
import random

# Connexion à la base de données
def get_db_connection():
    return mysql.connector.connect(
        host='0504-srv-sig',
        database='nsi_eleve8',
        user='nsi_eleve8',
        password='eleve8'
    )

# Classe Joueur
class Joueur:
    def __init__(self, id, pseudo, deck, batiments_data):
        self.id = id
        self.pseudo = pseudo
        self.deck = deck  # Liste de cartes
        self.batiments = [Batiment(bat["nom"]) for bat in batiments_data]

# Classe Batiment
class Batiment:
    def __init__(self, nom):
        self.nom = nom
        self.points_de_vie = 200 if "Gauche" in nom or "Droite" in nom else 250  # Spécifique pour les bâtiments de gauche/droite et du centre

# Charger un joueur à partir de la base de données
class Combat
    def charger_joueur(pseudo):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
    
        # Requête pour obtenir les informations du joueur
        cursor.execute("SELECT * FROM Joueurs WHERE pseudo = %s", (pseudo,))
        joueur = cursor.fetchone()
    
        # Vérification si le joueur existe
        if joueur is None:
            raise Exception(f"Le joueur {pseudo} n'a pas été trouvé dans la base de données.")
        
        joueur_id = joueur["id"]
    
        # Récupérer le deck du joueur
        cursor.execute("""
            SELECT Cartes.id, Cartes.nom, Cartes.type, Cartes.degats, Cartes.protection
            FROM Decks
            JOIN Cartes ON Decks.carte_id = Cartes.id
            WHERE Decks.joueur_id = %s
        """, (joueur_id,))
        cartes = cursor.fetchall()
        random.shuffle(cartes)
    
        # Récupérer les bâtiments du joueur
        cursor.execute("""
            SELECT Batiments.nom
            FROM Batiments_Joueurs
            JOIN Batiments ON Batiments_Joueurs.batiment_id = Batiments.id
            WHERE Batiments_Joueurs.joueur_id = %s
            ORDER BY Batiments_Joueurs.id ASC
        """, (joueur_id,))
        batiments = cursor.fetchall()
    
        conn.close()
    
        # Retourner l'objet Joueur
        return Joueur(id=joueur_id, pseudo=joueur["pseudo"], deck=cartes, batiments_data=batiments)
    
    # Afficher l'état du jeu
    def afficher_etat_jeu(joueur1, joueur2):
        print(f"Début de la partie : {joueur1.pseudo} VS {joueur2.pseudo}")
        print(f"{joueur1.pseudo} a pour deck :")
        for carte in joueur1.deck:
            print(f"- {carte['nom']} ({carte['type']}) : {carte['degats']} dégâts / {carte['protection']} protection")
        print(f"Bâtiments de {joueur1.pseudo}:")
        for batiment in joueur1.batiments:
            print(f"- {batiment.nom} : {batiment.points_de_vie} PV")
    
        print(f"\n{joueur2.pseudo} a pour deck :")
        for carte in joueur2.deck:
            print(f"- {carte['nom']} ({carte['type']}) : {carte['degats']} dégâts / {carte['protection']} protection")
        print(f"Bâtiments de {joueur2.pseudo}:")
        for batiment in joueur2.batiments:
            print(f"- {batiment.nom} : {batiment.points_de_vie} PV")
    
    # Fonction pour lancer la partie
    def lancer_partie(pseudo1, pseudo2):
        try:
            joueur1 = charger_joueur(pseudo1)
            joueur2 = charger_joueur(pseudo2)
    
            afficher_etat_jeu(joueur1, joueur2)
    
        except Exception as e:
            print(f"Erreur : {e}")
    
    # Lancer la partie
    lancer_partie("Alpha", "Bravo")

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

