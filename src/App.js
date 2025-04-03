import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useState } from 'react';
import './App.css';
import Welcome from './Welcome';
import StudentRegister from './StudentRegister';
import LecturerRegister from './LecturerRegister';
import Login from './Login';
import StudentDashboard from './StudentDashboard';
import LecturerDashboard from './LecturerDashboard';


function App() {
  return (

      <div className= "App-header" style={{ padding: "20px", textAlign: "center" }}>
                             
        <Router>
        <Routes>
            <Route path="/" element={<Welcome />} />
            <Route path="/StudentRegister" element={<StudentRegister />} />
            <Route path="/LecturerRegister" element={<LecturerRegister />} />
            <Route path="/login" element={<Login />} />
            <Route path="/studentdashboard" element={<StudentDashboard />} />
            <Route path="*" element={<Login />} />  {/* Default route */}
            </Routes>
            </Router>
            </div>
            
            
  ); 
  
};

export default App;
