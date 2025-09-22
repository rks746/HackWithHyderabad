import { useState } from 'react';
import { sendFeedback } from '../api/client';

export default function FeedbackForm() {
    const [note, setNote] = useState('');
    const [status, setStatus] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!note.trim()) return;
        setLoading(true);
        setStatus(null);
        try {
            const res = await sendFeedback(note.trim());
            setStatus(`Thanks! id=${res.feedback_id}`);
            setNote('');
        } catch (err) {
            setStatus(err?.message || 'Failed to send');
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} style={{ display: 'flex', gap: 8, marginTop: 16 }}>
            <input
                type="text"
                placeholder="Feedback about incorrect detection..."
                value={note}
                onChange={(e) => setNote(e.target.value)}
                style={{ flex: 1 }}
            />
            <button type="submit" disabled={!note.trim() || loading}>{loading ? 'Sending...' : 'Send Feedback'}</button>
            {status && <span>{status}</span>}
        </form>
    );
}


