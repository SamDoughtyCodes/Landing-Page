const token = localStorage.getItem("token")  // Get the token for the user (null if doesn't exist)

document.addEventListener("DOMContentLoaded", (e) => {  // Only run when the content has loaded
    // --------- Use the token to verify the login ---------
    fetch("http://localhost:8000/api/protected", {method: 'GET', headers: {'Authorization': 'Bearer' + token}})  // API call through the protected route (GET method and token in header)
    .then(response => {  // Take the API response and run it through the following:
        if (response.status === 403 || response.status === 401) {window.location.href = "/Login page/login.html";}  // Redirect if no token/expired token
        else {return response.json();}  // Return the json message from the protected route if the token is valid
    })
    .then(data => {
        document.getElementById("welcome_text").innerText = data.message;  // Set the login message from the protected route if the token is valid
    })
});