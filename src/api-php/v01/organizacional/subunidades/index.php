<?php 
$pars = http_build_query($_REQUEST, '', '&amp;');


$url="https://script.google.com/macros/s/AKfycbzmkOMho1VJxvjFSceMjx4x4RplquRid1Dk_6hYa2Lnr2cFSUQu/exec?".$pars;

$json = file_get_contents($url);
header('Content-type: application/json; charset=utf-8');
echo "$json";

?>

