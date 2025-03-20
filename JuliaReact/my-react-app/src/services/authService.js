// src/services/authService.js

import axios from 'axios';

const API_URL = 'http://localhost:8000/api/token/';

const login = async (username, password) => {
    const response = await axios.post(API_URL, { username, password });
    if (response.data) {
        localStorage.setItem('token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
    }
    return response.data;
};

const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('refresh_token');
};

const getAccessToken = () => {
    return localStorage.getItem('token');
};

const refreshAccessToken = async () => {
    const refreshToken = localStorage.getItem('refresh_token');
    if (refreshToken) {
        const response = await axios.post('http://localhost:8000/api/token/refresh/', { refresh: refreshToken });
        localStorage.setItem('token', response.data.access);
        return response.data.access;
    }
    return null;
};

export default {
    login,
    logout,
    getAccessToken,
    refreshAccessToken,
};
