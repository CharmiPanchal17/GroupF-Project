import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useState } from 'react';
import './App.css';
import SignupLogin from './SignupLogin';
import StudentDashboard from './StudentDashboard';
import LecturerDashboard from './LecturerDashboard';

function App() {
  return (
    <div className="App">
        <Router>
        <Routes>
            <Route path="/signup" element={<SignupLogin />} />
            <Route path="/studentdashboard" element={<StudentDashboard />} />
            <Route path="/" element={<Navigate to="/Signup" />} />
            </Routes>
            </Router>
    </div>
  );
}

export default App;
