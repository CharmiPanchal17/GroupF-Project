import { render, screen, fireEvent } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import Navbar from '../components/Navbar'; // Adjust the path if needed

test('calls onClick when a link in the Navbar is clicked', () => {
  const handleClick = jest.fn();

  render(
    <BrowserRouter>
      <Navbar />
    </BrowserRouter>
  );

  // Simulate clicking a link in the Navbar
  const linkElement = screen.getByText(/home/i); // Replace "home" with the actual text of a link in your Navbar
  fireEvent.click(linkElement);

  // Assert that the click handler was called
  expect(handleClick).toHaveBeenCalledTimes(1);
});