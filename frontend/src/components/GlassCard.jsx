import './GlassCard.css';

function GlassCard({ children, className = '', delay = 0 }) {
  return (
    <div
      className={`glass-card ${className}`}
      style={{ animationDelay: `${delay}ms` }}
    >
      {children}
    </div>
  );
}

export default GlassCard;
