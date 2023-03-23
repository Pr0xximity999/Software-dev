<?php
$servername = "mariaDB";
$username = "root";
$password = "mysql";
$dbname = "Batadase";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully";

    $query = mysqli_query("select * from tablename", $connection);



  } catch(PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
  }
  ?>