import React, { useState } from "react";

const AcademicIssuePage = () => {
    const [selectedCourse, setSelectedCourse] = useState("");
    const [successMessage, setSuccessMessage] = useState(false);

    const courses = [
        { value: "BSCS", label: "Bachelor of Science in Computer Science" },
        { value: "BIST", label: "Bachelor of Information Systems and Technology" },
        { value: "IT", label: "Bachelor of Information Technology" },
        { value: "BSSE", label: "Bachelor of Science in Software Engineering" },
        { value: "BLIS", label: "Bachelor of Library and Information Science" },
        { value: "BRAM", label: "Bachelor of Records and Archives Management" },
    ];

    const years = [1, 2, 3, 4];
    const semesters = [1, 2];

    const handleSubmit = (event) => {
        event.preventDefault();
        setSuccessMessage(true);
        setTimeout(() => setSuccessMessage(false), 3000);
    };

    return (
        <div className="container">
            <h2>Report Academic Issue</h2>
            <form onSubmit={handleSubmit}>
                <label>Select School:</label>
                <select required>
                    <option value="">-- Select School --</option>
                    <option value="SCIT">School of Computing and Informatics Technology</option>
                    <option value="EALIS">East African School of Library and Information Science</option>
                </select>

                <label>Select Department:</label>
                <select required>
                    <option value="">-- Select Department --</option>
                    <option value="1">Department of Computer Science</option>
                    <option value="2">Department of Information Systems</option>
                    <option value="3">Department of Information Technology</option>
                    <option value="4">Department of Networks</option>
                    <option value="5">Department of Library & Information Sciences</option>
                    <option value="6">Department of Records & Archives Management</option>
                </select>

                <label>Select Course:</label>
                <select onChange={(e) => setSelectedCourse(e.target.value)} required>
                    <option value="">-- Select Course --</option>
                    {courses.map((course) => (
                        <option key={course.value} value={course.value}>{course.label}</option>
                    ))}
                </select>

                <label>Year of Study:</label>
                <select required>
                    <option value="">-- Select Year --</option>
                    {years.map((year) => (
                        <option key={year} value={year}>{year} Year ({selectedCourse})</option>
                    ))}
                </select>

                <label>Select Semester:</label>
                <select required>
                    <option value="">-- Select Semester --</option>
                    {semesters.map((semester) => (
                        <option key={semester} value={semester}>Semester {semester}</option>
                    ))}
                </select>

                <label>Issue Details:</label>
                <textarea rows="4" required></textarea>

                <button type="submit">Submit</button>
            </form>
            {successMessage && <p className="success-message">Issue submitted successfully!</p>}
        </div>
    );
};

export default AcademicIssuePage;
