import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext.jsx';
import { login } from '../services/api.js';
import GlassCard from '../components/GlassCard.jsx';
import InputField from '../components/InputField.jsx';
import GradientButton from '../components/GradientButton.jsx';
import FloatingParticles from '../components/FloatingParticles.jsx';
import './LoginPage.css';

function LoginPage() {
  const [userId, setUserId] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [shake, setShake] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { saveAuth } = useAuth();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');

    if (!userId.trim() || !password.trim()) {
      setShake(true);
      setTimeout(() => setShake(false), 600);
      return;
    }

    setLoading(true);

    try {
      await login(userId, password);
      // Credentials are valid — persist them for subsequent API calls
      saveAuth(userId, password);
      navigate('/research');
    } catch (err) {
      setError(err.message || 'Invalid credentials');
      setShake(true);
      setTimeout(() => setShake(false), 600);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-wrapper login-page">
      <FloatingParticles count={8} />

      <div className={`login-container ${shake ? 'shake' : ''}`}>
        <GlassCard className="login-card">
          {/* Logo / Brand */}
          <div className="login-brand">
            <div className="brand-icon">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                <defs>
                  <linearGradient id="logoGrad" x1="0" y1="0" x2="32" y2="32" gradientUnits="userSpaceOnUse">
                    <stop stopColor="#6c5ce7" />
                    <stop offset="0.5" stopColor="#a29bfe" />
                    <stop offset="1" stopColor="#74b9ff" />
                  </linearGradient>
                </defs>
                <circle cx="16" cy="16" r="14" stroke="url(#logoGrad)" strokeWidth="2.5" fill="none" />
                <path d="M11 16.5L14.5 20L21 12" stroke="url(#logoGrad)" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
            </div>
            <h1 className="brand-title">ResearchSwarm</h1>
            <p className="brand-subtitle">Deep research, powered by AI</p>
          </div>

          {/* Form */}
          <form className="login-form" onSubmit={handleLogin}>
            <InputField
              id="userid"
              label="User ID"
              value={userId}
              onChange={(e) => setUserId(e.target.value)}
              delay={200}
            />

            <InputField
              id="password"
              label="Password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              delay={350}
            />

            {error && (
              <p className="login-error">{error}</p>
            )}

            <GradientButton
              type="submit"
              loading={loading}
              delay={500}
            >
              Sign In
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M5 12h14M12 5l7 7-7 7" />
              </svg>
            </GradientButton>
          </form>

          {/* Footer hint */}
          <p className="login-footer">
            Authenticate with your ResearchSwarm credentials
          </p>
        </GlassCard>
      </div>
    </div>
  );
}

export default LoginPage;
