from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import FileResponse

app = FastAPI()

# Vite builds the UI into ui/dist (see ui/vite.config.ts). Resolve it relative
# to this file so the API can be started from any working directory.
UI_DIST_DIR = Path(__file__).resolve().parent.parent / "ui" / "dist"

templates = Jinja2Templates(directory=str(UI_DIST_DIR))
# Vite emits hashed assets under dist/assets and references them at /assets/*.
# check_dir=False lets the API start before the UI has been built.
app.mount(
    '/assets',
    StaticFiles(directory=str(UI_DIST_DIR / "assets"), check_dir=False),
    'assets',
)


@app.get('/api/health')
async def health():
    return { 'status': 'healthy' }


@app.get("/{rest_of_path:path}")
async def react_app(req: Request, rest_of_path: str):
    # Serve real files from the build root (Vite copies ui/public/* here, e.g.
    # favicons and logos). Resolving and checking the parent guards against
    # path traversal like /..%2f..%2fetc/passwd escaping UI_DIST_DIR.
    if rest_of_path:
        candidate = (UI_DIST_DIR / rest_of_path).resolve()
        if candidate.is_relative_to(UI_DIST_DIR) and candidate.is_file():
            return FileResponse(candidate)
    # Anything else is a client-side route; let React Router handle it.
    return templates.TemplateResponse(req, 'index.html')
