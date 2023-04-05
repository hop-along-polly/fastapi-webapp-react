import { Route, Routes } from 'react-router-dom';
import Home from './pages/home';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/test" element={<p>Test</p>} />
    </Routes>
  );
};

export default App;
