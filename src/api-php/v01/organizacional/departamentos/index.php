<?php 

$url = "https://script.google.com/macros/s/AKfycbw3tgQUxsncrmz2MQXGaDtxmg56OOwq41LIR1QalQ39pul4G0gF/exec";
//; charset=utf-8'
$json = file_get_contents($url);
header('Content-type: application/json; charset=utf-8');
echo "$json";

?>

