<?php
$Usuario = "USUARIO";
$Senha = "SENHA";
$Host = "HOST";
$Database = "DB";

if (mysql_connect($Host, $Usuario, $Senha)){
    mysql_select_db($Database);
    }
?>