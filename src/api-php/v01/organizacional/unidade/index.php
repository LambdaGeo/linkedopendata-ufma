<?php 
$pars = http_build_query($_REQUEST, '', '&amp;');


$url="https://dados-abertos-ufma.herokuapp.com/api/v01/unidades?".$pars;

$json = file_get_contents($url);
header('Content-type: application/json; charset=utf-8');
echo "$json";

?>
