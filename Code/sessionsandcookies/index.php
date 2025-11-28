<?php
session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>sessions</title>
</head>
<body>
<?php
$_SESSION["username"]="JohnDoe";
$_SESSION["email"]="email@email.com";


echo "session variables are set";
echo $_SESSION["username"];
?>
   
</body>
</html>