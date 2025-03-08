function validateForm() {
          // Get form elements
          const fullName = document.getElementById('fullName').value.trim();
          const email = document.getElementById('email').value.trim();
          const password = document.getElementById('password').value.trim();
          
          const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/; // Email regex pattern
          
          // Validate Full Name (max length 30)
          if (fullName === "") {
              alert("Full Name is required.");
              return false;
          } else if (fullName.length > 30) {
              alert("Full Name should not exceed 30 characters.");
              return false;
          }
      
          // Validate Email (max length 30)
          if (email === "") {
              alert("Email is required.");
              return false;
          } else if (email.length > 30) {
              alert("Email should not exceed 30 characters.");
              return false;
          } else if (!emailPattern.test(email)) {
              alert("Please enter a valid email address.");
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
      
          return true;
      }
      