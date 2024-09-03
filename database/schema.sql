CREATE TABLE IF NOT EXISTS "user" (
    "user_id" INTEGER PRIMARY KEY,
    "user_name" TEXT NOT NULL,
    "user_password" TEXT NOT NULL,
    "user_permission_level" TEXT NOT NULL DEFAULT 'base_user',
    "user_email" TEXT NOT NULL,
    "user_address" TEXT NOT NULL,
    "user_dateofbirth" DATE NOT NULL,
    "user_age" INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "flights" (
    "id" INTEGER PRIMARY KEY,
    "flight_number" TEXT NOT NULL,
    "flight_name" TEXT NOT NULL,
    "airline" TEXT NOT NULL,
    "departure_airport" TEXT NOT NULL,
    "arrival_airport" TEXT NOT NULL,
    "flight_date" DATE NOT NULL,
    "flight_time" INTEGER NOT NULL,
    "flight_duration" INTEGER NOT NULL,
    "flight_status" TEXT NOT NULL DEFAULT 'on_time',
    "available_seats" INTEGER NOT NULL,
    "price" INTEGER NOT NULL
);
