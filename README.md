# WebApp Template w/ FastAPI, React.js and Typescript

This is a template for a Webapp using React.js and Typescript for the UI
(built with [Vite](https://vite.dev/)) and FastAPI as the API.

## Prerequisites

- **Node.js** 20.19+ / 22.12+ (Vite 8 requirement)
- **pnpm** — enable it via the Node-bundled Corepack:
  ```bash
  corepack enable pnpm
  ```
  The required version is pinned in `ui/package.json` (`packageManager`).
- **Python** 3.10+

## Project layout

```
api/    FastAPI backend
ui/     React + TypeScript frontend (Vite)
```

## Local development (recommended)

Run the API and the Vite dev server in two terminals. The Vite dev server
serves the UI with hot-module reload and proxies `/api/*` requests to FastAPI
(configured in `ui/vite.config.ts`).

```bash
# Terminal 1 — API on http://localhost:8000
cd api
pip install -r requirements.txt
uvicorn main:app --reload
```

```bash
# Terminal 2 — UI on http://localhost:3000
cd ui
pnpm install
pnpm dev
```

Open http://localhost:3000. API calls to `/api/*` are proxied to the backend.

## Single-server build

FastAPI can also serve the compiled UI and the API together from one origin
(no proxy needed). Build the UI, then start the API:

```bash
# Build the UI into ui/dist
cd ui
pnpm install
pnpm build
```

```bash
# Serve UI + API from http://localhost:8000
cd api
pip install -r requirements.txt
uvicorn main:app
```

Verify your setup in a browser:

- `localhost:8000/api/health` — returns `{ "status": "healthy" }`
- `localhost:8000/` — returns a web page that says `Home`
- `localhost:8000/test` — returns a web page that says `Test`

## UI scripts

Run from the `ui/` directory:

| Command | Description |
| --- | --- |
| `pnpm dev` | Start the Vite dev server (with API proxy) |
| `pnpm build` | Type-check and build to `ui/dist` |
| `pnpm preview` | Preview the production build locally |
| `pnpm test` | Run the test suite once ([Vitest](https://vitest.dev/)) |
| `pnpm test:watch` | Run tests in watch mode |
| `pnpm lint` | Lint the source |
| `pnpm format` | Format the source with Prettier |
