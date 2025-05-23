//const myBaseURL = 'https://127.0.0.1:8000/';

const IsDevelpopment = import.meta.env.MODE === 'development';
const myBaseURL = IsDevelpopment ? import.meta.env.REACT_APP_API_URL_LOCAL : import.meta.env.REACT_APP_API_URl_DEPLOY;

import axios from 'axios';
const axiosInstance=axios.create({
    baseURL: myBaseURL,
    timeout: 5000,
    headers:{
        'Content-Type':'application/json',
    },
    withCredentials:true,
});

export default axiosInstance;