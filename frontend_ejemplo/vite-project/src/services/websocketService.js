export function createWebSocket(onMessage) {
  const ws = new WebSocket("ws://localhost:8000/ws");

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
