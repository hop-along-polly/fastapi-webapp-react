/// <reference types="vitest/config" />
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    // Local dev: Vite serves the UI on :3000 and proxies API calls to the
    // FastAPI backend on :8000. This replaces CRA's src/setupProxy.js.
    // In the built/single-server setup there is no proxy — FastAPI serves both
    // the compiled UI and /api from the same origin (see api/main.py).
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
  // Vitest configuration (https://vitest.dev/config/).
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './src/setupTests.ts',
    css: true,
  },
});
