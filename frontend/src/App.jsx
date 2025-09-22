import { useState } from 'react'
import './App.css'
import UploadForm from './components/UploadForm'
import ResultsDisplay from './components/ResultsDisplay'
import FeedbackForm from './components/FeedbackForm'

function App() {
  const [result, setResult] = useState(null)

  return (
    <div style={{ maxWidth: 800, margin: '40px auto', padding: 16 }}>
      <h2>Object Detection Demo (Mock)</h2>
      <UploadForm onResult={setResult} />
      <ResultsDisplay result={result} />
      <FeedbackForm />
    </div>
  )
}

export default App


