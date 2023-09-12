<?php
//Define the database properties
$servername = "mariadb";
$username = "root";
$password = "mysql";
$dbname = "eindopdracht_db";
try {
    //Enstablish the connection
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    //Run the SQL query
    $stmt = $conn->prepare("SELECT * FROM characters ORDER BY name ASC");
    $stmt->execute();

} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}