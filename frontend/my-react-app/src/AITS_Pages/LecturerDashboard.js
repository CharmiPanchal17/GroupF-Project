import React, { useEffect, useState } from "react";
import "./LecturerDashboard.css";
import { FetchIssues, ResolveIssue } from "../services/issueService";

const LecturerDashboard = () => {


  const [issues, setIssues] = useState([]);

  console.log(issues)

  const handleInputChange = (index, value, id) => {
    const updatedIssues = [...issues];
    ResolveIssue(id)
    updatedIssues[index].status = value;
    setIssues(updatedIssues);
  };

  useEffect(() => {
    FetchIssues(setIssues)
  }, [])

  return (
    <div className="dashboard-container">
      <h2 className="title">ASSIGNED ISSUES</h2>
      <div className="course-section">
        <h3>COURSE: IT</h3>
        <table>
          <thead>
            <tr>
              <th>STUDENT NO.</th>
              <th>ISSUE DETAILS</th>
              <th>STATUS</th>
              <th>ACTION</th>
            </tr>
          </thead>
          <tbody>
            {issues.map((issue, index) => (
                <tr key={index} >
                  <td>{issue.student_details?.student_no}</td>
                  <td>{issue.issue_details}</td>
                  <td>{issue.status}</td>
                  <td>
                    <select
                      value={issue.status}
                      onChange={(e) => handleInputChange(index, e.target.value, issue.id)}
                    >
                      <option value="resolved">Resolved</option>
                      <option value="pending">Pending</option>
                      {/* you didnt put an alternative for in progress and that is why this is commented out.  */}
                      {/* <option value="in_progress">In Progress</option> */}
                      /</select>
                  </td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>


    </div>
  );
};

export default LecturerDashboard;
