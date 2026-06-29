from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

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
    return templates.TemplateResponse('index.html', { 'request': req })
