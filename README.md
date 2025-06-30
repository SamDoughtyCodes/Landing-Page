# Landing-Page
A basic landing page with login credentials, hooked up to a database for a bit of fun

NOTE: All commits are made by me, Sam Doughty. Any from the account "LilSpinachBoy1" are still me, but just from certain devices where that account is signed in.

## How it works
The following structure diagram provides a basic overview of the components of the project:
![Project structure diagram](https://github.com/SamDoughtyCodes/Landing-Page/blob/main/Super-Curricular%20Landing%20Page%20(1).png)
Passwords are hashed to improve security, and this is done client-side to reduce the risk of interception as API calls are made.

## How to use the site
Although this would typically be extremely insecure, as this is a demonstrative project and contains no sensitive data, I have shown some valid login credentials beneath for you to use:
| Username | Password |
| -------- | -------- |
| admin1   | adm1n!   |
| user1    | us3r?    |
| user2    | 0therUsr |

## Development
### Setting up the database
I have used sqlite for the database of this project, as its lightweight and portable nature fits the simplistic needs of the site. Furthermore, I am using a flat file database, with one table named `users`. This is as the scope of this project does not require anyhthing more complex.
A basic outline of the database structure is shown below:
| Field | Data Type | Description |
| ----- | --------- | ----------- |
| user_id | INTEGER | Stores the id of the user. Is the Primary Key. |
| username | varchar(255) | Stores the username. |
| hashed_password| varchar(255) | Stores the hashed version of the password, for added security. |
