const crypto = require("crypto");
const fs = require("fs");
const prompt = require("prompt-sync")({ sigint: true });

function encryptPassword(password) {
  // Create a hash object
  const hash = crypto.createHash("sha256");

  // Use the update method to add the password to the hash object
  hash.update(password);

  // Get the encrypted password as a hexadecimal string
  const encryptedPassword = hash.digest("hex");

  return encryptedPassword;
}

// Prompt the user for a username
const username = prompt("Enter your username:");
// Prompt the user for a password
const password = prompt("Enter your password:");

// Encrypt the password
const encryptedPassword = encryptPassword(password);

// Store the encrypted password in a JSON file
const data = {
  username,
  password: encryptedPassword,
};
fs.writeFileSync("password.json", JSON.stringify(data));
