# WebApp Template w/ FastAPI, React.js and Typescript

    This is a template for a Webapp using React.js and Typescript for the UI and FastAPI as the API.

# Getting Started

1. Install UI dependencies and build app
```bash
# run from ui/ directory
npm install
npm run build
```
2. Install API dependencies
```bash
# run from api/ directory
pip install -r requirements.txt
```
3. Start the API
```bash
# run from api/ directory
uvicorn main:app --reload
```
4. Test your setup
 - In a browser navigate to
    - `localhost:8000/api/health` this should return `{ "status": "healthy" }`
    - `localhost:8000/` this should return a web page that says `Home`
    - `localhost:8000/test` this should return a web page that says `Test`
