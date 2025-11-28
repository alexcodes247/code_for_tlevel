<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Stig of Metal</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Creepster&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Tac+One&display=swap" rel="stylesheet">
  <script src="validation.js" defer></script>
  <link rel="stylesheet" href="booking.css">
</head>
<body>

  <header class="navbar">
    <div class="logo">
      <img src="9bfb18de-823a-47ef-a277-d964f4625556.png" alt="Pure Media Logo" height="50">
      <span><a href="index.html">PURE MEDIA</a></span>
    </div>
    <nav>
      <a href="book-form.php">BOOK TICKETS</a>
      <a href="index.html">ABOUT</a>
      <a href="venues.html">UPCOMING EVENTS</a>
    </nav>
  </header>

  <div id="main">
    <form method="POST" id="form" action="book-form.php">
        <h1>BOOK TICKETS</h1>

        <label for="name">Name</label>
        <input type="text" id="name" name="name" placeholder="Your Name">

        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="Your Email">

        <label for="date">Date</label>
        <select id="date" name="date">
          <option value="">Select an event date</option>
          <option value="2025-11-12">MARCH 15 2025</option>
          <option value="2025-11-19">APRIL 2 2025</option>
          <option value="2025-12-01">APRIL 28 2025</option>
        </select>

        <label for="position">Position</label>
        <select id="position" name="position">
          <option value="">Select position</option>
          <option value="Sitting">Sitting</option>
          <option value="Standing">Standing</option>
          <option value="VIP">Vip Box</option>
        </select>

        <label for="quantity">Quantity</label>
        <input type="number" id="quantity" name="quantity" placeholder="Number of Tickets">

        <input type="submit" id="submit" value="Submit Booking">     
    </form>

<?php
include 'connection.php';
include 'create_table.php';

function sanitise($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $names = sanitise($_POST['name']);
    $emails = sanitise($_POST['email']);
    $dates = sanitise($_POST['date']);
    $positions = sanitise($_POST['position']);
    $quantitys = sanitise($_POST['quantity']);
    $errors = [];

    if (empty($names)) $errors[] = "Name is required.";
    if (empty($emails)) $errors[] = "Email is required.";
    if (empty($dates)) $errors[] = "Date is required.";
    if (empty($positions)) $errors[] = "Position is required.";
    if (empty($quantitys)) $errors[] = "Quantity is required.";
   
    if (empty($errors)) {
    $query = "INSERT INTO bookings (name, email, date, position, quantity) 
              VALUES ('$names', '$emails', '$dates', '$positions', '$quantitys')";
    
    $result = pg_query($connection, $query);

    if ($result) {
        echo "";
    } else {
        echo "Error: " . pg_last_error($connection);
    }
}


  pg_close($connection);

}
?>

  </div>

  <footer id="footer">
    <div id="links">
      <div id="pages">
        <p>PAGES</p>
        <a href="book-form.php">Book</a>
        <a href="venues.html">Venues</a>
        <a href="index.html">About</a>
        <a href="venues.html">Upcoming Events</a>
      </div>
      <div id="venues">
        <p>VENUES</p>
        <a href="#">The Iron Dome</a>
        <a href="#">Area Rock</a>
        <a href="#">Stagen Arena</a>
        <a href="#">Moes Bar</a>
      </div>
      <div id="legal">
        <p>LEGAL</p>
        <a href="#">T&Cs</a>
        <a href="#">Privacy Policy</a>
      </div>
    </div>
    <div>
      <p id="copyright">© 2025 The Stig | All Rights Reserved</p>
    </div>
  </footer>
</body>

</html>
