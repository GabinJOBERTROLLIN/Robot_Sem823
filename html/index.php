<!DOCTYPE html>
<html>
<head>
	<title>B0-P1 access point</title>
	<link rel="stylesheet" href="style.css">
</head>
<body>
	<?php
	include_once "Scripts.php"
	?>
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
					if(isset($_POST['stop'])) {
						echo "STOP";
						testPrint("STOP2");
					}
					if(isset($_POST['avancer'])) {
						echo "AVANCER";
						testPrint("AVANCER2");
					}
					if(isset($_POST['reculer'])) {
						echo "RECULER";
						testPrint("RECULER2");
					}
					if(isset($_POST['gauche'])) {
						echo "GAUCHE";
						testPrint("RECULER2");
					}
					if(isset($_POST['droite'])) {
						echo "DROITE";
						testPrint("DROITE2");
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
					<input type="submit" value="Reculer" name="reculer" id="reculer">
						<!-- <button id="stop">STOP</button>
					</div>
					<button id="avancer">Avancer tout droit</button>
					<div id="div-boutons">
						<button id="gauche">Tourner à gauche</button>
						<button id="droite">Tourner à droite</button>
					</div>
					<button id="reculer">Reculer</button> -->
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
				</div>
			</div>
		</div>
	</main>
</body>
</html>