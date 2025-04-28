import axios from 'axios';
const axiosInstance=axios.create({
    baseURL:'https://localhost:8000/api',
    timeout: 5000,
    headers:{
        'Content-Type':'application/json',
    },
    withCredentials:true,
});

export default axiosInstance;