import { render, screen, fireEvent } from '@testing-library/react';
import RegisterPage from '../AITS_Pages/RegisterPage';
import authService from '../services/authService';
import { MemoryRouter } from 'react-router-dom';

// Mock the authService
jest.mock('../services/authService');

describe('RegisterPage', () => {
  test('submits registration form and calls authService.register', async () => {
    const fakeToken = { access: 'fake-token' };
    authService.register.mockResolvedValue({ data: fakeToken });

    render(
      <MemoryRouter>
        <RegisterPage />
      </MemoryRouter>
    );

    // Fill in the form fields
    fireEvent.change(screen.getAllByPlaceholderText('👤 Username'), {
        target: { value:  'test2example.com' },
    })

    fireEvent.change(screen.getAllByPlaceholderText('👥 FullName'), {
        target: { value:  'test2example.com' },
    })

    fireEvent.change(screen.getAllByPlaceholderText('#️⃣ Student Number'), {
        target: { value:  'test2example.com' },
    })

    fireEvent.change(screen.getAllByPlaceholderText('#️⃣ Registration Number'), {
        target: { value:  'test2example.com' },
    })

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
    expect(authService.register).toHaveBeenCalledTimes(1);
    expect(authService.register).toHaveBeenCalledWith({
      email: 'test@example.com',
      password: 'password123',
    });

    // Expect to navigate (or reload the page as specified)
    expect(window.location.reload).toHaveBeenCalled();
  });
});
