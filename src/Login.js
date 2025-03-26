import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./SignupLogin.css"; // Corrected the import path

const Login = () => {
    const navigate = useNavigate();

    const handleLogin = (e) => {
        e.preventDefault();
        console.log("User successfully logged in!");
    };

    return (
        <div className="container">
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
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
                <span onClick={() => navigate("/signup")} style={{ color: "blue", cursor: "pointer" }}>
                    Signup
                </span>
            </p>
        </div>

    );
};

export default Login;