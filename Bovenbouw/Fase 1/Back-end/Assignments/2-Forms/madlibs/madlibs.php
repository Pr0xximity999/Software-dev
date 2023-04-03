<?php
$showPanicQuestions = true;
$showPanicAwnser = false;
$showIgnoranceQuestions = false;
$showIgnoranceAwnser = false;

function clean_input($data)
{
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

//The questions used in the panic madlib
$panicQuestions = array(
    "name" => array("question" => "Wat is je naam?", "defaultValue" => "", "fieldError" => "*"),
    "favAnimal" => array("question" => "Wat is je lievelingsdier?", "defaultValue" => "", "fieldError" => "*"),
    "favLiquid" => array("question" => "Wat is je favoriete vloeistof?", "defaultValue" => "", "fieldError" => "*"),
    "favColor" => array("question" => "Wat is je favoriete kleur?", "defaultValue" => "", "fieldError" => "*"),
    "toiletCount" => array("question" => "Hoe vaak ga je naar de wc op 1 dag?", "defaultValue" => "", "fieldError" => "*"),
    "milBought" => array("question" => "Als je 1 miljoen had en 1 ding kon kopen, wat zou je kopen?", "defaultValue" => "", "fieldError" => "*"),
    "poop" => array("question" => "Als je 1 miljoen had en 1 ding kon kopen, wat zou je kopen?", "defaultValue" => "", "fieldError" => "*"),
);
$ignoranceQuestions = array(
    "name" => array("question" => "Wat is je naam?", "defaultValue" => "", "fieldError" => "*"),
);
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $panicAllFieldsFilled = $ignoranceAllFieldsFilled = true;
    foreach ($_POST as $key => $value) {
        if($showPanicQuestions){
            $panicQuestions[$key]["defaultValue"] =  clean_input($value);

            if (empty($value)) {
                $panicAllFieldsFilled = false;
                $panicQuestions[$key]["fieldError"] = "*field required";
            } else {
                $panicQuestions[$key]["fieldError"] = "";
            }
        }
        else if($showIgnoranceQuestions){
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
    if ($panicAllFieldsFilled) {
        $showPanicQuestions = false;
        $showPanicAwnser = true;
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
            <button class="navBtns">Er heerst paniek...</button>
            <button class="navBtns">Onkunde</button>
        </header>
        <div id="mainDiv">
            <?php if ($showPanicQuestions) {
                require("./panic/panic_questions.php");
            } elseif($showPanicAwnser) {
                require("./panic/panic_result.php");
            }
            ?>
        </div>
    </main>
    <?php include("madlibs_footer.php"); ?>
</body>

</html>