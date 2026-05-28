import { Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from './pages/LoginPage.jsx';
import ResearchPage from './pages/ResearchPage.jsx';
import BackgroundMesh from './components/BackgroundMesh.jsx';

function App() {
  return (
    <>
      <BackgroundMesh />
      <Routes>
        <Route path="/" element={<Navigate to="/login" replace />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/research" element={<ResearchPage />} />
      </Routes>
    </>
  );
}

export default App;
