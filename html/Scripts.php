<?php
function lire($file){
$handler = fopen($file,"r") or die("Unable to open file"); //Ouvre le fichier
fread($handler,filesize($file)); //Lit l'intégralité du fichier
fclose($handler);
}

function ecrire($file,$instruction){
$handler = fopen($file,"w") or die("Unable to open file");
fwrite($handler, $instruction);
fclose($handler);
}

function testPrint($val){
    echo "$val"
}
?>