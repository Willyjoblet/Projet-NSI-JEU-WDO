<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jeu de Cartes</title>
    <link rel="stylesheet" href="CSS.css">
    <link rel="icon" type="image/vnd.icon" href="https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Mark_of_the_United_States_Army.svg/640px-Mark_of_the_United_States_Army.svg.png">
</head>
<body>
    <section>
        <h1>Bienvenue dans le jeu de cartes</h1>
        <form action="config.php" method="POST">
            <label for="pseudo1">Pseudo du Joueur 1 :</label>
            <input type="text" id="pseudo1" name="pseudo1" required>
            <label for="pseudo2">Pseudo du Joueur 2 :</label>
            <input type="text" id="pseudo2" name="pseudo2" required>
            <button type="submit">Démarrer la Partie </button>
        </form>
    </section>
</body>
</html>
