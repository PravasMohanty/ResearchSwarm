import { useState, useEffect, useCallback } from 'react';
import { useAuth } from '../context/AuthContext.jsx';
import { fetchHistory } from '../services/api.js';
import './HistorySidebar.css';

function HistorySidebar({ open, onClose, onSelectEntry, refreshKey }) {
  const [entries, setEntries] = useState([]);
  const [loading, setLoading] = useState(false);
  const { auth } = useAuth();

  const loadHistory = useCallback(async () => {
    if (!auth) return;
    setLoading(true);
    try {
      const data = await fetchHistory(auth.username, auth.password);
      setEntries(data.history || []);
    } catch {
      setEntries([]);
    } finally {
      setLoading(false);
    }
  }, [auth]);

  // Reload whenever sidebar opens or refreshKey changes (new research completed)
  useEffect(() => {
    if (open) loadHistory();
  }, [open, refreshKey, loadHistory]);

  const formatDate = (iso) => {
    if (!iso) return '';
    const d = new Date(iso);
    return d.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  const truncateQuery = (q, max = 80) => {
    if (!q) return 'Untitled';
    return q.length > max ? q.slice(0, max) + '…' : q;
  };

  return (
    <>
      {/* Overlay */}
      <div
        className={`sidebar-overlay ${open ? 'visible' : ''}`}
        onClick={onClose}
      />

      {/* Sidebar panel */}
      <aside className={`history-sidebar ${open ? 'open' : ''}`}>
        {/* Header */}
        <div className="sidebar-header">
          <div className="sidebar-title-row">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="12" cy="12" r="10" />
              <polyline points="12 6 12 12 16 14" />
            </svg>
            <h2 className="sidebar-title">Research History</h2>
          </div>
          <button className="sidebar-close" onClick={onClose} title="Close">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <line x1="18" y1="6" x2="6" y2="18" />
              <line x1="6" y1="6" x2="18" y2="18" />
            </svg>
          </button>
        </div>

        {/* Content */}
        <div className="sidebar-content">
          {loading && (
            <div className="sidebar-loading">
              <div className="sidebar-skeleton" />
              <div className="sidebar-skeleton short" />
              <div className="sidebar-skeleton" />
              <div className="sidebar-skeleton short" />
            </div>
          )}

          {!loading && entries.length === 0 && (
            <div className="sidebar-empty">
              <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
                <polyline points="14 2 14 8 20 8" />
              </svg>
              <p>No research history yet</p>
              <span>Your past research will appear here</span>
            </div>
          )}

          {!loading && entries.length > 0 && (
            <ul className="history-list">
              {entries.map((entry, i) => (
                <li
                  key={entry.filename}
                  className="history-item"
                  style={{ animationDelay: `${i * 0.05}s` }}
                  onClick={() => {
                    onSelectEntry(entry.filename);
                    onClose();
                  }}
                >
                  <div className="history-item-icon">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <circle cx="11" cy="11" r="8" />
                      <path d="M21 21l-4.35-4.35" />
                    </svg>
                  </div>
                  <div className="history-item-body">
                    <p className="history-item-title">
                      {entry.title || 'Untitled Research'}
                    </p>
                    <p className="history-item-query">
                      {truncateQuery(entry.query)}
                    </p>
                    <span className="history-item-date">
                      {formatDate(entry.created_at)}
                    </span>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>
      </aside>
    </>
  );
}

export default HistorySidebar;
