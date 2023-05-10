<?php 
  function deplacement(){  $myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
  $txt = "Mickey Mouse\n";}
?>

<?php
if(array_key_exists('deplacement', $_POST)) {
    deplacement();
}?>

<!doctype html>
<html lang="en">
  <head>
    <title>RBOT_SEM823</title>
    <script src="function.js"></script>
  </head>
  
  <body >
    <h1>Robot pour entrepot de stockage</h1>
    <input type = "button" onclick = "deplacement(value)" value = "UP">
  </body>
</html>
