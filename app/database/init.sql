-- USERS
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    balance NUMERIC(10,2) DEFAULT 0
);


-- SCOOTERS
CREATE TABLE IF NOT EXISTS scooters (
    id SERIAL PRIMARY KEY,
    scooter_code TEXT UNIQUE NOT NULL,
    location TEXT NOT NULL,
    price_per_min NUMERIC(5,2) NOT NULL,
    battery_level INTEGER NOT NULL,
    is_available BOOLEAN DEFAULT TRUE
);

-- TRIPS
CREATE TABLE IF NOT EXISTS trips (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    scooter_id INTEGER NOT NULL REFERENCES scooters(id),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    cost NUMERIC(10,2)
);
