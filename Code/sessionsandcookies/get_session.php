<?php
session_start();
if (isset($_SESSION['username'])) {
   echo "hello, ". $_SESSION["username"] . "! your role is " . $_SESSION['role'] . ".<br>";
   echo "<a href='destroy_session.php'>log out</a>";

} else {
   echo "No session found. <a href='setsession.php'>set session</a>";
}
?>
