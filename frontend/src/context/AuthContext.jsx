import { createContext, useContext, useState, useCallback } from 'react';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [auth, setAuth] = useState(() => {
    const stored = sessionStorage.getItem('rs_auth');
    return stored ? JSON.parse(stored) : null;
  });

  const saveAuth = useCallback((username, password) => {
    const data = { username, password };
    sessionStorage.setItem('rs_auth', JSON.stringify(data));
    setAuth(data);
  }, []);

  const clearAuth = useCallback(() => {
    sessionStorage.removeItem('rs_auth');
    setAuth(null);
  }, []);

  return (
    <AuthContext.Provider value={{ auth, saveAuth, clearAuth }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used inside AuthProvider');
  return ctx;
}
