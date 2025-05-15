import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import LoginPage from '../AITS_Pages/LoginPage';
import authService from '../services/authService';
import { BrowserRouter } from 'react-router-dom';

// Mock authService
jest.mock('../services/authService', () => ({
  login: jest.fn(),
}));

// Mock navigate
const mockedNavigate = jest.fn();
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: () => mockedNavigate,
}));

describe('LoginPage Component', () => {
  beforeEach(() => {
    // Clear previous mocks before each test
    authService.login.mockClear();
    mockedNavigate.mockClear();
  });

  test('renders login form', () => {
    render(<LoginPage setUser={() => {}} />, { wrapper: BrowserRouter });

    expect(screen.getByPlaceholderText('📧 Webmail')).toBeInTheDocument();
    expect(screen.getByPlaceholderText('🔒 Password')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /login/i })).toBeInTheDocument();
  });

  test('allows input and calls login on submit', async () => {
    const mockToken = { data: { access: 'testtoken' } };
    authService.login.mockResolvedValueOnce(mockToken);

    render(<LoginPage setUser={() => {}} />, { wrapper: BrowserRouter });

    fireEvent.change(screen.getByPlaceholderText('📧 Webmail'), {
      target: { value: 'user@example.com', name: 'email' },
    });

    fireEvent.change(screen.getByPlaceholderText('🔒 Password'), {
      target: { value: 'password123', name: 'password' },
    });

    const loginButton = screen.getByRole('button', { name: /login/i });

    fireEvent.click(loginButton);

    expect(authService.login).toHaveBeenCalledWith({
      email: 'user@example.com',
      password: 'password123',
    });
  });

  test('navigates to dashboard on login', async () => {
    const mockToken = { data: { access: 'testtoken' } };
    authService.login.mockResolvedValueOnce(mockToken);

    render(<LoginPage setUser={() => {}} />, { wrapper: BrowserRouter });

    fireEvent.change(screen.getByPlaceholderText('📧 Webmail'), {
      target: { value: 'user@example.com', name: 'email' },
    });

    fireEvent.change(screen.getByPlaceholderText('🔒 Password'), {
      target: { value: 'password123', name: 'password' },
    });

    fireEvent.click(screen.getByRole('button', { name: /login/i }));

    // Wait for mocked login
    await screen.findByRole('button'); // Forces wait

    expect(authService.login).toHaveBeenCalledTimes(1);
    expect(mockedNavigate).toHaveBeenCalledWith('/StudentDashboard');
  });
});
