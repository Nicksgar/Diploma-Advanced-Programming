<?php
/**
 * Basics of PDO - PDOCONNECT
 *
 *
 * Filename:        pdoConnect
 * Location:        /session-04
 * Date Created:    2024-08-07
 *
 * Author:          NS
 *
 */

require_once 'config.php';

$dsn = "mysql:host=$dbHost;dbname=$dbName;charset=UTF8";
# now will have a variable pdo which will alow to access database
try {
    $pdo = new PDO($dsn, $dbUser, $dbPass);
# if pdo is not null - display a nice message
    if ($pdo) {
        echo "Connected to the $dbName database successfully!";
    }
} catch (PDOException $e) {
    echo $e->getMessage();
}