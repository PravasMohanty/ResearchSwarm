import './SkeletonLoader.css';

function SkeletonLoader() {
  return (
    <div className="skeleton-container">
      <div className="skeleton-header">
        <div className="skeleton-icon pulse-glow" />
        <div className="skeleton-title-group">
          <div className="skeleton-line skeleton-w70" />
          <div className="skeleton-line skeleton-w40" style={{ animationDelay: '0.15s' }} />
        </div>
      </div>

      <div className="skeleton-body">
        <div className="skeleton-line skeleton-w100" style={{ animationDelay: '0.1s' }} />
        <div className="skeleton-line skeleton-w90" style={{ animationDelay: '0.2s' }} />
        <div className="skeleton-line skeleton-w95" style={{ animationDelay: '0.3s' }} />
        <div className="skeleton-line skeleton-w80" style={{ animationDelay: '0.4s' }} />
        <div className="skeleton-line skeleton-w60" style={{ animationDelay: '0.5s' }} />
      </div>

      <div className="skeleton-divider" />

      <div className="skeleton-body">
        <div className="skeleton-line skeleton-w85" style={{ animationDelay: '0.55s' }} />
        <div className="skeleton-line skeleton-w100" style={{ animationDelay: '0.65s' }} />
        <div className="skeleton-line skeleton-w75" style={{ animationDelay: '0.75s' }} />
      </div>

      <div className="skeleton-status">
        <div className="skeleton-dot pulse-glow" />
        <span className="skeleton-status-text">Researching your question...</span>
      </div>
    </div>
  );
}

export default SkeletonLoader;
