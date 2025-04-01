// StudentRegister.js (React Component)
import React from 'react';
import './StudentRegister.css';

function LecturerRegister() {
  return (
    <div className="container">
      <h1>Lecturer Register</h1>
      <form method="post" action="#">
        <input type="text" name="username" placeholder="Username" required />
        <input type="text" name="lecturer registration number" placeholder="Lecturer Registration Number" required />
        <input type="email" name="email" placeholder="Webmail" required />
        <input type="password" name="password1" placeholder="Password" required />
        <input type="password" name="password2" placeholder="Confirm Password" required />
        <button type="submit">Register</button>
        <span className="password">Already have an account? <a href="/login">Login</a></span>
      </form>
    </div>
  );
}

export default LecturerRegister;