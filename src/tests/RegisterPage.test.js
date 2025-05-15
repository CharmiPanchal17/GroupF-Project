import { render, screen, fireEvent } from '@testing-library/react';
import RegisterPage from '../AITS_Pages/RegisterPage';
import authService from '../services/authService';
import { MemoryRouter } from 'react-router-dom';

// Mock the authService
jest.mock('../services/authService');

describe('RegisterPage', () => {
  test('submits registration form and calls authService.register', async () => {
    const fakeResponse = { access: 'fake-token' };
    authService.register.mockResolvedValue({ data: fakeResponse });

    render(
      <MemoryRouter>
        <RegisterPage />
      </MemoryRouter>
    );

    // Fill in the form fields
    fireEvent.change(screen.getByPlaceholderText('👤 Username'), {
      target: { value: 'testuser' },
    });

    fireEvent.change(screen.getByPlaceholderText('👥 FullName'), {
      target: { value: 'Test User' },
    });

    fireEvent.change(screen.getByPlaceholderText('#️⃣ Student Number'), {
      target: { value: '12345678' },
    });

    fireEvent.change(screen.getByPlaceholderText('#️⃣ Registration Number'), {
      target: { value: 'REG12345' },
    });

    fireEvent.change(screen.getByPlaceholderText('📧 Webmail'), {
      target: { value: 'test@example.com' },
    });

    fireEvent.change(screen.getByPlaceholderText('🔒 Password'), {
      target: { value: 'password123' },
    });

    // Find the form and submit it
    const form = screen.getByRole('form');
    fireEvent.submit(form);

    // Assert that authService.register was called with the correct data
    expect(authService.register).toHaveBeenCalledTimes(1);
    expect(authService.register).toHaveBeenCalledWith({
      username: 'testuser',
      fullName: 'Test User',
      studentNumber: '12345678',
      registrationNumber: 'REG12345',
      email: 'test@example.com',
      password: 'password123',
    });

    // Assert that the page reloads or navigates
    expect(window.location.reload).toHaveBeenCalled();
  });
});