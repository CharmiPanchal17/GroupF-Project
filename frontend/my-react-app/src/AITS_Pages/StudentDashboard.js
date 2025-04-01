import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./StudentDashboard.css";


const StudentDashboard = ({ user = {} }) => {
  

  const [courseUnits, setCourseUnits] = useState([
    { name: "Mathematics", status: "resolved"},
    { name: "Computer literacy", status: "pending"},
    { name: "Programming", status: "denied"},
    { name: "Robotics", status: "pending"},
    { name: "Networking", status: "resolved"}
  ]);

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("Submitted Issues Data:", courseUnits);
    alert("Issues updated successfully!");
  };

  return (
    <div className="dashboard-container">
      <h1>Student Dashboard</h1>
      <h2>Hi, {user?.firstName || "Student"}! 👋</h2>
      <p>Track and update your issue resolutions.</p>

      <form onSubmit={handleSubmit}>
        <table>
          <thead>
            <tr>
              <th>Course</th>
              <th>Status</th>
              <th>Comment</th>
            </tr>
          </thead>
          <tbody>
            {courseUnits.map((course, index) => (
              <tr key={index} className={course.status}>
                <td>{course.name}</td>
                <td>{course.status}</td>
                <td>{course.comment}</td>      
              </tr>
            ))}
          </tbody>
        </table>

        <button type="submit">Update Issues</button>
      </form>

      
      <button className="report-btn">
  <Link to="/AcademicIssuePage" className="report-btn-link">Report an Issue</Link>
</button>
    </div>
  );
};

export default StudentDashboard;