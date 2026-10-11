import { useState } from "react";

export default function CommandForm({ onSend }) {
  const [command, setCommand] = useState("");

  const submit = (e) => {
    e.preventDefault();
    onSend({ deviceId: "raspberry", command });
    setCommand("");
  };

  return (
    <form onSubmit={submit} className="flex flex-wrap items-center justify-center gap-3">
      <input
        value={command}
        onChange={(e) => setCommand(e.target.value)}
        placeholder="Comando"
        className="min-w-0 rounded-md border border-slate-500 bg-slate-800 px-4 py-2 text-white placeholder-slate-400 shadow-sm outline-none transition focus:border-blue-400 focus:ring-2 focus:ring-blue-400/40"
      />
      <button
        type="submit"
        className="rounded-md bg-blue-600 px-5 py-2 font-semibold text-white shadow-sm transition hover:bg-blue-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-400"
      >
        Enviar
      </button>
    </form>
  );
}
