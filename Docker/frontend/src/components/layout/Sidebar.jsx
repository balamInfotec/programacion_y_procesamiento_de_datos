import { useState } from "react";
import TelemetryPage from "../../pages/TelemetryPage";
import CommandsPage from "../../pages/CommandsPage";
import LogsPage from "../../pages/LogsPage";
import DevicePage from "../../pages/DevicePage";

export default function Sidebar({ setPage }) {
  return (
    <aside className="w-64 h-full bg-slate-900 border-r border-slate-700 p-4">
      <nav className="flex flex-col gap-4 text-slate-300">
        <button onClick={() => setPage("telemetry")} className="hover:text-white text-left">Telemetría</button>
        <button onClick={() => setPage("commands")} className="hover:text-white text-left">Comandos</button>
        <button onClick={() => setPage("logs")} className="hover:text-white text-left">Logs</button>
        <button onClick={() => setPage("device")} className="hover:text-white text-left">Estado del dispositivo</button>
      </nav>
    </aside>
  );
}
