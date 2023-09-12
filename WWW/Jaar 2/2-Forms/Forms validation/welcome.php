<?php    
    $nameErr = $mailErr = "*";
    $errors = [];
    $fields = ["name", "mail"];
    function clean_input($data)
    {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }

if (empty($_POST["name"])|| empty($_POST["mail"])  || !preg_match("/^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$/", $_POST["mail"])){

    if($_SERVER["REQUEST_METHOD"] == "POST"){
        foreach ($_POST as $key => $value) {
            if($key == "mail"){
                if (!preg_match("/^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$/", $key)) {
                    $errors[$key] = "*Mail is invalid";
                }
            }
            if(empty($value)){
                $errors[$key] = "*Input is required";
            }
        }
    }
    else{
        foreach ($fields as $key ) {
            $errors[$key] = "*";
        }
    }
    ?>
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="welcome_style.css">
    </head>

    <body>
        <main>
            <form method="post" id="inputFields" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"])?>">
                <?php 
                    foreach ($fields as $key) {?>
                        <label><?php $keyCap = strtoupper($key[0]) . substr($key, 1); echo $keyCap?>:</label>
                        <input type="text" name=<?php echo $key?> id=<?php echo $key?> value="<?php if($_SERVER["REQUEST_METHOD"] == "POST"){echo clean_input($_POST[$key]);}?>">
                        <span class="error"><?php echo $errors[$key]?></span>
                        <br><br>
                    <?php }
                ?>
                <button>Submit</button>
            </form>
        </main>
    </body>

    </html>
    <?php
} 
else{
    ?>
    Welcome
    <?php echo clean_input($_POST["name"]); ?><br>
        Your email address is:
    <?php echo clean_input($_POST["mail"]); ?>
    <?php
    }
?>