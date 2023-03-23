<?php
if($_POST != [])
{
    function clean_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
    
    ?>
    Welcome <?php echo clean_input($_POST["name"]); ?><br>
    Your email address is: <?php echo clean_input($_POST["mail"]); ?>
    <?php
}
else{?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <main>
            <form method="post" id="inputFields" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
                    <label>Name:</label>
                    <input type="text" name="name" id="name"><br><br>  
                    <label>E-Mail</label>
                    <input type="text" name="mail" id="mail"><br>
                    <button>Submit</button>
            </form>
        </main>
    </body>

</html>
<?php } ?>