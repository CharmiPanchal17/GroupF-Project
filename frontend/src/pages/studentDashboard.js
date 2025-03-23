import { useState } from "react";
import { useNavigate } from "react-router-dom";

const StudentDashboard = ({ user }) => {
  const navigate = useNavigate();

  // Mock data for course units
  const [courseUnits, setCourseUnits] = useState([
    { name: "Mathematics", status: "resolved" },
    { name: "Computer literacy", status: "pending" },
    { name: "Programming", status: "denied" },
    { name: "Robotics", status: "pending" },
    { name: "Networking", status: "resolved" }
  ]);

  return (
    <div style={{ padding: "20px", textAlign: "center" }}>
      <h1>Student Dashboard</h1>
      <h2>Hi, {user.firstName}! 👋</h2>
      <p>Track your issue resolutions.</p>

      {/* Display Resolved Course Units */}
      <h3>Resolved Issues</h3>
      <ul>
        {courseUnits.filter(course => course.status === "resolved").length > 0 ? (
          courseUnits
            .filter(course => course.status === "resolved")
            .map((course, index) => <li key={index}>{course.name}</li>)
        ) : (
          <p>No resolved issues.</p>
        )}
      </ul>

      {/* Display Pending Course Units */}
      <h3>Pending Issues</h3>
      <ul>
        {courseUnits.filter(course => course.status === "pending").length > 0 ? (
          courseUnits
            .filter(course => course.status === "pending")
            .map((course, index) => <li key={index}>{course.name}</li>)
        ) : (
          <p>No pending issues.</p>
        )}
      </ul>

      {/* Display Denied Course Units */}
      <h3>Denied Issues</h3>
      <ul>
        {courseUnits.filter(course => course.status === "denied").length > 0 ? (
          courseUnits
            .filter(course => course.status === "denied")
            .map((course, index) => <li key={index}>{course.name}</li>)
        ) : (
          <p>No denied issues.</p>
        )}
      </ul>

      {/* Button to Report an Issue */}
      <button
        onClick={() => navigate("/complaint")}
        style={{ marginTop: "20px", padding: "10px 20px", fontSize: "16px", cursor: "pointer" }}
      >
        Report an Issue
      </button>
    </div>
  );
};

export default StudentDashboard;
