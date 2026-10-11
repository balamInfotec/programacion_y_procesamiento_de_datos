import { useState, useEffect } from "react";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

import TelemetryPage from "../../pages/TelemetryPage";
import CommandsPage from "../../pages/CommandsPage";
import LogsPage from "../../pages/LogsPage";
import DevicePage from "../../pages/DevicePage";

import { useTelemetry } from "../../context/TelemetryContext";
import { useLogs } from "../../context/LogsContext";
import { useDevice } from "../../context/DeviceContext";

import { createWebSocket } from "../../services/websocketService";

export default function DashboardLayout({ children }) {
  const { setMetrics } = useTelemetry();
  const { addLog } = useLogs();
  const { setStatus } = useDevice();

  const [page, setPage] = useState("telemetry");

  useEffect(() => {
    const ws = createWebSocket((msg) => {
      if (msg.metrics) setMetrics(msg.metrics);
      addLog(msg);
      setStatus({
        connected: true,
        lastUpdate: msg.timestamp || new Date().toISOString(),
      });
    });

    window.ws = ws; // para enviar comandos

    return () => ws.close();
  }, []);

  const renderPage = () => {
    switch (page) {
      case "telemetry": return <TelemetryPage />;
      case "commands": return <CommandsPage />;
      case "logs": return <LogsPage />;
      case "device": return <DevicePage />;
      default: return <TelemetryPage />;
    }
  };

  return (
    <div className="flex h-screen flex-col overflow-hidden bg-slate-950 text-white">
      <Navbar />
      <div className="flex min-h-0 flex-1">
        <Sidebar setPage={setPage} />
        <main className="min-h-0 flex-1 overflow-y-auto p-6">
          {renderPage()}
        </main>
      </div>
    </div>
  );
}
