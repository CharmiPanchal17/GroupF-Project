import { useState } from "react"
import './StudentDashboard.css'
import { useNavigate } from "react-router-dom"

const StudentDashboard = ({ user }) =>
    {
        const navigate = useNavigate();
//data for course units
        const [courseUnits, setCourseUnits] = useState([
            { name: "Statistics", status: "resolved"},
            { name: "Computer literacy", status: "resolved"},
            { name: "Programming", status: "pending"},
            { name: "Robotics", status: "denied"}
        ]);
        console.log(courseUnits);

        return (
            <div style={{ padding: "20px", textAlign: "left" }}>
                <h1>Student Dashboard</h1>
                <h2> Hi, {user?.username || "Student"}! </h2>
                <h3>Track your issue resolutions with AITS</h3>

                <div className="course-units-container">
                    <div className="course-unit-header">
                        <div className="course-unit-name=header">Course unit</div>
                        <div className="course-unit-status-header">Status</div>
                    </div>
                    <ul className="course-units-list">
                        {courseUnits.map((unit, index) => (
                            <li key={index} 
                                className={`course-unit ${
                                    unit.status === "resolved" ? "resolved" : unit.status === "pending" ? "pending" : "denied"}`}
                                   >   
                                   <strong>{unit.name}</strong> - {unit.status}
                            </li>
                        ))}
                        </ul>
                </div>
                <button
                  className="submit-issue-button"
               onClick={() => navigate("/complaint")}>Submit an issue
                    </button>
            </div>
        );
    };

    export default StudentDashboard;
