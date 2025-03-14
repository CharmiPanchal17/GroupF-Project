import React, {useState} from 'react';
import { Link } from "react-router-dom";
import './Navbar.css';
import { Button } from './Button';
import StudentDashboard from '../pages/studentDashboard';
import AcademicIssuePage from '../pages/issue';
import Login from '../pages/loginpage';

function Navbar() {
const {click, setClick} = useState(false);
const handleClick = () => setClick(!click);
const closeMobileMenu = () => setClick(false);
const [button, setButton] = useState(true);
const showButton = () => {
    if(window.innerWidth <= 960) {
        setButton(false);
    } else {
        setButton(true);
    }
}
window.addEventListener('resize', showButton);
  return (
   <>
   <nav className='navbar'> 
    <div className='navbar-container'>
        <Link to='/' className='navbar-logo'>
        AITS<i className='fab fa-typo3'/>
        </Link>
        <div className='menu-icon' onClick={handleClick}> 
            <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
    </div> 
    <ul className={click ? 'nav-menu active' : 'nav-menu'}>  
      <li className='nav-item'>   
        <Link to='/' className='nav-links' onClick={closeMobileMenu}>
          Home
        </Link>
      </li>
      <li className='nav-item'>   
        <Link to='/StudentDashboard' className='nav-links' onClick={StudentDashboard}>
          Dashboard
        </Link>
      </li>
      <li className='nav-item'>   
        <Link to='/notifications' className='nav-links' onClick={closeMobileMenu}>
          Notifications
        </Link>
      </li>
      <li className='nav-item'>   
        <Link to='/issue' className='nav-links' onClick={AcademicIssuePage}>
          Issues
        </Link>
      </li>
    </ul>
    {button && <Button buttonStyle='btn--outline'>Login</Button>}  
    </div>
   </nav>
   </>
  )
}

export default Navbar
