import React from "react";
import { useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AcademicIssuePage from "./AITS_Pages/issuepage";
import StudentDashboard from "./AITS_Pages/StudentDashboard";
import WelcomePage from "./AITS_Pages/WelcomePage";
import LoginPage from "./AITS_Pages/LoginPage";

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
        <Route path="/login" element={<LoginPage />} /> {/* Add login route */}
      </Routes>
    </Router>
  );
}

export default App;