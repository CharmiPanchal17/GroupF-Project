import React,{useState} from "react";
import { useNavigate } from "react-router-dom";
import './SignupLogin.css'

const Signup = () => {
    const [studentNumber, setStudentNumber] = useState("");
    const [role, setRole] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        if (role === "student" && !/^\d{10}$/.test(studentNumber)) {setError("student number must be exactly 10 digits.");
            return;
        }
        setError("");
        console.log(`User signed up as ${role}:`);

        if (role === "student"){
        navigate("/StudentDashboard");
        } else if (role === "lecturer") {
            navigate("/LecturerDashboard");
        }
     };

        return (
            <div className="page-container">
              
                <div className="signup-container">
                {/*<img src="/logo.jpg" alt="AITS logo" className="logo" />*/} 
                <h2>Signup</h2>
                <form> 
                    <div className="input-group">
                        <label>Username</label>
                          <input type="text" placeholder="Username"/></div>
                             <div className="input-group">
                                <label>Email</label>
                               <input type="email" placeholder="Email"/></div>
                               <div className="input-group">
                    <label>Student Number</label>
                    <input
                        type="text" placeholder="Student Number"
                    /></div>
                          <div className="input-group">
                             <label>Password</label>
                                 <input type="password" placeholder="Password" /></div>
                                  
                                    {error && <p style={{ color: "red" }}>{error}</p>}             
                    <button type="submit" className="submit" onClick={() => navigate("/StudentDashboard")} style={{cursor:"pointer"}}>Signup</button>
                </form>
                    <p>
                        Have an account?{" "}
                        <span onClick={() => navigate("/Login")} style={{color:"blue", cursor:"pointer"}}>Login</span>
                    </p>
                    </div>
                    </div>
                    
        
                      

    
    );
};
export default Signup;
