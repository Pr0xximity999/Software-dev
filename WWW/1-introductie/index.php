<?php
echo "<h1> Hello world! </h1>";

define('Hello', 'Hello world! <br>');
echo Hello;

$hi = 'Learning PHP';
$hi = "Hello world";
echo $hi;

$hw1 = "<h1>Hello";
$hw2 = " world!</h1>";
echo $hw1, $hw2;

$hw = ['Hello', 'world!'];
echo implode($hw, ' ');