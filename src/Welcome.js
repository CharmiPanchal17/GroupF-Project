import React from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import './Welcome.css'; // Corrected the import path

const Welcome = () =>{
    const navigate = useNavigate();

    return(
        <div className="page-container">
            <h1>WELCOME TO ACADEMIC ISSUE TRACKING SYSTEM!</h1>
            
            <div className="navbar">
                <a href="home">Home</a>
                <a href="contacts">Contacts</a>
                <a href="about us">About us</a>
                <a href="help">Help</a>
                <div className="dropdown">
         
                    <button className="dropbtn">Login</button>
                    <div className="dropdown-content">    
                    <a onClick={() => navigate("/login")}>As Student</a>
                    <a onClick={() => navigate("/lecturer-login")}> As Lecturer</a>
                    <a onClick={() => navigate("/admin-login")}>Admin</a>
              </div>
            </div>
         </div>
     </div>
    );
};

export default Welcome;