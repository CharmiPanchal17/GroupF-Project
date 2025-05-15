// src/tests/WelcomePage.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import WelcomePage from '../AITS_Pages/WelcomePage';

jest.mock('../components/Navbar', () => () => <div>Mocked Navbar</div>);

describe('WelcomePage', () => {
  beforeEach(() => {
    render(
      <MemoryRouter>
        <WelcomePage />
      </MemoryRouter>
    );
  });

  it('renders the welcome header', () => {
    expect(screen.getByText(/WELCOME TO AITS/i)).toBeInTheDocument();
    expect(screen.getByText(/Your comprehensive academic management system/i)).toBeInTheDocument();
  });

  it('displays all user categories', () => {
    expect(screen.getByText('Students')).toBeInTheDocument();
    expect(screen.getByText('Lecturers')).toBeInTheDocument();
    expect(screen.getByText('Registrars')).toBeInTheDocument();
  });

  it('has login and register links for students', () => {
    expect(screen.getAllByText('Login')[0]).toHaveAttribute('href', '/login');
    expect(screen.getByText('Register')).toHaveAttribute('href', '/register');
  });

  it('has login and register links for lecturers', () => {
    expect(screen.getAllByText('Login')[1]).toHaveAttribute('href', '/login');
    expect(screen.getByText('Register', { selector: 'a[href="/LecRegisterPage"]' })).toBeInTheDocument();
  });

  it('has login and register links for registrars', () => {
    expect(screen.getByText('Login', { selector: 'a[href="Registardashboard"]' })).toBeInTheDocument();
    expect(screen.getByText('Register', { selector: 'a[href="/registrar-signup"]' })).toBeInTheDocument();
  });

  it('renders the footer', () => {
    expect(screen.getByText(/© 2025 AITS. All rights reserved/i)).toBeInTheDocument();
  });
});
