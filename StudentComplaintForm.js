// StudentComplaintForm.js (React Component)
import React, { useState } from 'react';
import './StudentComplaintForm.css';

function StudentComplaintForm() {
  const [filePreview, setFilePreview] = useState({
    photo: null,
    pdf: null,
  });

  const previewFile = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();

      reader.onload = (e) => {
        if (file.type.startsWith('image/')) {
          setFilePreview({ photo: e.target.result, pdf: null });
        } else if (file.type === 'application/pdf') {
          setFilePreview({ photo: null, pdf: e.target.result });
        } else {
          alert('Please upload an image or PDF file.');
          setFilePreview({ photo: null, pdf: null });
        }
      };
      reader.readAsDataURL(file);
    } else {
        setFilePreview({ photo: null, pdf: null });
    }
  };

  return (
    <div className="container">
      <h1>STUDENT COMPLAINT</h1>
      <form id="studentForm" encType="multipart/form-data">
        <label htmlFor="name">Full Name:</label>
        <input type="text" id="name" name="name" required />

        <label htmlFor="number">Student Number:</label>
        <input type="number" id="number" name="number" required />

        <label htmlFor="registration_number">Student Registration Number:</label>
        <input type="text" id="registration_number" name="registration_number" required />

        <label htmlFor="email">Student Email:</label>
        <input type="email" id="email" name="email" required />

        <label htmlFor="phone">Student WhatsApp Number:</label>
        <input type="tel" id="phone" name="phone" required />

        <label htmlFor="college">College:</label>
        <input type="text" id="college" name="college" required />

        <label htmlFor="course">Course:</label>
        <input type="text" id="course" name="course" required />

        <label htmlFor="course_unit">Course Unit:</label>
        <input type="text" id="course_unit" name="course_unit" required />

        <label htmlFor="lecturer_email">Lecturer Email:</label>
        <input type="email" id="lecturer_email" name="lecturer_email" required />

        <label htmlFor="essay">What would be your issue? (Max 500 words):</label>
        <textarea id="essay" name="essay" rows="5" required></textarea>

        <label htmlFor="file">Upload an Image or PDF:</label>
        <input type="file" id="file" name="file" accept="image/*,application/pdf" onChange={previewFile} />

        {filePreview.photo && (
          <img id="photo" alt="Uploaded Image Preview" src={filePreview.photo} style={{ width: '100%', maxHeight: '300px', marginTop: '10px' }} />
        )}
        {filePreview.pdf && (
          <iframe id="pdfViewer" src={filePreview.pdf} style={{ width: '100%', height: '400px', marginTop: '10px', border: '1px solid #ccc' }} />
        )}

        <button type="submit">Submit complaint</button>
      </form>
      <p id="responseMessage"></p>
    </div>
  );
}

export default StudentComplaintForm;