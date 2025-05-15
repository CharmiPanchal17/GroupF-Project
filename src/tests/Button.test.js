import { render, screen, fireEvent } from '@testing-library/react';
import Button from '../components/Button'; // adjust if needed

test('calls onClick when button is clicked', () => {
  const handleClick = jest.fn();

  render(
    <Button onClick={handleClick} buttonStyle="btn--primary" buttonSize="btn--medium">
      Click Me
    </Button>
  );

  fireEvent.click(screen.getByText(/click me/i));
  expect(handleClick).toHaveBeenCalledTimes(1);
});
