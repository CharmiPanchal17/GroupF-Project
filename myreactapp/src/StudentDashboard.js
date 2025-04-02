import { userState } from "react"
import { useNavigate } from "react-router-dom"

const StudentDashboard = ({ user }) =>
    {
        const navigate = useNavigate();
//data for course units
        const [courseUnits, setCourseUnits] = useState([
            { name: "Statistics", status: "resolved"},
            {name: "Computer literacy", status: "resolved"},
            {name: "Programming", status: "pending"},
            {name: "Robotics", status: "denied"}
        ]);

        return (
            <div style={{ padding: "20px", textAlign: "centre" }}>
                <h1>Student Dashboard</h1>
                <h2> Hi, {user.username}! </h2>
                <p>Track your issueresolutins with AITS</p>
                <GamepadButton
                onClick={() => navigate("/complaint")}
                style={{ marginTop: "20px",
                    padding: "10px 20px",
                    fontSize: "16px", cursor: "pointer" }}
                    >
                        Submit an issue
                    </GamepadButton>
            </div>
        );
    };

    export default StudentDashboard;
