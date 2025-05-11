<?php

  //Connection DBB
  $con = mysqli_connect("'0504-srv-sig'","nsi_eleve8","nsi_eleve8","eleve8");
  //gerer caracters non UTF-8
  $req = mysqli_query($con , "SET NAMES UTF8");
  if(!$con){
    //si la connection echoue
    echo "Connectiuon echouee"
  }
?>
