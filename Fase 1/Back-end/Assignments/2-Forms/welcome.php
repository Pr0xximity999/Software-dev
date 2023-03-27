<?php
$nameErr = $mailErr = "*";
if ((empty($_POST["name"]) || !preg_match("/^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$/", $_POST["mail"]) || empty($_POST["mail"]))) {
    if (empty($_POST["name"])) {
        $nameErr = "*Input is required";
    }
    if (!preg_match("/^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$/", $_POST["mail"])) {
        $mailErr = "*Mail is invalid";
    }
    if (empty($_POST["mail"])) {
        $mailErr = "*Input is required";
    }
    ?>
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
    </head>

    <body>
        <main>
            <form method="post" id="inputFields" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
                <label>Name:</label>
                <input type="text" name="name" id="name" value="<?php echo $_POST["name"];?>">
                <span class="error"><?php echo $nameErr ?></span>
                <br><br>
                <label>E-Mail</label>
                <input type="text" name="mail" id="mail" value="<?php echo $_POST["mail"];?>">
                <span class="error"><?php echo $mailErr ?></span>
                <br>
                <button>Submit</button>
            </form>
        </main>
    </body>

    </html>
    <?php
} else if ($_POST != [] && (!$_POST["name"]) || !empty("mail")) {
    function clean_input($data)
    {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }

    ?>
        Welcome
    <?php echo clean_input($_POST["name"]); ?><br>
        Your email address is:
    <?php echo clean_input($_POST["mail"]); ?>
    <?php
    }
?>