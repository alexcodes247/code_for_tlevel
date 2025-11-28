<?php
        $query = "CREATE TABLE IF NOT EXISTS bookings (
        /*id SERIAL PRIMARY KEY,*/
        name VARCHAR(255) NOT NULL,
        email Varchar(255) NOT NULL,
        position Varchar(255) NOT NULL,
        date Varchar(255) NOT NULL,
        quantity VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)";

    $result = pg_query($connection, $query);

    if ($result) {
        echo "";
    } else{
        echo "error create table:" . pg_last_error($connection);
    }


?>