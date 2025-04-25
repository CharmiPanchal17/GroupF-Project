import { render, screen, fireEvent } from '@testing-library/react';
import Navbar from '../components/Navbar'; // adjust if needed
import { Link } from 'react-router-dom';

test('calls onClick when link is clicked', () => {
  const handleClick = jest.fn();

  render(
    <Link onClick={handleClick} buttonStyle="btn--primary" buttonSize="btn--medium">
      Click Me
    </Link>
  );

  fireEvent.click(screen.getByText(/click me/i));
  expect(handleClick).toHaveBeenCalledTimes(1);
});
