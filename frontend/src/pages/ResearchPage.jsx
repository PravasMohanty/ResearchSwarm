import { useState, useCallback } from 'react';
import { useNavigate, Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext.jsx';
import { startResearch, fetchHistoryEntry } from '../services/api.js';
import GlassCard from '../components/GlassCard.jsx';
import GradientButton from '../components/GradientButton.jsx';
import SkeletonLoader from '../components/SkeletonLoader.jsx';
import FloatingParticles from '../components/FloatingParticles.jsx';
import HistorySidebar from '../components/HistorySidebar.jsx';
import './ResearchPage.css';

function ResearchPage() {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [historyRefreshKey, setHistoryRefreshKey] = useState(0);
  const [viewingHistory, setViewingHistory] = useState(false);
  const { auth, clearAuth } = useAuth();
  const navigate = useNavigate();

  // Redirect to login if no credentials stored
  if (!auth) {
    return <Navigate to="/login" replace />;
  }

  const handleResearch = async () => {
    if (!query.trim()) return;
    setLoading(true);
    setResult(null);
    setError('');
    setViewingHistory(false);

    try {
      const data = await startResearch(query, auth.username, auth.password);
      setResult(data);
      // Bump the key so sidebar reloads on next open
      setHistoryRefreshKey((k) => k + 1);
    } catch (err) {
      if (err.message === 'Invalid credentials') {
        clearAuth();
        navigate('/login', { replace: true });
        return;
      }
      setError(err.message || 'Research failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleSelectHistoryEntry = useCallback(async (filename) => {
    setLoading(true);
    setResult(null);
    setError('');
    setViewingHistory(true);

    try {
      const data = await fetchHistoryEntry(filename, auth.username, auth.password);
      setResult({
        report: data.report_text,
        raw_report: data.raw_report,
        filename,
      });
      // Also populate the query bar with the original query
      setQuery(data.query || '');
    } catch (err) {
      setError(err.message || 'Failed to load report');
    } finally {
      setLoading(false);
    }
  }, [auth]);

  const handleLogout = () => {
    clearAuth();
    navigate('/login', { replace: true });
  };

  const handleNewResearch = () => {
    setResult(null);
    setError('');
    setQuery('');
    setViewingHistory(false);
  };

  // Extract structured data from the response
  const rawReport = result?.raw_report;
  const sections = rawReport?.sections || [];
  const executiveSummary = rawReport?.executive_summary;
  const reportTitle = rawReport?.title;
  const sources = rawReport?.sources || [];
  const finalConclusion = rawReport?.final_conclusion;

  return (
    <div className="page-wrapper research-page">
      <FloatingParticles count={10} />

      {/* History Sidebar */}
      <HistorySidebar
        open={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
        onSelectEntry={handleSelectHistoryEntry}
        refreshKey={historyRefreshKey}
      />

      {/* Top bar */}
      <div className="top-bar">
        {/* Hamburger menu */}
        <button
          className="hamburger-btn"
          onClick={() => setSidebarOpen(true)}
          title="Research history"
        >
          <span className="hamburger-line" />
          <span className="hamburger-line" />
          <span className="hamburger-line" />
        </button>

        {/* Logout */}
        <button className="logout-btn" onClick={handleLogout} title="Sign out">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" />
            <polyline points="16 17 21 12 16 7" />
            <line x1="21" y1="12" x2="9" y2="12" />
          </svg>
        </button>
      </div>

      <div className="research-container">
        {/* Header */}
        <div className="research-header">
          <h1 className="research-welcome">
            Welcome<span className="accent-dot">.</span>
          </h1>
          <p className="research-prompt">
            Write a detailed question to research on — our AI swarm will do the rest
          </p>
        </div>

        {/* Query Card */}
        <GlassCard className="research-card" delay={200}>
          <div className="textarea-wrapper">
            <textarea
              id="research-query"
              className="research-textarea"
              placeholder="e.g. What are the latest breakthroughs in quantum computing and how might they affect cryptography in the next decade?"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              rows={4}
              disabled={loading}
            />
            <div className="textarea-counter">
              {query.length} characters
            </div>
          </div>

          <GradientButton
            onClick={handleResearch}
            loading={loading}
            delay={400}
          >
            Start Research
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="11" cy="11" r="8" />
              <path d="M21 21l-4.35-4.35" />
            </svg>
          </GradientButton>
        </GlassCard>

        {/* Error */}
        {error && (
          <div className="results-section">
            <GlassCard className="error-card">
              <div className="error-content">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <circle cx="12" cy="12" r="10" />
                  <line x1="12" y1="8" x2="12" y2="12" />
                  <line x1="12" y1="16" x2="12.01" y2="16" />
                </svg>
                <p>{error}</p>
              </div>
            </GlassCard>
          </div>
        )}

        {/* Loading Skeleton */}
        {loading && (
          <div className="results-section">
            <SkeletonLoader />
          </div>
        )}

        {/* Results */}
        {rawReport && !loading && (
          <div className="results-section">
            {/* Viewing history badge */}
            {viewingHistory && (
              <div className="history-badge">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <circle cx="12" cy="12" r="10" />
                  <polyline points="12 6 12 12 16 14" />
                </svg>
                <span>Viewing past research</span>
                <button className="new-research-link" onClick={handleNewResearch}>
                  New Research →
                </button>
              </div>
            )}

            <GlassCard className="result-card">
              {/* Header */}
              <div className="result-header">
                <div className="result-icon">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
                    <polyline points="22 4 12 14.01 9 11.01" />
                  </svg>
                </div>
                <h2 className="result-title">{reportTitle || 'Research Complete'}</h2>
              </div>

              {/* Executive Summary */}
              {executiveSummary && (
                <div className="result-summary-block">
                  <h3 className="section-label">Executive Summary</h3>
                  <p className="result-summary">{executiveSummary}</p>
                </div>
              )}

              {/* Sections */}
              {sections.length > 0 && (
                <div className="result-sections">
                  {sections.map((section, i) => (
                    <div
                      key={i}
                      className="report-section"
                      style={{ animationDelay: `${i * 0.12}s` }}
                    >
                      <h3 className="report-section-title">{section.title}</h3>
                      <p className="report-section-content">{section.content}</p>

                      {section.findings && section.findings.length > 0 && (
                        <ul className="section-findings">
                          {section.findings.map((finding, j) => (
                            <li key={j} className="section-finding-item">
                              <span className="finding-bullet" />
                              <div>
                                <p className="finding-claim">{finding.claim}</p>
                                {finding.confidence != null && (
                                  <span className="finding-confidence">
                                    {Math.round(finding.confidence * 100)}% confidence
                                  </span>
                                )}
                              </div>
                            </li>
                          ))}
                        </ul>
                      )}
                    </div>
                  ))}
                </div>
              )}

              {/* Final Conclusion */}
              {finalConclusion && (
                <div className="result-conclusion">
                  <h3 className="section-label">Conclusion</h3>
                  <p className="result-summary">{finalConclusion}</p>
                </div>
              )}

              {/* Sources */}
              {sources.length > 0 && (
                <div className="result-sources">
                  <h3 className="section-label">Sources</h3>
                  <ul className="sources-list">
                    {sources.map((src, i) => (
                      <li key={i} className="source-item">
                        <span className="source-number">{i + 1}</span>
                        <a href={src} target="_blank" rel="noopener noreferrer" className="source-link">
                          {src}
                        </a>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </GlassCard>
          </div>
        )}
      </div>
    </div>
  );
}

export default ResearchPage;
