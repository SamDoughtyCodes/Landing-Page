// Import the SHA3-256 hashing function
import sha3 from "https://cdn.jsdelivr.net/npm/js-sha3@0.9.2/+esm";

const token = localStorage.getItem("token");  // Attempt to fetch the token of the user

function hashData(data) {
    return sha3.sha3_256(data);  // Directly compute and return the hash
}

// Only run the script when the page contents have loaded
document.addEventListener("DOMContentLoaded", (e) => {
    // Add a fetch here to run the API test endpoint
    console.log("Page has loaded, JS running!");
});