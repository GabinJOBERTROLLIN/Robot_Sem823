<?php
    function lire($file){
        $handler = fopen($file,"r") or die("Unable to open file"); //Ouvre le fichier
        fread($handler,filesize($file)); //Lit l'intégralité du fichier
        fclose($handler); //Ferme le fichier
    }

    function ecrire($file,$instruction){
        $handler = fopen($file,"w") or die("Unable to open file"); //Ouvre le fichier
        fwrite($handler, $instruction); //Ecrit l'instruction dans le fichier
        fclose($handler); //Ferme le fichier
    }

    function ecrireFin($file,$instruction){
	$handler=fopen($file,"r+") or die("Unable to open file");
	$fileArray=file($file);
	if (count($fileArray)>9){
		$fileArray=array_slice($fileArray,-9);
	}
	array_push($fileArray,$instruction);
	foreach ($fileArray as $command){
		fwrite($handler,$command);
	}
	fclose($handler);
   }
?>
