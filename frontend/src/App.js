
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from './components/Navbar';
import { BrowserRouter as Router,Routes,Route} from 'react-router-dom';
import StudentDashboard from './pages/studentDashboard';
import Login from "./pages/loginpage";
import AcademicIssuePage from './pages/issue';
import Home from './pages/home';

function App() {
  return (
    <>
    <Router>
      <Navbar/>
      <Routes>
        <Route path='/' exact component={Home}/>
        <Route path='/fetchdata' component={FetchData}/> 
      </Routes>
      <Routes>
        <Route path='login' component={Login}/>
      </Routes>
      <Routes>
        <Route path='/StudentDashboard' component={StudentDashboard}/>
      </Routes>
      <Routes>
        <Route path='/issues' component={AcademicIssuePage}/>
      </Routes>

    </Router>
    </>
        
  );
}

function FetchData(){
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('https://jsonplaceholder.typicode.com/posts')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h2>Fetched Data</h2>
      <ul>
        {data.slice(0, 5).map((item) => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;
