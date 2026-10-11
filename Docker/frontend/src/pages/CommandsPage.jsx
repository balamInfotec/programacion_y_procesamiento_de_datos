import CommandForm from "../components/commands/CommandForm";
import { useLogs } from "../context/LogsContext";

export default function CommandsPage() {
  const { addLog } = useLogs();

  const sendCommand = (cmd) => {
    // El WebSocket está en DashboardLayout
    // Lo enviamos usando window.ws para simplificar
    window.ws.send(JSON.stringify(cmd));
    addLog({ type: "command", command: cmd });
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4 text-white">Enviar Comandos</h2>
      <CommandForm onSend={sendCommand} />
    </div>
  );
}
