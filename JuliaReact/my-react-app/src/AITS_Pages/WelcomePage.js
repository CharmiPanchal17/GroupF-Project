import React from 'react';
import { Link } from 'react-router-dom';
import './WelcomePage.css';
import Navbar from '../components/Navbar';

const WelcomePage = () => {
  return (
    <div className="welcome-page-container">
      <header className="welcome-page-header">
        <img src="/images/Aitslogo.png" alt="AITS Logo" className="welcome-page-logo"/>
        <h2>WELCOME TO AITS (Acacemic Issue Tracking System)</h2>
        <p>Your comprehensive academic management system.</p>
        <p>How can we help you?</p>
      </header>

      <Navbar /> {/* Navbar moved outside main */}

      <main className="welcome-page-main">
        <section className="welcome-page-section">
          <h2>Students</h2>
          <p>Access your courses, grades, and resources.</p>
          <div className="welcome-page-links">
            <Link to="/student-login" className="welcome-page-link">Login</Link>
            <Link to="/student-signup" className="welcome-page-link">Sign Up</Link>
          </div>
        </section>

        <section className="welcome-page-section">
          <h2>Lecturers</h2>
          <p>Manage courses, students, and academic tasks.</p>
          <div className="welcome-page-links">
            <Link to="/lecturer-login" className="welcome-page-link">Login</Link>
            <Link to="/lecturer-signup" className="welcome-page-link">Sign Up</Link>
          </div>
        </section>

        <section className="welcome-page-section">
          <h2>Registrars</h2>
          <p>Administer student records and system settings.</p>
          <div className="welcome-page-links">
            <Link to="/registrar-login" className="welcome-page-link">Login</Link>
            <Link to="/registrar-signup" className="welcome-page-link">Sign Up</Link>
          </div>
        </section>
      </main>

      <footer className="welcome-page-footer">
        <p>&copy; 2025 AITS. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default WelcomePage;