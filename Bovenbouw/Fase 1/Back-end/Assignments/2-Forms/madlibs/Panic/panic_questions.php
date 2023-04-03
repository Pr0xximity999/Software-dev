<h1 id="title">Er heerst paniek...</h1>
<form action="madlibs.php" method="post">
    <?php
    foreach ($panicQuestions as $questionID => $question) { 
        $question["question"]
        ?>
        <div class="questionDiv">
            <label class="questionLabel">
                <?= $question["question"] ?>
            </label>
            <div>
                <span class="fieldError">
                    <?= $question["fieldError"] ?>
                </span>
                <input class="questionInput" type="text" name=<?= $questionID ?> value=<?= $question["defaultValue"] ?>>
            </div>
        </div><br>
    <?php }
    ?>
    <button id="submitBtn">Versturen</button>
</form>