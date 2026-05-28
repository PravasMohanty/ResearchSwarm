const API_BASE = import.meta.env.VITE_API_URL;

/**
 * Authenticate against the backend.
 */
export async function login(username, password) {
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Login failed' }));
    throw new Error(err.detail || 'Invalid credentials');
  }

  return res.json();
}

/**
 * Start a research query (requires HTTP Basic auth).
 */
export async function startResearch(query, username, password) {
  const basicToken = btoa(`${username}:${password}`);

  const res = await fetch(`${API_BASE}/research/start`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Basic ${basicToken}`,
    },
    body: JSON.stringify({ query }),
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Research failed' }));
    throw new Error(err.detail || 'Something went wrong');
  }

  return res.json();
}

/**
 * Fetch the list of all past research reports.
 * Returns { history: [{ filename, query, title, created_at }] }
 */
export async function fetchHistory(username, password) {
  const basicToken = btoa(`${username}:${password}`);

  const res = await fetch(`${API_BASE}/research/history`, {
    headers: {
      'Authorization': `Basic ${basicToken}`,
    },
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Failed to load history' }));
    throw new Error(err.detail || 'Failed to load history');
  }

  return res.json();
}

/**
 * Fetch a specific past research report by filename.
 * Returns { query, raw_report, report_text, created_at }
 */
export async function fetchHistoryEntry(filename, username, password) {
  const basicToken = btoa(`${username}:${password}`);

  const res = await fetch(`${API_BASE}/research/history/${encodeURIComponent(filename)}`, {
    headers: {
      'Authorization': `Basic ${basicToken}`,
    },
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Failed to load report' }));
    throw new Error(err.detail || 'Failed to load report');
  }

  return res.json();
}
