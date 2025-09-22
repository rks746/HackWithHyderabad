import { useState } from 'react';
import { predictImage } from '../api/client';

export default function UploadForm({ onResult }) {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) return;
        setLoading(true);
        setError(null);
        try {
            const res = await predictImage(file);
            onResult(res);
        } catch (err) {
            setError(err?.message || 'Upload failed');
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
            <input type="file" accept="image/*" onChange={(e) => setFile(e.target.files?.[0] || null)} />
            <button type="submit" disabled={!file || loading}>{loading ? 'Uploading...' : 'Predict'}</button>
            {error && <span style={{ color: 'red' }}>{error}</span>}
        </form>
    );
}


