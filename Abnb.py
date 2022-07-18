
import csv
from cs50 import SQL

open("AirBnB.db", "w").close()

db = SQL("sqlite:///AirBnB.db")

db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, updated_at TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP)")

db.execute("CREATE TABLE homes (id INTEGER PRIMARY KEY, address TEXT, price_per_night INTEGER, updated_at TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP)")

db.execute("CREATE TABLE reservations (id INTEGER PRIMARY KEY AUTOINCREMENT, role TEXT, start_date TEXT, end_date TEXT, updated_at TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP)")

db.execute("CREATE TABLE users_homes (id INTEGER PRIMARY KEY, user_id INTEGER, home_id INTEGER, reservations_id INTEGER, updated_at TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(user_id) REFERENCES users(id), FOREIGN KEY(home_id) REFERENCES homes(id), FOREIGN KEY (reservations_id) REFERENCES reservations(id))")


with open("ABnB.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        title = row["name"].strip().capitalize()
        mail = row["email"].strip().capitalize()
        address = row["address"].strip().capitalize()
        price_per_night = row["price_per_night"].strip().capitalize()
        role = row["role"].strip().capitalize()
        start_date = row["start_date"].strip().capitalize()
        end_date = row["end_date"].strip().capitalize()
        total = row["total"].strip().capitalize()

        users = db.execute("INSERT INTO users(name, email) VALUES(?, ?)", title, mail)
        
        homes = db.execute("INSERT INTO homes(address, price_per_night) VALUES(?, ?)", address, price_per_night)
    
        reservations = db.execute("INSERT INTO reservations(role, start_date, end_date) VALUES(?, ?, ?)", role, start_date, end_date)

        users_homes = db.execute("INSERT INTO users_homes(user_id, home_id, reservations_id) VALUES((SELECT id FROM users WHERE name = ?),(SELECT id FROM homes WHERE address = ?),?)", title, address, reservations)


        