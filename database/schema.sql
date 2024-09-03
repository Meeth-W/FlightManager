CREATE TABLE IF NOT EXISTS `user` (
    `user_id` int PRIMARY KEY,
    `user_name` varchar(20) NOT NULL,
    `user_password` varchar(20) NOT NULL,
    `user_permission_level` varchar(10) NOT NULL DEFAULT `base_user`,
    `user_email` varchar(100) NOT NULL,
    `user_address` varchar(100) NOT NULL,
    `user_dateofbirth` DATE NOT NULL,
    `user_age` INT NOT NULL,

    CHECK (`user_age` >= 18)
)

CREATE TABLE IF NOT EXISTS `flights` (
    `id` INT PRIMARY KEY,
    `flight_number` VARCHAR(10) NOT NULL,
    `flight_name` VARCHAR(20) NOT NULL,
    `airline` VARCHAR(10) NOT NULL,
    `departure_airport` VARCHAR(20) NOT NULL,
    `arrival_airport` VARCHAR(20) NOT NULL,
    `flight_date` DATE NOT NULL,
    `flight_time` INT NOT NULL,
    `flight_duration` INT NOT NULL,
    `flight_status` VARCHAR(10) NOT NULL DEFAULT 'on_time',
    `available_seats` INT NOT NULL,
)

CREATE TABLE IF NOT EXISTS `bookings` (
    
)