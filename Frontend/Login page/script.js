// Import the SHA3-256 hashing function
const { sha3_256 } = require('js-sha3');

function hashData(data) {
    return sha3_256(data);  // Directly compute and return the hash
}

// Only run the script when the page contents have loaded
document.addEventListener("DOMContentLoaded", (e) => {
    console.log("Page has loaded, JS running!");
});