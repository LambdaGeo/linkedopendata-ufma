<?php 

$pars = http_build_query($_REQUEST);

$url="https://script.google.com/macros/s/AKfycbyNnv_noQEaUkdScNzYYGqjE9zvNnsKP-kZIIXnQiLuD1fTrJI/exec?" . $pars;
$json = file_get_contents($url);
header('Content-type: application/json; charset=utf-8');
echo "$json";

?>

