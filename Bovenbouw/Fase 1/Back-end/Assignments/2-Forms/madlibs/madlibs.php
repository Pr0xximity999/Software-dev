<?php
$showPanicQuestions = true;
//The questions used in the panic madlib
$panicQuestions = array(
    "name" => array("question" => "Wat is je naam?", "defaultValue" => "", "fieldError" => "*"),
    "favAnimal" => array("question" => "Wat is je lievelingsdier?", "defaultValue" => "", "fieldError" => "*"),
    "favLiquid" => array("question" => "Wat is je favoriete vloeistof?", "defaultValue" => "", "fieldError" => "*"),
    "favColor" => array("question" => "Wat is je favoriete kleur?", "defaultValue" => "", "fieldError" => "*"),
    "toiletCount" => array("question" => "Hoe vaak ga je naar de wc op 1 dag?", "defaultValue" => "", "fieldError" => "*"),
    "milBought" => array("question" => "Als je 1 miljoen had en 1 ding kon kopen, wat zou je kopen?", "defaultValue" => "", "fieldError" => "*"),
);
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    foreach ($_POST as $key => $value) {
        $panicAllFieldsFilled = true;
        $panicQuestions[$key]["defaultValue"] = $value;
        if (empty($value)) {
            $panicAllFieldsFilled = false;
            $panicQuestions[$key]["fieldError"] = "*field required";
        } else {
            $panicQuestions[$key]["fieldError"] = "";
        }

    }
    if ($panicAllFieldsFilled) {
        $showPanicQuestions = false;
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
            } else {
                require("./panic/panic_result.php");
            }
            ?>
        </div>
    </main>
    <?php include("madlibs_footer.php"); ?>
</body>

</html>