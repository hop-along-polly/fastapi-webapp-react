from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="../ui/build")
app.mount('/static', StaticFiles(directory="../ui/build/static"), 'static')


@app.get('/api/health')
async def health():
    return { 'status': 'healthy' }


@app.get("/{rest_of_path:path}")
async def react_app(req: Request, rest_of_path: str):
    print(f'Rest of path: {rest_of_path}')
    return templates.TemplateResponse('index.html', { 'request': req })
