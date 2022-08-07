import sqlite3
import pprint

conn = sqlite3.connect('DataBase.db')
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS Goods (
Good_ID INTEGER PRIMARY KEY AUTOINCREMENT, Name varchar(255));
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Depots (
Depot_ID INTEGER PRIMARY KEY AUTOINCREMENT, Depot varchar(255));
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Bookings (
Good_ID INTEGER PRIMARY KEY, Depot_ID, Booking_Date varchar(255));
""")

cur.execute("""
INSERT INTO Goods (Name) VALUES ('кроссовки'), ('кроссовки'),
('нож'), ('нож'), ('нож'), 
('вилка'), ('вилка'),
('шорты'), ('шорты'), ('шорты'),
('окунь'),
('шапка'), ('шапка'),
('нож');
""")

cur.execute("""
INSERT INTO Depots (Depot) VALUES ('Minsk-Central'), ('Minsk-East'), ('Brest'), ('Vitebsk');
""")

cur.execute("""
INSERT INTO Bookings (Good_ID, Depot_ID ,Booking_Date) VALUES (1, 1, '13:11:24'), (2, 1, '14:11:24'), 
(3, 1, '15:11:24'), (4, 1, '16:11:24'), (5, 1, '17:11:24'), (6, 2, '18:11:24'), (7, 2, '19:11:24'), 
(8, 3, '19:11:24'), (9, 3, '20:11:24'), (10, 3, '21:11:24'), (11, 4, '22:11:24'), (12, 1, '23:11:24'), 
(13, 1, '05:11:24'), (14, 2, '06:11:24');
""")

cur.execute("""
select *  from Goods
;""")

pprint.pprint(cur.fetchall(), width=45)

cur.execute("""
select *  from Depots
;""")

pprint.pprint(cur.fetchall(), width=45)

cur.execute("""
select *  from Bookings
;""")

pprint.pprint(cur.fetchall(), width=45)

conn.commit()

#select Name, Depot, Booking_Date from Bookings inner join Depots D on Bookings.Depot_ID = D.Depot_ID inner join Goods G on Bookings.Good_ID = G.Good_ID order by G.Good_ID desc limit 5;
