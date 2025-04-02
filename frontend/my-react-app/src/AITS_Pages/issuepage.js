import React, { useState } from "react";
import "./AcademicIssuePage.css";

const AcademicIssuePage = () => {
    const [selectedCourse, setSelectedCourse] = useState("");
    const [selectedSchool, setSelectedSchool] = useState("");
    const [successMessage, setSuccessMessage] = useState(false);

    const courses = {
        SCIT: [
            { value: "BSCS", label: "Bachelor of Science in Computer Science" },
            { value: "BIST", label: "Bachelor of Information Systems and Technology" },
            { value: "IT", label: "Bachelor of Information Technology" },
            { value: "BSSE", label: "Bachelor of Science in Software Engineering" },
        ],
        EALIS: [
            { value: "BLIS", label: "Bachelor of Library and Information Science" },
            { value: "BRAM", label: "Bachelor of Records and Archives Management" },
        ],
    };

    const departments = {
        SCIT: [
            { value: "1", label: "Department of Computer Science" },
            { value: "2", label: "Department of Information Systems" },
            { value: "3", label: "Department of Information Technology" },
            { value: "4", label: "Department of Networks" },
        ],
        EALIS: [
            { value: "5", label: "Department of Library & Information Sciences" },
            { value: "6", label: "Department of Records & Archives Management" },
        ],
    };

    const years = [1, 2, 3, 4];
    const semesters = [1, 2];

    const handleSubmit =(event) => {
        event.preventDefault();
       };

        try {
            const response=("issues");
            console.log("Issue submitted:", response.data);

        setSuccessMessage(true);
        setTimeout(() => setSuccessMessage(false), 3000);
        }
        catch (error) {
            console.error("Error submitting issue:", error);
            setSuccessMessage(false);
        }
    
     return (
        <div className="container">
            <h2>COCIS Academic Issue Report</h2>
            <form onSubmit={handleSubmit}>
                <label>Select School:</label>
                <select onChange={(e) => setSelectedSchool(e.target.value)} required>
                    <option value="">-- Select School --</option>
                    <option value="SCIT">School of Computing and Informatics Technology</option>
                    <option value="EALIS">East African School of Library and Information Science</option>
                </select>

                <label>Select Department:</label>
                <select required>
                    <option value="">-- Select Department --</option>
                    {selectedSchool && departments[selectedSchool].map((dept) => (
                        <option key={dept.value} value={dept.value}>{dept.label}</option>
                    ))}
                </select>

                <label>Select Course:</label>
                <select onChange={(e) => setSelectedCourse(e.target.value)} required>
                    <option value="">-- Select Course --</option>
                    {selectedSchool && courses[selectedSchool].map((course) => (
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

                <label>Course Unit:</label>
                <textarea rows="1" required></textarea>

                <label>Lecturer's Name:</label>
                <textarea rows="1" required></textarea>

                <label>Issue Details:</label>
                <textarea rows="3" required></textarea>

                <button type="submit">Submit</button>
            </form>
            {successMessage && <p className="success-message">Issue submitted successfully!</p>}
            
            </div>
        );
    };


export default AcademicIssuePage;
