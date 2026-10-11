import { createContext, useContext, useState } from "react";

const TelemetryContext = createContext(null);

export function TelemetryProvider({ children }) {
  const [metrics, setMetrics] = useState({});

  return (
    <TelemetryContext.Provider value={{ metrics, setMetrics }}>
      {children}
    </TelemetryContext.Provider>
  );
}

export function useTelemetry() {
  const ctx = useContext(TelemetryContext);
  if (!ctx) throw new Error("useTelemetry must be used within TelemetryProvider");
  return ctx;
}
