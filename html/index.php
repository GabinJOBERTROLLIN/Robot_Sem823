<!DOCTYPE html>
<html>
<head>
	<title>B0-P1 access point</title>
	<link rel="stylesheet" href="style.css">
</head>
<body class="pc">
	<?php include_once("Scripts.php") ?>
	<header>
		<h1><span id="robot-name">B0-P1</span> access point</h1>
		<h2> < un robot autonome pour explorer de nouveaux horizons > </Un></h2>
	</header>
	<main>
		<div class="pc left-column">
			<div class="pc blackbox">
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
			<div class="pc blackbox" id="commandes-boutons">
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
				</form>
			</div>
		</div>
		<div class="pc right-column">
			<div class="pc blackbox" id="info-robot">
				<h3>Infos robot</h3>
				<div>
					<p>speed : <span id="vitesse">0</span> m/h</p>
					<p>LED : <span id="LED_bool">OFF</span></p>
					<p>direction : <span id="direction">N/E</span></p>
				</div>
			</div>
			<div class="pc blackbox" id="commande-specifique">
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

	<script>
		function updateData() {
			var xhttp = new XMLHttpRequest();
			xhttp.onreadystatechange = function() {
				if (this.readyState == 4 && this.status == 200) {
					document.getElementById("vitesse").innerHTML = this.responseText;
					setTimeout(function(){updateData();}, 1000)
				}
			};
			xhttp.open("GET", "vitesse.txt", true);
			xhttp.send();
		}
	</script>

</body>
<mobile>
	<h2>
		<p>B0-P1</p>
	</h2>
	<li>
		<btn-menu id="btn-menu-boutons">
			<img src="img/manette.png" class="icon-menu">
		</btn-menu>
		<btn-menu id="btn-menu-infos">
			<img src="img/rapport.png" class="icon-menu">
		</btn-menu>
		<btn-menu id="btn-menu-cam">
			<img src="img/camera.png" class="icon-menu">
		</btn-menu>
	</li>
	<div-boutons>
		<form action="index.php" method="post">
			<div id="div-rotate">
				<input type="submit" value="Avancer" name="avancer" id="avancer">
			</div>
			<div id="div-rotate">
				<input type="submit" value="Gauche" name="gauche" id="gauche">
				<input type="submit" value="STOP" name="stop" id="stop">
				<input type="submit" value="Droite" name="droite" id="droite">
			</div>
			<div id="div-rotate">
				<input type="submit" value="Reculer" name="reculer" id="reculer">
			</div>
			<p></p>
			<div id="div-boutons-90">
				<input type="submit" value="Gauche 90°" name="gauche 90°" id="gauche 90°">
				<input type="submit" value="Droite 90°" name="droite 90°" id="droite 90°">
			</div>
			<div id="div-boutons-vitesse">
				<input type="submit" value="Ralentir" name="ralentir" id="ralentir">
				<input type="submit" value="Accélérer" name="accélérer" id="accélérer">
			</div>
		</form>
	</div-boutons>
</mobile>
</html>
