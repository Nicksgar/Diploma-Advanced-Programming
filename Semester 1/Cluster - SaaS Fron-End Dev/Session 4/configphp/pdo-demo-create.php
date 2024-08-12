<?php
/**
 * PDO DEMO
 *
 *
 * Filename:        pdo-demo-create
 * Location:        /session-04
 * Date Created:    2024-08-07
 *
 * Author:          NS
 *
 */

require_once "pdoConnect.php";

$sql = "INSERT INTO demo(name, colour, owned)"
    ."VALUES( :name, :colour, :owned)";

$statement = $pdo->prepare($sql);

$name = 'orville';
$colour = 'green';
$owned = 0; // Cannot use boolean FALSE - used in place of FALSE (1 = TRUE)

$statement->execute([
    "name" => $name,
    "colour" => $colour,
    "owned" => $owned
]);