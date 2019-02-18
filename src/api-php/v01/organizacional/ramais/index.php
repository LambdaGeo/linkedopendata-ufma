<?php 
$query = $_REQUEST["query"];

$url="https://script.google.com/macros/s/AKfycbzyE1ASRvk2-beaEyiNAnjclQ6a1bKfTZ05AXHDaiKQplHlpeXc/exec?query=" . $query;
$json = file_get_contents($url);
header('Content-type: application/json; charset=utf-8');
echo "$json";
?>

