// RegisterPage.js (React Component)
import React from 'react';
import './RegisterPage.css';
import { useNavigate } from 'react-router-dom';

function LecRegisterPage() {
  const navigate = useNavigate()
  
  return (
    <div className="container">
      <h1>🧑‍🏫 Lecturer Register</h1>
      <form method="post" action="#">
        <input type="text" name="username" placeholder="Username" required />
        <input type="text" name="fullname" placeholder="FullName" required />
        <input type="text" name="lecturer id" placeholder="Lecturer ID" pattern="\d{8}" title="Lecturer number must be exactly 8 digits" required />
        <input type="email" name="email" placeholder="Webmail" required />
        <input type="password" name="password1" placeholder="Password" required />
        <input type="password" name="password2" placeholder="Confirm Password" required />
        <button type="submit">Register</button>
        <span className="password">Already have an account? <a href="/login">Login</a></span>
        <span className="password">Forgot <a href="#">password</a></span>
      </form>
    </div>
  );
}

export default LecRegisterPage;