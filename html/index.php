<!DOCTYPE html>
<html>
<head>
	<title>B0-P1 access point</title>
	<link rel="stylesheet" href="style3.css">
</head>
<body onload="update()">
	<?php include_once("Scripts.php") ?>
	<header>
		<h1><span id="robot-name">B0-P1</span> access point</h1>
		<h2> < un robot autonome pour explorer de nouveaux horizons > </Un></h2>
	</header>
	<main>
		<div class="pc left-column">
			<div>
				<?php
					$file="/var/www/html/instruction.txt";
					$log ="/var/www/html/log.txt";
					if(isset($_POST['stop'])) {
						ecrire($file,"p");
						ecrireFin($log,"Stop\n");
					}
					if(isset($_POST['avancer'])) {
						ecrire($file,"z");
						ecrireFin($log,"Avancer\n");
					}
					if(isset($_POST['reculer'])) {
						ecrire($file,"s");
						ecrireFin($log,"Reculer\n");
					}
					if(isset($_POST['gauche'])) {
						ecrire($file,"q");
						ecrireFin($log,"Gauche\n");
					}
					if(isset($_POST['droite'])) {
						ecrire($file,"d");
						ecrireFin($log,"Droite\n");
					}
					if(isset($_POST['gauche90'])) {
						ecrire($file,"a");
						ecrireFin($log,"Gauche 90\n");
					}
					if(isset($_POST['droite90'])) {
						ecrire($file,"e");
						ecrireFin($log,"Droite 90\n");
					}
					if(isset($_POST['accélérer'])) {
						ecrire($file,"r");
						ecrireFin($log,"Accélérer\n");
					}
					if(isset($_POST['ralentir'])) {
						ecrire($file,"f");
						ecrireFin($log,"Ralentir\n");
					}
					if(isset($_POST['clear'])) {
						ecrire($log,"");
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
						<input type="submit" value="Gauche 90°" name="gauche90" id="gauche90">
						<input type="submit" value="Droite 90°" name="droite90" id="droite90">
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


					<p>Vitesse : <span id="vitesse">0</span> km/h</p>
					<p>Obstacle : <span id="distance">OFF</span></p>
					<p>Chemin : <span id="chemin">N/E</span></p>
					<p>Actuel : <span id="actuel">0</span></p>

					<div class="pc blackbox">
                        		<a href="http://192.168.29.153:8081" target="_blank">
                                	<button>camera</button>
                        		</a></div>

				</div>
			</div>
			<div class="pc blackbox" id="commande-specifique">
				<div>
					<div id="logs">
						<p id="log9">></p>
						<p id="log8">></p>
						<p id="log7">></p>
						<p id="log6">></p>
						<p id="log5">></p>
						<p id="log4">></p>
						<p id="log3">></p>
						<p id="log2">></p>
						<p id="log1">></p>
						<p id="log0">></p>
					</div>
					<form action="index.php" method="post">
						<input type="submit" id="clear" name="clear" value="Clear">
					</form>
				</div>
			</div>
		</div>
	</main>

	<script>
		function update(){
			updateData();
			test();
		}
		function updateData() {
			var xhttp = new XMLHttpRequest();
			var url = "capteurs.json";
			xhttp.onreadystatechange = function() {
				if (this.readyState == 4 && this.status == 200) {
					var myCapteurs = JSON.parse(this.responseText);
					document.getElementById("distance").innerHTML = myCapteurs["ultrason"];
					document.getElementById("prochain").innerHTML = myCapteurs["prochain"];
					document.getElementById("vitesse").innerHTML = myCapteurs["vitesse"];
					document.getElementById("chemin").innerHTML = myCapteurs["chemin"];
					setTimeout(function(){updateData();}, 1000)
				}
			};
			xhttp.open("GET", url, true);
			xhttp.send();
		}
		<?php
			$logFile = "/var/www/html/log.txt";
			$handler = fopen($logFile,"r") or die("Unable to open log file");
			$commandArray = file($logFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
			$jsArray = json_encode($commandArray);
			echo "var jsCommandArray = ".$jsArray. ";\n";
		?>
		function test() {
			let i = 9;
			for (const x in jsCommandArray){
				document.getElementById("log"+i).innerHTML =">" + jsCommandArray[x];
				i = i-1;
			};
			while (i > 0) {
				document.getElementById("log"+i).innerHTML = ">";
				i = i-1;
			}
		}
	</script>
</body>
</html>

