import { render, screen, fireEvent } from '@testing-library/react';
import LoginPage from '../AITS/LoginPage'; // Ensure correct import path
import authService from '../services/authService';
import { MemoryRouter } from 'react-router-dom';

// Mock the authService
jest.mock('../services/authService');

describe('LoginPage', () => {
  test('submits login form and calls authService.login', async () => {
    const fakeToken = { access: 'fake-token' };
    authService.login.mockResolvedValue({ data: fakeToken });

    render(
      <MemoryRouter>
        <LoginPage />
      </MemoryRouter>
    );

    // Fill in the form fields
    fireEvent.change(screen.getByPlaceholderText('📧 Webmail'), {
      target: { value: 'test@example.com' },
    });
    fireEvent.change(screen.getByPlaceholderText('🔒 Password'), {
      target: { value: 'password123' },
    });

    // Find the form and submit it
    const form = screen.getByRole('form');
    fireEvent.submit(form);

    // Expect authService.login to be called
    expect(authService.login).toHaveBeenCalledTimes(1);
    expect(authService.login).toHaveBeenCalledWith({
      email: 'test@example.com',
      password: 'password123',
    });

    // Expect to navigate (or reload the page as specified)
    expect(window.location.reload).toHaveBeenCalled();
  });
});
