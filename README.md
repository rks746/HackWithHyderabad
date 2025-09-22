Full-stack React + Flask (mock object detection)

Backend (Flask)
- Location: `backend/`
- Create venv and install deps:
  - Windows PowerShell:
    - `cd backend`
    - `python -m venv .venv`
    - `. .\.venv\Scripts\Activate.ps1`
    - `pip install -r requirements.txt`
- Run:
  - `python wsgi.py`
- Endpoints:
  - `POST /predict` form-data `image`: returns mock boxes and `annotated_image_url`
  - `GET  /annotated/<filename>`: serves annotated image
  - `POST /feedback` json `{ note: string }`: returns `{ status, feedback_id }`

Frontend (Vite + React + TS)
- Location: `frontend/`
- Configure API base in `frontend/.env.local`:
  - `VITE_API_BASE=http://127.0.0.1:5000`
- Install and run:
  - `cd frontend`
  - `npm install`
  - `npm run dev`

Notes
- CORS is enabled in Flask; adjust origins for production.
- The detection logic is mocked. Replace in `backend/app/routes.py` with real YOLO inference later.


