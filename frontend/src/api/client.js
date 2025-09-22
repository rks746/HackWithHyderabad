import axios from 'axios';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE || 'http://127.0.0.1:5000',
    withCredentials: false,
});

export const predictImage = async (file) => {
    const form = new FormData();
    form.append('image', file);
    const res = await api.post('/predict', form, {
        headers: { 'Content-Type': 'multipart/form-data' },
    });
    return res.data;
};

export const sendFeedback = async (note) => {
    const res = await api.post('/feedback', { note });
    return res.data;
};

export default api;


