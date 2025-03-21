import React from "react";
import { useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AcademicIssuePage from "./AITS_Pages/issuepage";
import StudentDashboard from "./AITS_Pages/StudentDashboard";
import WelcomePage from "./AITS_Pages/WelcomePage";
import LoginPage from "./AITS_Pages/LoginPage";
import LecturerDashboard from "./AITS_Pages/LecturerDashboard";
import Registrardashboard from "./AITS_Pages/Registrardashboard";

function App() {
  useEffect(() => {
    document.title = "AITS";
  }, []);
  
  return (
    <Router>
      <Routes>
        <Route path="/" element={<WelcomePage />} />
        <Route path="/AcademicIssuePage" element={<AcademicIssuePage />} />
        <Route path="/StudentDashboard" element={<StudentDashboard />} />
        <Route path="/LecturerDashboard" element={<LecturerDashboard />} />
        <Route path="/Registardashboard" element={<Registrardashboard />} />
        <Route path="/login" element={<LoginPage />} /> 
      </Routes>
    </Router>
  );
}

export default App;