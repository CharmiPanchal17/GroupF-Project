import React,{useState} from "react";
import { useNavigate } from "react-router-dom";
import './SignupLogin.css'

const Signup = () => {
    const [studentNumber, setStudentNumber] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!/^\d{10}$/.test(studentNumber)) {setError("student number must be exactly 10 digits.");
            return;
        }
        setError("");
        console.log("user signed up:");
        navigate("/login");// this will navigate to the login page
     };

        return (
            <div className="page-container">
                <div className="signup-container">
                    <div className="header">
                    <h1>WELCOME TO Aits!</h1>
                <h2 style={{color:"purple", justifyContent:"center", textUnderlinePosition:2 }}>Signup</h2>
                <form onSubmit={handleSubmit}> 
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
                    <button type="submit" onClick={() => navigate("/StudentDashboard")} style={{color:"plum", cursor:"pointer"}}>Signup</button>
                </form>
                    <p>
                        Have an account?{" "}
                        <span onClick={() => navigate("/Login")} style={{color:"blue", cursor:"pointer"}}>Login</span>
                    </p>
                    </div>
                    </div>
                    </div>
                      

    
    );
};
export default Signup;
