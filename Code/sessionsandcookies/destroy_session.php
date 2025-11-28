<?php
session_start();
session_unset();
session_destroy();
echo "to create a session. <a href='set_session.php'>set session</a>"
?>