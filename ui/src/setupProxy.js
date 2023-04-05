// https://create-react-app.dev/docs/proxying-api-requests-in-development/#configuring-the-proxy-manually
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'http://localhost:8000',
      changeOrigin: true,
    })
  );
};
