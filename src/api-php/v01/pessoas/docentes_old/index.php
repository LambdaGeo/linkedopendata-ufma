<?php 
$nome = $_REQUEST["nome"];
$departamento = $_REQUEST["departamento"];

$url="https://script.google.com/macros/s/AKfycbyEfNvWitlEijpCSmidnguLxD-drkWbPD1Vq-WVX1gY_IdtDqw/exec?nome=" . $nome . "&departamento=" . $departamento;

$json = file_get_contents($url);
header('Content-type: application/json; charset=utf-8');
echo "$json";

?>

