<!DOCTYPE html>
<html>
<head>
	<title>B0-P1 access point</title>
	<link rel="stylesheet" href="style.css">
</head>
<body>
	<?php include_once("Scripts.php") ?>
	<header>
		<h1><span id="robot-name">B0-P1</span> access point</h1>
		<h2> < un robot autonome pour explorer de nouveaux horizons > </Un></h2>
	</header>
	<main>
		<div class="left-column">
			<div class="blackbox">
				<h3>Retour caméra</h3>
				<p>La caméra est en cours de chargement...</p>
			</div>
			<div>
				<?php
					$file="/var/www/html/instruction.txt";
					if(isset($_POST['stop'])) {
						ecrire($file,"p");
					}
					if(isset($_POST['avancer'])) {
						ecrire($file,"z");
					}
					if(isset($_POST['reculer'])) {
						ecrire($file,"s");
					}
					if(isset($_POST['gauche'])) {
						ecrire($file,"q");
					}
					if(isset($_POST['droite'])) {
						ecrire($file,"d");
					}
					if(isset($_POST['gauche 90°'])) {
						ecrire($file,"a");
					}
					if(isset($_POST['droite 90°'])) {
						ecrire($file,"e");
					}
					if(isset($_POST['accélérer'])) {
						ecrire($file,"r");
					}
					if(isset($_POST['ralentir'])) {
						ecrire($file,"f");
					}
				?>
			</div>
			<div class="blackbox" id="commandes-boutons">
				<form action="index.php" method="post">
					<h3>Commandes robot</h3>
					<div id="div-stop">
						<input type="submit" value="STOP" name="stop" id="stop">
					</div>
					<input type="submit" value="Avancer" name="avancer" id="avancer">
					<div id="div-boutons">
						<input type="submit" value="Gauche" name="gauche" id="gauche">
						<input type="submit" value="Droite" name="droite" id="droite">
					</div>
					<div id="div-boutons-90">
						<input type="submit" value="Gauche 90°" name="gauche 90°" id="gauche 90°">
						<input type="submit" value="Droite 90°" name="droite 90°" id="droite 90°">
					</div>
					<input type="submit" value="Reculer" name="reculer" id="reculer">
					<div id="div-boutons-vitesse">
						<input type="submit" value="Ralentir" name="ralentir" id="ralentir">
						<input type="submit" value="Accélérer" name="accélérer" id="accélérer">
					</div>
					<!--<button onclick="ecrire('/var/www/html/instruction.txt','test')">Test</button>-->
				</form>
			</div>
		</div>
		<div class="right-column">
			<div class="blackbox" id="info-robot">
				<h3>Infos robot</h3>
				<div>
					<p>speed : <span id="vitesse">0</span> km/h</p>
					<p>LED : <span id="LED_bool">OFF</span></p>
					<p>direction : <span id="direction">N/E</span></p>
				</div>
			</div>
			<div class="blackbox" id="commande-specifique">
				<div>
					<div id="logs">
						<p>></p>
						<p>></p>
						<p>></p>
						<p>></p>
						<p>></p>
						<p>></p>
						<p>></p>
						<p>></p>
						<p>></p>
						<p>></p>
					</div>
				<div>
					<input type="text" id="commande-texte" placeholder="Entrez votre commande ici">
					<button id="envoyer">Envoyer</button>
					<button type="button" onclick="updateData()">Montrer les données</button>
				</div>
			</div>
		</div>
	</main>

	<!--<script type="text/JavaScript">

		function envoiCommande($file,$instruction)
		{
			$handler = fopen($file,"w") or die("Unable to open file"); //Ouvre le fichier
			fwrite($handler, $instruction); //Ecrit l'instruction dans le fichier
			fclose($handler); //Ferme le fichier
    	
			// get the URL
			http = new XMLHttpRequest(); 
			http.open("GET", url, true);
			http.send(null);

			// prevent form from submitting
			return false;
		}

	</script>

<form action="" onsubmit="return submitCouponCode();">
   <input type="text" id="couponCode">
   <input type="submit" value="Apply">
</form>-->
	<script>
		function updateData() {
			var xhttp = new XMLHttpRequest();
			var url = "capteurs.json";
			xhttp.onreadystatechange = function() {
				if (this.readyState == 4 && this.status == 200) {
					var myCapteurs = JSON.parse(this.repsponseText)
					document.getElementById("LED-bool").innerHTML = myCapteurs["ultrason"];
					document.getElementById("vitesse").innerHTML = myCapteurs["vitesse"];
					document.getElementById("direction").innerHTML = myCapteurs["direction"];
					setTimeout(function(){updateData();}, 1000)
				}
			};
			xhttp.open("GET", url, true);
			xhttp.send();
		}

		<?php
			error_reporting(E_ALL);
			$data = $_POST['command'];
			$f = fopen('file.txt', 'w+');
			fwrite($f, $data);
			fclose($f);
		?>
	</script>

</body>
</html>
