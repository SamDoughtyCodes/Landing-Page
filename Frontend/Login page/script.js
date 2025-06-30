// Import the SHA3-256 hashing function
const { sha3_256 } = require('js-sha3');

function hashData(data) {
    return sha3_256(data);  // Directly compute and return the hash
}