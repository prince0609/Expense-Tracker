function validateForm() {
  // Get form elements
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();

  // Validate Username (max length 30)
  if (username === "") {
    alert("Username is required.");
    return false;
  } else if (username.length > 30) {
    alert("Username should not exceed 30 characters.");
    return false;
  }

  // Validate Password (min 6 and max 15 characters)
  if (password === "") {
    alert("Password is required.");
    return false;
  } else if (password.length < 6 || password.length > 15) {
    alert("Password must be between 6 and 15 characters.");
    return false;
  }

  // If everything is valid, the form will be submitted
  return true;
}
