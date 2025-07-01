from sqlite3 import connect
import os

# Create connection to the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "users.db")
conn = connect(db_path)
cursor = conn.cursor()


# Function to run generic SQL queries
def query_db(query):
    cursor.execute(query)
    results = cursor.fetchall()
    return results

# Function to compare the provided password with the stored hashed password for a user
def check_password(username, password):
    # Fetch the hashed password for the given username
    query = f"SELECT hashed_password FROM users WHERE username = '{username}';"
    result = query_db(query)[0][0]  # Array indecies needed as queries return an array

    if result == password:
        return True  # Return true if the login is valid
    else:
        return False  # Return false if the login is invalid