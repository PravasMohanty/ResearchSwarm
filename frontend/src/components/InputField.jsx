import { useState } from 'react';
import './InputField.css';

function InputField({ id, label, type = 'text', value, onChange, delay = 0 }) {
  const [focused, setFocused] = useState(false);

  return (
    <div
      className={`input-group ${focused || value ? 'active' : ''}`}
      style={{ animationDelay: `${delay}ms` }}
    >
      <div className="input-wrapper">
        <input
          id={id}
          type={type}
          value={value}
          onChange={onChange}
          onFocus={() => setFocused(true)}
          onBlur={() => setFocused(false)}
          autoComplete="off"
          required
        />
        <label htmlFor={id}>{label}</label>
        <div className="input-border" />
        <div className="input-glow" />
      </div>
    </div>
  );
}

export default InputField;
