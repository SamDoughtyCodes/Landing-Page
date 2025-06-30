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
