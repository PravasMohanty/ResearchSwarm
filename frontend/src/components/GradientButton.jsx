import { useState, useRef } from 'react';
import './GradientButton.css';

function GradientButton({ children, onClick, loading = false, delay = 0, type = 'button' }) {
  const [ripples, setRipples] = useState([]);
  const btnRef = useRef(null);

  const handleClick = (e) => {
    if (loading) return;

    const rect = btnRef.current.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const id = Date.now();

    setRipples((prev) => [...prev, { x, y, id }]);
    setTimeout(() => {
      setRipples((prev) => prev.filter((r) => r.id !== id));
    }, 700);

    onClick && onClick(e);
  };

  return (
    <button
      ref={btnRef}
      type={type}
      className={`gradient-btn ${loading ? 'loading' : ''}`}
      onClick={handleClick}
      disabled={loading}
      style={{ animationDelay: `${delay}ms` }}
    >
      <span className="btn-content">
        {loading ? (
          <span className="btn-spinner">
            <span className="spinner-dot" />
            <span className="spinner-dot" />
            <span className="spinner-dot" />
          </span>
        ) : (
          children
        )}
      </span>
      <span className="btn-shine" />
      {ripples.map((r) => (
        <span
          key={r.id}
          className="btn-ripple"
          style={{ left: r.x, top: r.y }}
        />
      ))}
    </button>
  );
}

export default GradientButton;
