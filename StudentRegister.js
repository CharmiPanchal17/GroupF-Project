// StudentRegister.js (React Component)
import React from 'react';
import './StudentRegister.css';

function StudentRegister() {
  return (
    <div className="container">
      <h1>Student Register</h1>
      <form method="post" action="#">
        <input type="text" name="username" placeholder="Username" required />
        <input type="text" name="fullname" placeholder="FullName" required />
        <input type="number" name="student number" placeholder="Student Number" required />
        <input type="text" name="student registration number" placeholder="Student Registration Number" required />
        <input type="email" name="email" placeholder="Email Address" required />
        <input type="password" name="password1" placeholder="Password" required />
        <input type="password" name="password2" placeholder="Confirm Password" required />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default StudentRegister;