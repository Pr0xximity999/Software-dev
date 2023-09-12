<?php
//Start the database connection and retrieve the data
require("./resources/php/init_db.php");
//Run the SQL query
$stmt = $conn->prepare("SELECT * FROM characters ORDER BY name ASC");
$stmt->execute();
require("./resources/php/pull_db.php");
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>All Characters</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <link href="resources/css/style.css" rel="stylesheet" />
</head>

<body>
    <header>
        <h1><?="Alle ".sizeof($data)." characters uit de database"?></h1>
    </header>
    <div id="container">
        <? foreach ($data as $key => $value) { ?>
        <a class="item" href="character.php?id=<?=$value['id']?>">
            <div class="left">
                <img class="avatar" src=<?="resources/images/".$value['avatar']?>>
            </div>
            <div class="right">
                <h2><?=$value['name']?></h2>
                <div class="stats">
                    <ul class="fa-ul">
                        <li><span class="fa-li"><i class="fas fa-heart"></i></span><?= $value["health"]?></li>
                        <li><span class="fa-li"><i class="fas fa-fist-raised"></i></span><?= $value["attack"]?></li>
                        <li><span class="fa-li"><i class="fas fa-shield-alt"></i></span><?= $value["defense"]?></li>
                    </ul>
                </div>
            </div>
            <div class="detailButton"><i class="fas fa-search"></i> bekijk</div>
        </a>
        <? } ?>
    </div>
    </form>
    <?php include("./resources/php/footer.php") ?>
</body>
</html>
<?
//Close connection
$conn = null;