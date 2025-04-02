import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useState } from 'react';
import './App.css';
import Welcome from './Welcome';
import Signup from './Signup';
import Login from './Login';
import StudentDashboard from './StudentDashboard';
import LecturerDashboard from './LecturerDashboard';


function App() {
  return (
        //<div className= "App-header" style={{ padding: "20px", textAlign: "center" }}>
              
               // <h1>Academic Issue Tracking System</h1>
               //<img src="/logo.jng" alt="AITS logo" className="logo" />                
        <Router>
        <Routes>
            <Route path="/" element={<Welcome />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/studentdashboard" element={<StudentDashboard />} />
            <Route path="*" element={<Login />} />  {/* Default route */}
            </Routes>
            </Router>
            
            
    
  );
}

export default App;
