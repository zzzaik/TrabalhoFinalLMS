<?php
include("db.php");

$consulta = postgresql_query("SELECT * FROM arquivo_resposta ORDER BY arquivo_resposta ASC");
if ($resultado = postgresql_fetch_array($consulta)){
    do {
        echo "<a href=\"" . $resultado["arquivos"] . $resultado["arquivo_resposta"] . "\">" . $resultado["arquivo_resposta"] . "</a><br />";
        }
    while($resultado = postgresql_fetch_array($consulta));
    }
?>