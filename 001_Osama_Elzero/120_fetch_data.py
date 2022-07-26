# def jls_extract_def():

#     import sqlite3

#     return sqlite3

# sqlite3 = jls_extract_def()

import sqlite3

# Creat Database And Coonect 

db = sqlite3.connect("app.db")


# Settiig Up The Cursor 

cr = db.cursor()


# Creat The Table And Fields

db.execute("CREATE TABLE if not exists user (user_id integer , name text) ")

db.execute("CREATE TABLE if not exists skills (name text, progress integer, user_id integer ) ")


# # Inserting Data 

# cr.execute(" INSERT INTO user(user_id, name ) VALUES( 1, 'hamza')")

# cr.execute(" INSERT INTO user(user_id, name ) VALUES( 2, 'banga')")

# cr.execute(" INSERT INTO user(user_id, name ) VALUES( 3, 'ahmed')")


# # Inserting Data 

# cr.execute(" INSERT INTO skills( name, progress, user_id ) VALUES('HTLM',  90, 1)")

# cr.execute(" INSERT INTO skills( name, progress, user_id ) VALUES('CSS' , 90, 2)")

# cr.execute(" INSERT INTO skills( name, progress, user_id ) VALUES('PHP' , 90, 3)")


my_list = ["hamza", "banga", "ahmed", "Buga", "hassan", "hamzoooz", "osama", "moazer", "PC", "Pyton" ]

for key , name in enumerate(my_list):

    cr.execute(f"INSERT INTO user(user_id, name ) VALUES( { key + 1 }, '{name}')")


# Save Commit Changes 

db.commit()


# Close Datebase

db.close()