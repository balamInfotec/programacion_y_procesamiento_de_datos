export function createWebSocket(onMessage) {
  const ws = new WebSocket(import.meta.env.VITE_WS_URL);

  ws.onopen = () => console.log("[WS] Conectado");
  ws.onerror = (err) => console.error("[WS] Error:", err);
  ws.onclose = () => console.log("[WS] Cerrado");

  ws.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data);
      onMessage(data);
    } catch (err) {
      console.error("[WS] Error al parsear mensaje:", err);
    }
  };

  return ws;
}
