import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./StudentRegister.css"; // Corrected the import path

function Login () {
    const navigate = useNavigate();

    
    return (
        <div className="container">
            <h2>Login</h2>
            <form action="action_page.php" method="post">
                {/*<div className="logo">
                    <img src="logo.jpg" alt="AITS logo" className="logo"></img>
                </div>*/}
                
                <div className="input-group">
                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        required
                    />
                </div>
                <div className="input-group">
                    <input
                        type="password"
                        name="password"
                        placeholder="Password"
                        required
                    />
                </div>
                <button type="submit" className="submit" onClick={() => navigate("/StudentDashboard")}>Login</button>
                </form>
                 <p>
                Don't have an account?{" "}
                <span onClick={() => navigate("/studentRegister")} style={{ color: "blue", cursor: "pointer" }}>
                    Register
                </span>
                <span className="password">Forgot<a href="#">password</a>
                </span>
            </p>
        </div>

    );
};

export default Login;