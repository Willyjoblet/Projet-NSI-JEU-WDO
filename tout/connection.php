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
    <?php 
        if(isset($_POST['boutton_inscription'])){
            //si connecter
            //connection DBB
            include "connection_bdd.php";
            $req = mysqli_query($con, "INSERT INTO Joueurs VALUES (NULL, '$pseudo')");
            
        }else{
            echo "connection echoue"
        }
    
    ?>
    <section>
        <h1>CONNECTION</h1>
        <form action="" method="POST">
            <label for="pseudo1">Pseudo du Joueur 1 :</label>
            <input type="text" id="pseudo1" name="pseudo1" required>
            <label for="pseudo2">Pseudo du Joueur 2 :</label>
            <input type="text" id="pseudo2" name="pseudo2" required>
            <input type="submit" value = "Connection" name="boutton_inscription">
        </form>
    </section>
</body>
</html>
