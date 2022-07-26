import sqlite3

def connect_database():
    try:
            
        # Creat Database And Coonect 
        db = sqlite3.connect("app.db")

        # Settiig Up The Cursor 
        cr = db.cursor()
        # Fetch Data From Database 
        cr.execute("SELECT * FROM user ")

        result = cr.fetchall()
        print(f"Database Has {len(result)} Rows. ")

        for row in result:
            print(f"UserID => {row[0]},", end=" " )
            print(f"UserName  => {row[1]} ")


    except sqlite3.Error as re :
        print(f"There Error [{re}] ")

    finally:
        print("Done")
        # Close Datebase
        db.close()

connect_database()