<!DOCTYPE html>
<html>
<body>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- mobile-friendly -->

<?php
function factorize($n) {
    echo "<br>$n: ";
    // Error checks on $n < 0, $n >= 65536 omitted for brevity ...
    $d = 2;
    while ($n > 1) {
        $power = 0;
        while (($n % $d) == 0) {
            $power += 1;
            $n /= $d;
        }
        if ($power == 1) {
            echo " $d";
        } else if ($power > 1) {
            echo " $d^$power";
        }
        $d += 1;
    }
    echo "</br>\n";
}
?>

<?php factorize((integer)$_GET["n"]); ?>

</body>
</html>
