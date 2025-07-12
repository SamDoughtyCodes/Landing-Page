# Landing-Page
A basic landing page with login credentials, hooked up to a database for a bit of fun

NOTE: All commits are made by me, Sam Doughty. Any from the account "LilSpinachBoy1" are still me, but just from certain devices where that account is signed in.

## How it works
The following structure diagram provides a basic overview of the components of the project:
![Project structure diagram](https://github.com/SamDoughtyCodes/Landing-Page/blob/main/Super-Curricular%20Landing%20Page%20(1).png)

## How to use the site
Although this would typically be extremely insecure, as this is a demonstrative project and contains no sensitive data, I have shown some valid login credentials beneath for you to use. I have also shown the hashed passwords for reference.
| Username | Password | Hashed Password |
| -------- | -------- | --------------- |
| admin1   | adm1n!   | 251544a05ca68b78142cb1490f93200e4c2656db720aa10b3900047748d8d2ca |
| user1    | us3r?    | 71224760c014ad6558bc9a86639caaa7248183074a48eb2fade7a4faa79d93c9 |
| user2    | 0therUsr | b18de7e2466beed153d8c9f7fe904c8fc1e223a63637b08732fcf23895cb912f |

## Development
### Hashing
I decided to hash passwords for this project in order to increase its security. Using the SHA3-256 hashing algorithm, I have encoded the passwords on the client-side. This ensures that no private data (passwords) are sent over any networks where they are at risk of interception. Storing the hashed version of the passwords on the database is also beneficial, as it ensures that if the data was leaked it could not be traced back to the real password values.
### Setting up the database
I have used sqlite for the database of this project, as its lightweight and portable nature fits the simplistic needs of the site. Furthermore, I am using a flat file database, with one table named `users`. This is as the scope of this project does not require anyhthing more complex.
A basic outline of the database structure is shown below:
| Field | Data Type | Description |
| ----- | --------- | ----------- |
| user_id | INTEGER | Stores the id of the user. Is the Primary Key. |
| username | varchar(255) | Stores the username. |
| hashed_password| varchar(255) | Stores the hashed version of the password, for added security. |

### The API
Using FastAPI, I created a simple python script to handle the login requests. The file contains only 2 endpoints, a GET type test function (to confirm that the API is working correcrly), and a POST type function to confim a login.
```Python
# Create a model for the login request
class LoginRequest(BaseModel):
    username: str
    password: str

# Create an endpoint for user login
@app.post("/api/login")
def login(request: LoginRequest):
    # Check with the database if the username and password are correct
    return check_password(request.username, request.password)
```
The `login` function takes the posted data from the API call as a pydantic BaseModel, and passes it to the `check_password` function of the database.
```Python
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
```
This creates a connection to `users.db`. It then creates a query to fetch the hash value of the password corrisponding with the required username (doing so using parameters to protect from an SQL injection), and stores it in the result variable. If the query returns data (i.e. A user with that username exists), the query password is compared to the API call password. If they are equal, the user can be granted access to the site, otherwise they can be denied based on an incorrect password or an incorrect username, depending on if the query returned any data.
