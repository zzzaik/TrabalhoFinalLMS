<?php
include("db.php");

$consulta = mysql_query("SELECT * FROM `arquivos` ORDER BY `arquivo_nome` ASC");
if ($resultado = mysql_fetch_array($consulta)){
    do {
        echo "<a href=\"" . $resultado["arquivo_local"] . $resultado["arquivo_nome"] . "\">" . $resultado["arquivo_nome"] . "</a><br />";
        }
    while($resultado = mysql_fetch_array($consulta));
    }
?>