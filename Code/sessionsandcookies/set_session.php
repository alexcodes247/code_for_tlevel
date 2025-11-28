<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $_SESSION['username'] = $_POST['username'] ?? '';
    $_SESSION['role'] = $_POST['role'];

    echo "Session variables are set. <a href='get_session.php'>Go to get_session.php</a>";
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Document</title>
</head>
<body>
   <form action="set_session.php" method="POST">
      <input type="text" name="username" required>
      <input type="text" name="role" required>
      <input type="submit">
   </form>
</body>
</html>
