import React from "react";

const LecturerDashboard = () => {
  const issuesData = [
    {
      course: "CSC1100",
      issues: [
        { studentNo: "2406787436", issue: "MISSING MARKS", dueDate: "13/03/2025" },
        { studentNo: "2378745435", issue: "REMARKING", dueDate: "17/02/2025" },
      ],
    },
    {
      course: "BSE1209",
      issues: [
        { studentNo: "22098675567", issue: "WRONG MARKS", dueDate: "20/05/2025" },
      ],
    },
  ];

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-2xl font-bold text-blue-500 mb-4">ASSIGNED ISSUES</h1>
      
      {issuesData.map((courseData, index) => (
        <div key={index} className="mb-6">
          <h2 className="text-lg font-semibold mb-2">COURSE: {courseData.course}</h2>
          <div className="overflow-x-auto">
            <table className="w-full border border-gray-300">
              <thead>
                <tr className="bg-gray-200 text-gray-700">
                  <th className="border px-4 py-2">STUDENT NO.</th>
                  <th className="border px-4 py-2">ISSUE</th>
                  <th className="border px-4 py-2">DUE DATE</th>
                </tr>
              </thead>
              <tbody>
                {courseData.issues.map((issue, i) => (
                  <tr key={i} className="text-center border">
                    <td className="border px-4 py-2">{issue.studentNo}</td>
                    <td className="border px-4 py-2">{issue.issue}</td>
                    <td className="border px-4 py-2">{issue.dueDate}</td>
                  </tr>
                ))}
                {/* Empty Rows for Consistency */}
                {[...Array(3 - courseData.issues.length)].map((_, i) => (
                  <tr key={`empty-${i}`} className="text-center border">
                    <td className="border px-4 py-2">-------</td>
                    <td className="border px-4 py-2">-------</td>
                    <td className="border px-4 py-2">-------</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      ))}

      <div className="text-gray-600 mt-4">
        <p>ASSIGNED ISSUES: 15</p>
        <p>RESOLVED ISSUES: 06</p>
        <p>PENDING ISSUES: 09</p>
      </div>

      <div className="text-gray-600 mt-4">
        <p>MISSING MARKS: 11</p>
        <p>REMARKING: 02</p>
        <p>WRONG MARKS: 02</p>
      </div>
    </div>
  );
};

export default LecturerDashboard;
