export default function ResultsDisplay({ result }) {
    if (!result) return null;
    const base = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:5000';
    return (
        <div style={{ marginTop: 16 }}>
            <h3>Detection Result</h3>
            <pre style={{ background: '#f6f8fa', padding: 12, borderRadius: 6 }}>{JSON.stringify(result.boxes, null, 2)}</pre>
            {result.annotated_image_url && (
                <img src={`${base}${result.annotated_image_url}`} alt="annotated" style={{ maxWidth: '100%', border: '1px solid #ddd', borderRadius: 6 }} />
            )}
        </div>
    );
}


