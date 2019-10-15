import axios from "axios"

const service = axios.create({
    baseURL: 'http://192.168.150.38:5000/api1',
    //baseURL: 'online',
    withCredentials: true,
    timeout: 60000
});

export default service;