import { createContext, useContext, useState } from "react";

const DeviceContext = createContext(null);

export function DeviceProvider({ children }) {
  const [status, setStatus] = useState({
    connected: false,
    lastUpdate: null,
  });

  return (
    <DeviceContext.Provider value={{ status, setStatus }}>
      {children}
    </DeviceContext.Provider>
  );
}

export function useDevice() {
  const ctx = useContext(DeviceContext);
  if (!ctx) throw new Error("useDevice must be used within DeviceProvider");
  return ctx;
}
