import React, {useState} from 'react';
import { Link } from "react-router-dom";
import './Navbar.css';
import { Button } from './buttons';

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
        <Link to='/dashboard' className='nav-links' onClick={closeMobileMenu}>
          Dashboard
        </Link>
      </li>
      <li className='nav-item'>   
        <Link to='/notifications' className='nav-links' onClick={closeMobileMenu}>
          Notifications
        </Link>
      </li>
      <li className='nav-item'>   
        <Link to='/issues' className='nav-links' onClick={closeMobileMenu}>
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
