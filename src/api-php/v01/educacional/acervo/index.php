<?php 

$pars = http_build_query($_REQUEST);

$url="https://script.google.com/macros/s/AKfycbyNMkmIHMvdpObLRlnuGA0ktE-Jd_GlomerV7XfmBuzQXQvs9os/exec?" . $pars;
$json = file_get_contents($url);
header('Content-type: application/json; charset=utf-8');
echo "$json";

?>

