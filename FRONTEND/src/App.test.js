import { render, screen } from '@testing-library/react';
import App from '../../../../Group-F/FRONTEND/src/App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
