<?php
include("db.php");
if (isset($_FILES["Arquivo"])){
    $Arquivo = $_FILES["Arquivo"];
    $Pasta_Destino = "arquivos/";
    $Arquivo_Nome = $Arquivo['name'];
    move_uploaded_file($Arquivo['tmp_name'], $Pasta_Destino . $Arquivo_Nome);
    mysql_query("INSERT INTO `arquivos` (`arquivo_nome`,`arquivo_local`) VALUES ('$Arquivo_Nome','$Pasta_Destino')");
    header("Location: mostra_arquivos.php");
    }
	

?>