from sqlite3 import connect
import os

# Create connection to the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "users.db")
conn = connect(db_path, check_same_thread=False)
cursor = conn.cursor()

# Function to compare the provided password with the stored hashed password for a user
def check_password(username, password):
    # Fetch the hashed password for the given username
    query = f"SELECT hashed_password FROM users WHERE username = ?;"
    cursor.execute(query, (username,))
    result = cursor.fetchall()

    if result:
        if result[0][0] == password: return {'valid': True, 'error': None}
        else: return {'valid': False, 'error': 'Invalid Password'}
    else: return {'valid': False, 'error': 'Invalid Username'}

# Function to add a new user to the database
def add_user(username, password):
