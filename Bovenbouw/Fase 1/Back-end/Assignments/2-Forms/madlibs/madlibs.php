<?php
require_once("once.php");
function clean_input($data)
{
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

$panicQuestions = array(
    "pName" => array("question" => "Wat is je naam?", "defaultValue" => "", "fieldError" => "*"),
    "pFavAnimal" => array("question" => "Wat is je lievelingsdier?", "defaultValue" => "", "fieldError" => "*"),
    "pFavLiquid" => array("question" => "Wat is je favoriete vloeistof?", "defaultValue" => "", "fieldError" => "*"),
    "pFavColor" => array("question" => "Wat is je favoriete kleur?", "defaultValue" => "", "fieldError" => "*"),
    "pToiletCount" => array("question" => "Hoe vaak ga je naar de wc op 1 dag?", "defaultValue" => "", "fieldError" => "*"),
    "pMilBought" => array("question" => "Als je 1 miljoen had en 1 ding kon kopen, wat zou je kopen?", "defaultValue" => "", "fieldError" => "*"),
);
$ignoranceQuestions = array(
    "iName" => array("question" => "Wat is je naam?", "defaultValue" => "", "fieldError" => "*"),
    "iBabyNum" => array("question" => "Hoeveel minuten per dag zit je op je telefoon?", "defaultValue" => "", "fieldError" => "*"),
    "iFavForestAnimal" => array("question" => "Wat is je favoriete bosdier?", "defaultValue" => "", "fieldError" => "*"),
    "iRandomObject" => array("question" => "Wat is het eerste object wat in je opkomt als ik supermarkt zeg", "defaultValue" => "", "fieldError" => "*"),
    "iFavBreadTopping" => array("question" => "Wat is je favoriete broodbeleg?", "defaultValue" => "", "fieldError" => "*"),
    "iFavPerson" => array("question" => "Wie is je favoriete Persoon?", "defaultValue" => "", "fieldError" => "*"),
    "iFavMusic" => array("question" => "Wat is je favoriete muzieknummer?", "defaultValue" => "", "fieldError" => "*"),
    "iFavTaste" => array("question" => "Wat is je favoriete smaak?", "defaultValue" => "", "fieldError" => "*"),
);
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $panicAllFieldsFilled = $ignoranceAllFieldsFilled = true;
    foreach ($_POST as $key => $value) {

        if($key[0] == "p"){
            $showPanicQuestions = true;
            $showIgnoranceQuestions = false;
        }
        elseif($key[0] == "i"){
            $showIgnoranceQuestions = true;
            $showPanicQuestions = false;
        }

        if($showPanicQuestions){
            $ignoranceAllFieldsFilled = false;
            $panicQuestions[$key]["defaultValue"] =  clean_input($value);

            if (empty($value)) {
                $panicAllFieldsFilled = false;
                $panicQuestions[$key]["fieldError"] = "*field required";
            } else {
                $panicQuestions[$key]["fieldError"] = "";
            }
        }
        else if($showIgnoranceQuestions){
            $panicAllFieldsFilled = false;
            $ignoranceQuestions[$key]["defaultValue"] = clean_input($value);
            if (empty($value)) {
                $ignoranceAllFieldsFilled = false;
                $ignoranceQuestions[$key]["fieldError"] = "*field required";
            } else {
                $ignoranceQuestions[$key]["fieldError"] = "";
            }
        }
    }
    if ($panicAllFieldsFilled) {
        $showPanicQuestions = false;
        $showPanicAwnser = true;
    }
    if ($ignoranceAllFieldsFilled) {
        $showIgnoranceQuestions = false;
        $showIgnoranceAwnser = true;
    }
}
elseif($_SERVER["REQUEST_METHOD"] == "GET"){
    if(array_key_exists('panic', $_GET)){
        $showPanicQuestions = true;
        $showIgnoranceQuestions = false;
    }
    if(array_key_exists('ignorance', $_GET)){
        $showPanicQuestions = false;
        $showIgnoranceQuestions = true;
    }
}
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="./Styling/style.css">
</head>

<body>
    <main id="main">
        <header id="nav">
            <form action="madlibs.php" method="get">
                <input type="submit" name="panic" class="navBtns" value="Er heerst paniek...">
                <input type="submit" name="ignorance" class="navBtns" value="Onkunde">
            </form>
        </header>
        <div id="mainDiv">
            <?php if ($showPanicQuestions) {
                require("./panic/panic_questions.php");
            } elseif($showPanicAwnser) {
                require("./panic/panic_result.php");
            }

            if($showIgnoranceQuestions){
                require("./ignorance/ignorance_questions.php");
            }
            elseif($showIgnoranceAwnser){
                require("./ignorance/ignorance_result.php");
            }
            ?>
        </div>
    </main>
    <?php include("madlibs_footer.php"); ?>
</body>

</html>