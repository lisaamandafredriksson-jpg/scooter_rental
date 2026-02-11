# 🛴 Scooter Rental System

A containerized scooter rental system built with Python, Docker, and PostgreSQL.  
This project was developed as part of a Programming course, with a strong focus on **Object-Oriented Programming**, **clean architecture**, **testing**, and **professional project structure**.

---

## 📌 Overview

The system allows users to:
- Register and manage users
- Add and manage electric scooters
- Start and end trips
- Automatically calculate trip cost
- Persist all data in a relational database
- Run the entire system using Docker

---

## 🧱 Project Structure

```
scooter_rental/
├── docker-compose.yml
├── README.md
│
└── app/
    ├── Dockerfile
    ├── requirements.txt
    │
    ├── database/
    │   └── init.sql git
    │
    ├── models/
    │   ├── __init__.py
    │   ├── user.py
    │   ├── scooter.py
    │   └── trip.py
    │
    ├── services/
    │   ├── __init__.py
    │   └── database.py
    │
    ├── ui/
    │   ├── __init__.py
    │   └── menu.py
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_user.py
    │   ├── test_scooter.py
    │   └── test_trip.py
    │
    └── main.py
```

---

## 🐳 Running the Project with Docker

### Build and start containers
```bash
docker-compose up --build
```

### Run the application
```bash
docker-compose exec app python main.py
```

---

## 📋 Menu Features

The application includes **9 fully working menu options**:

1. Register a user  
2. Show all users  
3. Add balance to user  
4. Add scooter  
5. Show available scooters  
6. Start a trip  
7. End a trip  
8. Show user trips  
9. Exit program  

---

## 🧠 Design & Architecture

The project follows **separation of concerns**:

- **models/**  
  Contains domain models with private attributes and business logic
- **services/**  
  Handles database connections and SQL queries
- **ui/**  
  Responsible for user interaction and menu handling
- **tests/**  
  Unit tests validating business logic independently from the database

This structure improves readability, maintainability, and testability.

---

## 🧩 Object-Oriented Design

Each core concept is represented as a class:

### User
- Stores user information and balance

### Scooter
- Tracks availability, location, battery level, and price per minute
- Handles rental state

### Trip
- Connects a user and a scooter
- Calculates cost based on trip duration
- Prevents invalid state changes (e.g. ending a trip twice)

All attributes are private and accessed through properties, ensuring encapsulation.

---

## 🗄️ Database Design

The database consists of three related tables.

### users
```sql
id INTEGER PRIMARY KEY
name TEXT
balance REAL
```

### scooters
```sql
id INTEGER PRIMARY KEY
scooter_code TEXT
location TEXT
price_per_min REAL
battery_level INTEGER
is_available BOOLEAN
```

### trips
```sql
id INTEGER PRIMARY KEY
user_id INTEGER REFERENCES users(id)
scooter_id INTEGER REFERENCES scooters(id)
start_time TIMESTAMP
end_time TIMESTAMP
cost REAL
```

---

## 🔍 Example SQL Query

```sql
SELECT * FROM trips;
```

Used to verify trip duration, cost calculation, and relations between users and scooters.

---

## 🧪 Testing

Unit tests are implemented using Python’s `unittest` framework.

- test_user.py
- test_scooter.py
- test_trip.py

The tests verify:
- Correct business logic
- Proper error handling
- Edge cases such as ending a trip twice

---

## ⚠️ Error Handling

The system includes defensive programming:
- Prevents renting an unavailable scooter
- Prevents ending a trip more than once
- Validates battery usage
- Handles invalid operations gracefully

---

## 🚀 Future Improvements

- Trip statistics and revenue tracking
- Filtering and search functionality
- Logging system
- REST API
- Web-based interface

---

## 👩‍💻 Author

Developed by **Lisa**  
Programming student focusing on backend development, databases, and clean architecture.
