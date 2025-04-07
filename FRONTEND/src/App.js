import React, { useState, useEffect, useContext } from 'react';
import { 
  BrowserRouter as Router, 
  Routes, 
  Route, 
  Navigate 
} from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

// Import your pages and components
import AcademicIssuePage from './AITS_Pages/issuepage';
import StudentDashboard from './AITS_Pages/StudentDashboard';
import WelcomePage from './AITS_Pages/WelcomePage';
import LoginPage from './AITS_Pages/LoginPage';
import LecturerDashboard from './AITS_Pages/LecturerDashboard';
import Registrardashboard from './AITS_Pages/Registrardashboard';

// Import your auth context
import { authContext } from './context/AuthContext';

// Toast container configuration
const toastProps = {
  position: "top-right",
  autoClose: 3000,
  hideProgressBar: false,
  newestOnTop: false,
  closeOnClick: true,
  rtl: false,
  pauseOnFocusLoss: true,
  draggable: true,
  pauseOnHover: true
};

function App() {
  const [loading, setLoading] = useState(true);
  const { userLoginData } = useContext(authContext);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    document.title = "AITS";
    setIsAuthenticated(!!localStorage.getItem("token"));
    setLoading(false);
  }, [userLoginData]);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  return (
    <>
      <Router>
        <Routes>
          {/* Always accessible routes */}
          <Route path="/" element={<WelcomePage />} />
          <Route path="/login" element={<LoginPage />} />
          
          {/* Protected routes */}
          {isAuthenticated ? (
            <>
              {/* Student Routes */}
              {userLoginData?.role === "student" && (
                <>
                  <Route path="/student" element={<StudentDashboard />} />
                  <Route path="/student/academic-issues" element={<AcademicIssuePage />} />
                </>
              )}

              {/* Lecturer Routes */}
              {userLoginData?.role === "lecturer" && (
                <>
                  <Route path="/lecturer" element={<LecturerDashboard />} />
                  <Route path="/lecturer/academic-issues" element={<AcademicIssuePage />} />
                </>
              )}

              {/* Registrar Routes */}
              {userLoginData?.role === "registrar" && (
                <Route path="/registrar-dashboard" element={<Registrardashboard />} />
              )}
            </>
          ) : null}

          {/* Fallback routes */}
          <Route 
            path="*" 
            element={
              isAuthenticated 
                ? <Navigate to={getDefaultRoute(userLoginData?.role)} replace /> 
                : <Navigate to="/login" replace />
            } 
          />
        </Routes>
      </Router>
      <ToastContainer {...toastProps} />
    </>
  );
}

// Helper function for default routes
function getDefaultRoute(role) {
  switch(role) {
    case 'student': return '/student';
    case 'lecturer': return '/lecturer';
    case 'registrar': return '/registrar-dashboard';
    default: return '/login';
  }
}

export default App;