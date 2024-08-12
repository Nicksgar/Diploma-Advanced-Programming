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

$sql = "SELECT id, name, colour, owned "
    ."FROM demo WHERE id = 4";

$statement = $pdo->prepare($sql);

$statement->execute();

$results = $statement->fetchAll(PDO::FETCH_ASSOC);

print_r($results);

echo "<dl>"
foreach ($results as $key => $value) {
    ?>
     "<dt><?=$key ?></dt>"
     "<dd><?=$value ?></dd>";
<?php
}
echo "</dl>";