<?php
    date_default_timezone_set('Europe/Amsterdam');
    $hour = (int) date('H');
    $time = date('H:i:s');
    
    if($hour >= 6 && $hour < 12){
        echo '<img src="images\morning.png" alt="clock">';
        echo "<p>Goede Morgen!</p>";
        echo "<p class='time'> $time</p>"; 
    }
    if($hour >= 12 && $hour < 18){
        echo '<img src="images\afternoon.png" alt="clock">';
        echo "<p>Goede Middag!</p>";
        echo "<p class='time'> $time</p>"; 
    }
    if($hour >= 18 && $hour < 24){
        echo '<img src="images\evening.png" alt="clock">';
        echo "<p>Goede Avond!</p>";
        echo "<p class='time'> $time</p>"; 
    }
    if($hour >= 0 && $hour < 6){
        echo '<img src="images\night.png" alt="clock">';
        echo "<p class='white'>Goede Nacht!</p>";
        echo "<p class='time white'> $time</p>"; 
    }
    
    
?>
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>    
    </body>
</html>