import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./StudentDashboard.css";


const StudentDashboard = ({ user = {} }) => {
  

  const [courseUnits, setCourseUnits] = useState([
    { name: "Mathematics", status: "resolved", comment: "" },
    { name: "Computer literacy", status: "pending", comment: "" },
    { name: "Programming", status: "denied", comment: "" },
    { name: "Robotics", status: "pending", comment: "" },
    { name: "Networking", status: "resolved", comment: "" }
  ]);

  // Handle input changes
  const handleInputChange = (index, field, value) => {
    const updatedUnits = [...courseUnits];
    updatedUnits[index][field] = value;
    setCourseUnits(updatedUnits);
  };

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
                <td>
                  <select
                    value={course.status}
                    onChange={(e) => handleInputChange(index, "status", e.target.value)}
                  >
                    <option value="resolved">Resolved</option>
                    <option value="pending">Pending</option>
                    <option value="denied">Denied</option>
                  </select>
                </td>
                <td>
                  <input
                    type="text"
                    placeholder="Add a comment"
                    value={course.comment}
                    onChange={(e) => handleInputChange(index, "comment", e.target.value)}
                  />
                </td>
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