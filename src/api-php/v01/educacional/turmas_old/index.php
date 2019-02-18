<?php 
$siape = $_REQUEST["docente"];

$url="https://script.google.com/macros/s/AKfycbxjYbgBYlXU6-wGKXTcb58p52VKEoFqYsIeZ7rp4YhM5GhIafcU/exec?siape=" . $siape;
$json = file_get_contents($url);
header('Content-type: application/json; charset=utf-8');
echo "$json";
?>

