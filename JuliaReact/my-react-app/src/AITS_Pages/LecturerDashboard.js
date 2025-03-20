import React from "react";
import "./LecturerDashboard.css";
const LecturerDashboard = () => {
  const issues = [
    {
      course: "CSC1100",
      assigned: [
        { student: "2406787436", issue: "MISSING MARKS", due: "13/03/2025" },
        { student: "2378745435", issue: "REMARKING", due: "17/02/2025" },
      ],
    },
    {
      course: "BSE1209",
      assigned: [{ student: "2209867556", issue: "WRONG MARKS", due: "20/05/2025" }],
    },
  ];

  return (
    <div className="dashboard-container">
      <h2 className="title">ASSIGNED ISSUES</h2>

      {issues.map((course, index) => (
        <div key={index} className="course-section">
          <h3>COURSE: {course.course}</h3>
          <table>
            <thead>
              <tr>
                <th>STUDENT NO.</th>
                <th>ISSUE</th>
                <th>DUE DATE</th>
              </tr>
            </thead>
            <tbody>
              {course.assigned.map((item, idx) => (
                <tr key={idx}>
                  <td>{item.student}</td>
                  <td>{item.issue}</td>
                  <td>{item.due}</td>
                </tr>
              ))}
              {/* Empty rows for additional spacing */}
              {[...Array(3)].map((_, idx) => (
                <tr key={`empty-${idx}`}>
                  <td>-------</td>
                  <td>-------</td>
                  <td>-------</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ))}

      <div className="stats">
        <p>ASSIGNED ISSUES: 15</p>
        <p>RESOLVED ISSUES: 06</p>
        <p>PENDING ISSUES: 09</p>
        <p>MISSING MARKS: 11</p>
        <p>REMARKING: 02</p>
        <p>WRONG MARKS: 02</p>
      </div>
    
    </div>
  );
};

export default LecturerDashboard;

  