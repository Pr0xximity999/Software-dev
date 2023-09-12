<?php
//Start the database connection and retrieve the data
require("./resources/php/init_db.php");
//Run the SQL query
$stmt = $conn->prepare("SELECT * FROM characters WHERE id=".$_GET['id']);
$stmt->execute();
require("./resources/php/pull_db.php");
$character = $data[0];
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title><?="Character - ".$character['name']?></title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <link href="resources/css/style.css" rel="stylesheet"/>
</head>
<body>
<header><h1><?=$character['name']?></h1>
    <a class="backbutton" href="index.php"><i class="fas fa-long-arrow-alt-left"></i> Terug</a></header>
<div id="container">
    <div class="detail">
        <div class="left">
            <img class="avatar" src=<?="resources/images/".$character['avatar']?>>
            <div class="stats" style="background-color:<?=$character['color']?>">
                <ul class="fa-ul">
                    <li><span class="fa-li"><i class="fas fa-heart"></i></span> <?=$character['health']?></li>
                    <li><span class="fa-li"><i class="fas fa-fist-raised"></i></span> <?=$character['attack']?></li>
                    <li><span class="fa-li"><i class="fas fa-shield-alt"></i></span> <?=$character['defense']?></li>
                </ul>
                <ul class="gear">
                    <li><b>Weapon</b>: <?=$character['weapon']?></li>
                    <? 
                    if(isset($character['armor'])){
                        echo "<li><b>Armor</b>:".$character['armor'];
                    }
                    ?></li>
                </ul>
            </div>
        </div>
        <div class="right">
            <p>
                <?=$character['bio']?>
            </p>
        </div>
        <div style="clear: both"></div>
    </div>
</div>
<?php include("./resources/php/footer.php") ?>
</body>
</html>