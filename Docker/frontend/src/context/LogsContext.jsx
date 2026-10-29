import { createContext, useContext, useState } from "react";

const LogsContext = createContext(null);

export function LogsProvider({ children }) {
  const [logs, setLogs] = useState([]);

  const addLog = (log) => setLogs((prev) => [...prev, log]);

  return (
    <LogsContext.Provider value={{ logs, addLog }}>
      {children}
    </LogsContext.Provider>
  );
}

export function useLogs() {
  const ctx = useContext(LogsContext);
  if (!ctx) throw new Error("useLogs must be used within LogsProvider");
  return ctx;
}
