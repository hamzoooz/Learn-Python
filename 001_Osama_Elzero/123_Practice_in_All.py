import sqlite3

# Creat Database And Coonect 
db = sqlite3.connect("app.db")
# Settiig Up The Cursor 
cr = db.cursor()

# My user ID 
user_id = 1

# Commit And Close 
def commit_and_close():
    db.commit()
    db.close()
    print("Done !")

# input Big Message
input_message = """
    What Do You Want To Do ? 
    "s" => Show All Skill 
    "a" => Add New Skill
    "d" => Delete A Skill  
    "u" => Update A Skill 
    """
user_input = input(input_message).strip().lower()

# Command List
command_list = ["s", "a", "d", "u", "q"]

# Define The Method 
def show_skills():
    print("Show Skill")
    commit_and_close()

def add_skills():
    skill = input("Write Skill Name  ").strip().capitalize()
    progress = input("Write Skill Progress  ").strip()
    cr.execute(f" INSERT INTO skills(name, progress, user_id ) VALUES('{skill}', '{progress}', '{user_id}'  )  ")
    print("Add Skill")
    commit_and_close()

def delete_skills():
    print("Deleting ")
    skill = input("Write Skill Name To Delete  ").strip().capitalize()
    cr.execute(f" DELETE FROM skills WHERE name = '{skill}' AND user_id = '{user_id}' ")
    commit_and_close()

def update_skills():
    print("Update Skill")
    commit_and_close()

# Check If Command is Ecists
if user_input in command_list:
    print(f"Command Found {user_input} ")
    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skills()
    elif user_input == "d":
        delete_skills()
    elif user_input == "u":
        update_skills()
else:

    print(f"Sorry This Command [{user_input} ] Not Found ")
    print("App Was Closed . ")
