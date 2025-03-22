import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "/.Login.css"

const Login = ({ setUser }) =>{
    const navigate = useNavigate();
    const [credentials, setCredentials] = useState({ studentNumber: "", password: ""});

};
const handleChange = (e) => {
    setCredentials({ ...credentials,[e.target.name]: e.target.value });
    
};

const handleLogin = (e) => {
    e.preventDefault();
    const storedUsers = JSON.parse(localStorage.getItem("users")) || [];
    const user = storedUsers.find(u => u.studentNumber === credentials.studentNumber && u.password === credentials.password);
    
    if (user) {
        setUser({ isAuthenticated: true,firstName: user.name.split("")[0], role: user.role});
        navigate(user.role ==="student" ? "/ student" : user.role ==="lecturer" ? "/lecturer" : "/register");
    }
};

return(
    <div className="login-container">
        <h2>Login</h2>
        <form onSubmit={handleLogin}>
            <input type="email" name= "email" placeholder="Email" onChange={handleChange} required />
            <br />
            <button type="Submit">Login</button>
        </form>
        <p>Dont have an account? <a href="/signup">Signup</a></p>
    </div>
);
export default Login;