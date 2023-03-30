<h1 id="panicTitle">Er heerst paniek...</h1>
<form action="madlibs.php" method="post">
    <?php
    foreach ($panicQuestions as $questionID => $question) { ?>
        <div class="panicQuestionDiv">
            <label class="panicQuestionLabel">
                <? echo $question["question"] ?>
            </label>
            <div>
                <span class="fieldError">
                    <?php echo $question["fieldError"] ?>
                </span>
                <input class="panicQuestionInput" type="text" name=<?php echo $questionID ?> value=<?php echo $question["defaultValue"] ?>>
            </div>
        </div><br>
    <?php }
    ?>
    <button id="panicSubmitBtn">Versturen</button>
</form>