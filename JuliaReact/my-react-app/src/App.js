// App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AcademicIssuePage from "./AITS_Pages/issuepage";
import StudentDashboard from "./AITS_Pages/student dashboard ";
import WelcomePage from "./AITS_Pages/WelcomePage";
import LoginPage from "./AITS_Pages/LoginPage"; // Import your LoginPage component

function App() {
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