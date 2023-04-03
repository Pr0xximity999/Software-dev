<h1 id="title">Onkunde</h1>
<form action="madlibs.php" method="post">
    <?php
    foreach ($ignoranceQuestions as $questionID => $question) { ?>
        <div class="questionDiv">
            <label class="questionLabel">
                <? echo $question["question"] ?>
            </label>
            <div>
                <span class="fieldError">
                    <?php echo $question["fieldError"] ?>
                </span>
                <input class="questionInput" type="text" name=<?php echo $questionID ?> value=<?php echo $question["defaultValue"] ?>>
            </div>
        </div><br>
    <?php }
    ?>
    <button id="submitBtn">Versturen</button>
</form>