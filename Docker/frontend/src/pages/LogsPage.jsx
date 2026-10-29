import LogViewer from "../components/logs/LogViewer";
import { useLogs } from "../context/LogsContext";

export default function LogsPage() {
  const { logs } = useLogs();

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4 text-white">Logs</h2>
      <LogViewer logs={logs} />
    </div>
  );
}
