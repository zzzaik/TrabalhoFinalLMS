<?php
$Usuario = "postgres";
$Senha = "LMS_GP_Draco";
$Host = "localhost";
$Database = "DB_LMS";
$PORT = '8000';

if (postgresql_connect($Host, $Usuario, $Senha)){
    postgresql_select_db($Database);
    }
?>