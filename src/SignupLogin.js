import React,{useState} from "react";
import { useNavigate } from "react-router-dom";
import './SignupLogin.css'

function Signup() {
    const [formData, setFormData] = useState({
      userName: "",
      email: "",
      studentNumber: "",
      password: "",
    });

    const [error, setError] = useState("")
    const navigate = useNavigate();
    const handleChange = (e) => {
        setFormData({ ...formData,[e.target.name]: e.target.value
         });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!/^\d{10}$/.test(formData.studentNumber)) {setError("student number must be exactly 10 digits.");
            return;
        }
        setError("");
        console.log("user signed up:", formData);
        navigate("/login");
    
    };
    return (
        <div>
            <h2>Signup</h2>
            {error && <p style={{ color: "red" }}> {error} </p>}
            <form onSubmit={handleSubmit}>
                <input type="text" name="userName" placeholder="Username"
                onChange={handleChange} required />
                <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
                <input type="text" name="studentNumber" placeholder="Student Number" onChange={handleChange} />
                <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
                <button type="submit">Singup</button>
            </form>
        </div>
    );
}
export default Signup;  
