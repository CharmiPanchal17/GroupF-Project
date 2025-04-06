// RegisterPage.js (React Component)
import React from 'react';
import './RegisterPage.css';
import { useNavigate } from 'react-router-dom';

function RegisterPage() {
  return (
    <div className="container">
      <h1>AITS</h1>
      <img src='logo.jpg' alt='AITS-logo' className='dashboard-logo' />
      <h1>Student Register</h1>
      <form method="post" action="#">
        <input type="text" name="username" placeholder="Username" required />
        <input type="text" name="fullname" placeholder="FullName" required />
        <input type="text" name="student number" placeholder="Student Number" pattern="\d{10}" title="Student number must be exactly 10 digits" required />
        <input type="text" name="registration number" placeholder="Registration Number"required />
        <input type="email" name="email" placeholder="Webmail" required />
        <input type="password" name="password1" placeholder="Password" required />
        <input type="password" name="password2" placeholder="Confirm Password" required />
        <button type="submit" className="submit" onClick={() => navigate("/StudentDashboard")}>Register</button>
        <span className="password">Already have an account? <a href="/login">Login</a></span>
        <span className="password">Forgot <a href="#">password</a></span>
      </form>
    </div>
  );
}

export default RegisterPage;