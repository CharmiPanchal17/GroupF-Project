import React, { useState } from "react";
import "./LecturerDashboard.css";
const LecturerDashboard = () => {
  const[issues,setIssue]= useState([
    {
      course: "CSC1100",
      assigned: [
        { student: "2406787436", issue: "MISSING MARKS", due: "13/03/2025",status:"resolved" },
        { student: "2378745435", issue: "REMARKING", due: "17/02/2025", status:"pending" },
      ],
    },
    {
      course: "BSE1209",
      assigned: [{ student: "2209867556", issue: "WRONG MARKS", due: "20/05/2025",status:"denied" }],
    },
  ]);
  const handleInputChange = (courseIndex, issueIndex, value) => {
    const updatedIssues = [...issues];
    updatedIssues[courseIndex].assigned[issueIndex].status = value;
    setIssue(updatedIssues);
  };
  const getStatusClass = (status) => {
    switch (status) {
      case "resolved":
        return "resolved";
      case "pending":
        return "pending";
      case "denied":
        return "denied";
      default:
        return "";
    }
  };

  return (
    <div className="dashboard-container">
      <h2 className="title">ASSIGNED ISSUES</h2>

      {issues.map((course, courseIndex) => (
        <div key={courseIndex} className="course-section">
          <h3>COURSE: {course.course}</h3>
          <table>
            <thead>
              <tr>
                <th>STUDENT NO.</th>
                <th>ISSUE</th>
                <th>DUE DATE</th>
                <th>STATUS</th>
              </tr>
            </thead>
            <tbody>
              {course.assigned.map((issue,issueIndex) => (
                <tr key={issueIndex} className={issue.status}>
                  <td>{issue.student}</td>
                  <td>{issue.issue}</td>
                  <td>{issue.due}</td>
                  <td>{issue.status}</td>
                  <td>
                    <select>
                    value={issue.status}
                    onChange={(e) => handleInputChange(courseIndex,issueIndex, e.target.value)}
                      <option value="resolved">Resolved</option>
                      <option value="pending">Pending</option>
                      <option value="denied">Denied</option>
                      /</select>
                  </td>
                </tr>
              ))}
              {/* Empty rows for additional spacing */}
              {[...Array(3)].map((_, idx) => (
                <tr key={`empty-${idx}`}>
                  <td>-------</td>
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
  