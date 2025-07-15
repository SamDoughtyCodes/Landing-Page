// Import the SHA3-256 hashing function
import sha3 from "https://cdn.jsdelivr.net/npm/js-sha3@0.9.2/+esm";

const token = localStorage.getItem("token");  // Attempt to fetch the token of the user

function hashData(data) {
    return sha3.sha3_256(data);  // Directly compute and return the hash
}

// Process a login request
const login_form = document.getElementById("login_form");
login_form.addEventListener("submit", async function(e) {
    // Get login data from the form when a submission is logged
    e.preventDefault()
    let user = login_form["username"].value;
    let hashed_p = hashData(login_form["password"].value);
    let login_data = {"username": user, "password": hashed_p};

    // Check the login data
    const response = await fetch("http://localhost:8000/api/login", {method: 'POST', headers: {"Content-Type": "application/json"}, body: JSON.stringify(login_data)});
    const data = await response.json();

    // Deal with the login data accordingly
    if (data.valid === false) {  // If the login details aren't valid, output a suitable message
        let err = data.error;
        const msg_p = document.getElementById("login_status_msg");
        if (err === "Invalid Username") {msg_p.innerText = "This username does not exist!";}
        else if (err === "Invalid Password") {msg_p.innerText = "Incorrect password!";}
    } else {  // If the login details are valid, create a token for the user
        console.log("Valid login!")
    }
});